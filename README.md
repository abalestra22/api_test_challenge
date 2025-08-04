# API Automation Challenge - WorldSys

This repository contains an automated test suite for the `/import` endpoint using `pytest` and a Page Object Model (POM) adapted to API testing.

---

##  Test Coverage

- **Happy Path**  
  Sends a valid `POST` request with a `personId` and validates:
  - Status code `200`
  - Response field `"status": "success"`
  - The `personId` is inserted into the database

- **Sad Path**  
  Executes parameterized tests using invalid `personId` values:
  - Nonexistent string
  - Random UUID
  - Negative number
  - Boolean value
  - Null (`None`)

  Expects a `4xx` response and `"status": "error"` in the body

---

## Project Structure

```
api_test_challenge/
├── .venv/
├── tests/
│   ├── test_import_happy.py
│   └── test_import_sad.py
├── utils/
│   ├── endpoints/
│   │   └── import_endpoints.py
│   ├── pages/
│   │   └── person_api.py
│   ├── assertions.py
│   ├── db.py
│   ├── decorators.py
│   ├── logger.py
│   └── conftest.py
├── requirements.txt
└── README.md
```

---

## ⚙Setup

1. Clone the repository:

```bash
git clone https://github.com/abalestra22/api_test_challenge.git
cd api_test_challenge
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Sensitive credentials are handled through environment variables:

```bash
export API_TOKEN="your_token"
export DB_HOST="localhost"
export DB_NAME="worldsys_db"
export DB_USER="admin"
export DB_PASSWORD="password"
```

> You can also use a `.env` file with `python-dotenv` if preferred.

---

## Run the Tests

### Run all tests:

```bash
pytest -v
```

### Run only regression tests:

```bash
pytest -m regression -v
```

### Generate HTML report:

```bash
pytest --html=report.html --self-contained-html
```

---

## Notes

- Implements **Page Object Model (POM)** to separate endpoint logic.
- Uses `pytest.fixture` for authentication and DB configuration.
- Validates data insertion directly against the database.
- Includes logging for request/response tracing.
- Generates HTML reports with `pytest-html`.

---

##  Author

Andrea Balestra  
QA Automation Engineer  
 Argentina
