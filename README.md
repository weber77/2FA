# FastAPI Bookings API

This is a simple FastAPI application for managing bookings, students, subscriptions, lessons, courses, reviews, FAQs, and availability.

## Endpoints

# FastAPI Bookings API

This is a simple FastAPI application for managing bookings, students, subscriptions, lessons, courses, reviews, FAQs, and availability.

## Endpoints

### Create a Booking

- **URL:** `/bookings/`
- **Method:** `POST`
- **Request Body:** JSON object representing a booking
- **Response:** The created booking

### Get a Booking by ID

- **URL:** `/bookings/{booking_id}`
- **Method:** `GET`
- **Response:** The booking with the specified ID, or a 404 error if not found

### Create a Student

- **URL:** `/students/`
- **Method:** `POST`
- **Request Body:** JSON object representing a student
- **Response:** The created student

### Get a Student by ID

- **URL:** `/students/{student_id}`
- **Method:** `GET`
- **Response:** The student with the specified ID, or a 404 error if not found

### Update a Student

- **URL:** `/students/{student_id}`
- **Method:** `PUT`
- **Request Body:** JSON object representing the updated student
- **Response:** The updated student

### Create a Subscription

- **URL:** `/subscriptions/`
- **Method:** `POST`
- **Request Body:** JSON object representing a subscription
- **Response:** The created subscription

### Get a Subscription by ID

- **URL:** `/subscriptions/{subscription_id}`
- **Method:** `GET`
- **Response:** The subscription with the specified ID, or a 404 error if not found

### Create a Lesson

- **URL:** `/lessons/`
- **Method:** `POST`
- **Request Body:** JSON object representing a lesson
- **Response:** The created lesson

### Get a Lesson by ID

- **URL:** `/lessons/{lesson_id}`
- **Method:** `GET`
- **Response:** The lesson with the specified ID, or a 404 error if not found

### Create a Course

- **URL:** `/courses/`
- **Method:** `POST`
- **Request Body:** JSON object representing a course
- **Response:** The created course

### Get a Course by ID

- **URL:** `/courses/{course_id}`
- **Method:** `GET`
- **Response:** The course with the specified ID, or a 404 error if not found

### Update a Course

- **URL:** `/courses/{course_id}`
- **Method:** `PUT`
- **Request Body:** JSON object representing the updated course
- **Response:** The updated course

### Create a Review

- **URL:** `/reviews/`
- **Method:** `POST`
- **Request Body:** JSON object representing a review
- **Response:** The created review

### Get a Review by ID

- **URL:** `/reviews/{review_id}`
- **Method:** `GET`
- **Response:** The review with the specified ID, or a 404 error if not found

### Create an FAQ

- **URL:** `/faqs/`
- **Method:** `POST`
- **Request Body:** JSON object representing an FAQ
- **Response:** The created FAQ

### Get an FAQ by ID

- **URL:** `/faqs/{faq_id}`
- **Method:** `GET`
- **Response:** The FAQ with the specified ID, or a 404 error if not found

### Update an FAQ

- **URL:** `/faqs/{faq_id}`
- **Method:** `PUT`
- **Request Body:** JSON object representing the updated FAQ
- **Response:** The updated FAQ

### Set Availability

- **URL:** `/availability/`
- **Method:** `POST`
- **Request Body:** JSON object representing an availability period
- **Response:** The created availability period

### Get Availability

- **URL:** `/availability/`
- **Method:** `GET`
- **Response:** List of all availability periods

### Update Availability

- **URL:** `/availability/{availability_id}`
- **Method:** `PUT`
- **Request Body:** JSON object representing the updated availability period
- **Response:** The updated availability period

### Create an Admin

- **URL:** `/admins/`
- **Method:** `POST`
- **Request Body:** JSON object representing an admin
- **Response:** The created admin

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

- FastAPI
- Uvicorn
- Stripe
- Firebase Admin SDK
- bcrypt

## License

This project is licensed under the MIT License.

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

- FastAPI
- Uvicorn
- Stripe
- Firebase Admin SDK
- bcrypt

## License

This project is licensed under the MIT License.
