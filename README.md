# Student Registration App

This is a Django-based web application for student registration. It implements basic Create, Read, Update, Delete functionalities.

## Features

  Create a new student record
  Read/view existing student records
  Update student information
  Delete a student record

## Prerequisites

Before you begin, ensure you have met the following requirements:

Python 3.x installed on your machine
Virtual environment package (`virtualenv`) installed

## Installation

1. Clone the repository to your local machine:

    ```sh
    git clone <https://github.com/dulinajayarathna/student_resgistration_app.git>
    ```

2. Navigate to the project directory:

    ```sh
    cd <student_resgistration_app>
    ```

3. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Set up environment variables:

     Copy the contents of `.env.example` to a new file named `.env`:

        ```sh
        cp .env.example .env
        ```

      Open `.env` and update the environment variables as needed.

6. Apply database migrations:

    ```sh
    python manage.py migrate
    ```

## Usage

1. Start the development server:

    ```sh
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Project Structure

`manage.py`: Django's command-line utility for administrative tasks.
 `requirements.txt`: List of dependencies required for the project.
 `.env`: Environment variables for the project.
 `.env.example`: Example environment variables file.

## Dependencies

```python
Django~=5.0.7
djangorestframework~=3.15.2
mysqlclient~=2.2.4
python-dotenv~=1.0.1



