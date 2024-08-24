# FastAPI 2FA seed phrase

This is a simple FastAPI application for 2FA authentication with seed phrase and QR code generation.

## Setup

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```sh
   virtualenv virtualenv
   source virtualenv/bin/activate # On Windows use `virtualenv\Scripts\activate`
   # OR
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip3 install -r requirements.txt
   ```

4. Run the FastAPI application:

   ```sh
   uvicorn main:app --reload
   ```

## Dependencies

- fastapi
- uvicorn
- pyotp
- qrcode
- pydantic
- Pillow
- qrcode[pil]
- svg2png
- cairosvg
- mnemonic

## License

This project is licensed under the MIT License.
