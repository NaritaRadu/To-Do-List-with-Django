# To-Do List App (Django & TDD)

A dynamic To-Do List web application built with Python and Django, developed using Test-Driven Development (TDD) methodologies.

## 🚀 Features

- Functional Tests (FTs) with **Selenium WebDriver**
- Unit Tests with Django's internal test runner
- Dynamic task management (Add, view, and organize items)

## 🛠️ Prerequisites & Installation

1. **Clone the repository:**
   ```bash
   git clone <LINK-REPO-GITHUB>
   cd Django-TDD
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv

**Windows (PowerShell/CMD):**
    ```bash
    .venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run database migrations:**
    ```bash
    python manage.py migrate

5. **Running the Tests:**
To run the functional tests with Selenium:
    ```bash
    python functional_tests.py

**To run Django unit tests:**
    ```bash
    python manage.py test

6. **Running the App Locally**
    ```bash
    python manage.py runserver

7. Open http://localhost:8000 in your browser.