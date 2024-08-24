from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pyotp
import qrcode
from pydantic import BaseModel
from io import BytesIO
import base64
from fastapi.middleware.cors import CORSMiddleware
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image
import cairosvg
from mnemonic import Mnemonic
import hashlib

app = FastAPI()
# Configure CORS for the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class TokenVerificationRequest(BaseModel):
    token: str
    secret: str

@app.get("/generate_secret/")
def generate_secret():
    # Generate a random secret key
    mnemo = Mnemonic("english")
    secret = mnemo.generate(strength=128)
    return {"secret": secret}

@app.get("/generate_qr/")
def generate_qr(secret: str, username: str):
    # Convert mnemonic to TOTP secret
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(secret)
    totp_secret = hashlib.sha256(seed).digest()[:32]
    totp_secret_base32 = base64.b32encode(totp_secret).decode('utf-8')

    # Generate a QR code that can be scanned by Google Authenticator
    totp = pyotp.TOTP(totp_secret_base32)
    otp_auth_url = totp.provisioning_uri(name=username, issuer_name="Wakamann")

    # Convert SVG to PNG using cairosvg
    # with open("wakamann.svg", "rb") as svg_file:
    #     png_logo = cairosvg.svg2png(file_obj=svg_file)
    # logo = Image.open(BytesIO(png_logo))
    logo = Image.open("wakamann.png")

    # Create QR code
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(otp_auth_url)

    # Create the QR code image with the logo
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), embeded_image=logo)

    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')

    return JSONResponse(content={"qr_code": img_str})

@app.post("/verify_token/")
def verify_token(data: TokenVerificationRequest):
   
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(data.secret)
    totp_secret = hashlib.sha256(seed).digest()[:32]
    totp_secret_base32 = base64.b32encode(totp_secret).decode('utf-8')

    
    totp = pyotp.TOTP(totp_secret_base32)
    
    if totp.verify(data.token):
        return {"status": "success", "message": "Token is valid"}
    else:
        raise HTTPException(status_code=400, detail="Invalid token")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
