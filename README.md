# Crypto Market API

A production-ready FastAPI service that provides cryptocurrency market data powered by the CoinGecko API. This project was built as part of the **Vetty Intern – Python API Technical Exercise** and implements all required features including authentication, pagination, Docker support, and unit tests.

---

## 🚀 Features Implemented (Per Assignment Requirements)

### ✅ 1. List all coins including coin ID

Endpoint: `/coins`

### ✅ 2. List all coin categories

Endpoint: `/categories`

### ✅ 3. Get specific coins (by ID or category)

* Supports INR and CAD market prices
* Supports pagination using `page_num` and `per_page`
  Endpoint: `/coins/filter`

### ✅ 4. Authentication

The API uses token-based header authentication:

```
x-api-key: <INTERNAL_API_KEY>
```

### ✅ 5. Swagger API Documentation

Available automatically at:

```
http://localhost:8000/docs
```

### ✅ 6. Unit Tests Included

Run tests using:

```
pytest --cov
```

### ✅ 7. Docker Support

Run using Docker Compose:

```
docker-compose up --build
```

### ✅ 8. Linting & Quality Control

Configured via `pyproject.toml`.

---

## 📁 Project Structure

```
crypto_market_api/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── coingecko_client.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_api.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Create virtual environment

```
python -m venv .venv
```

### 2️⃣ Activate environment (Windows)

```
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Copy environment template

```
cp .env.example .env
```

Fill environment variables:

```
COINGECKO_API_KEY=your_api_key_here
INTERNAL_API_KEY=your_internal_access_key
```

### 5️⃣ Run the API

```
uvicorn app:app --reload
```

API runs at:

```
http://localhost:8000
```

---

## 🧪 Running Tests

```
pytest --cov
```

---

## 🐳 Running in Docker

```
docker-compose up --build
```

---

## 🩺 Health Check & Version Info

**Health Check:** `/health`
**Version:** `/version`

---

## 🔐 Authentication

Every API request must include:

```
x-api-key: your_internal_api_key
```

Example cURL:

```
curl -H "x-api-key: Apurv12345" http://localhost:8000/coins
```

---

## 📌 Submission Notes (For Vetty Review Team)

This project demonstrates:

* Clean architecture following KISS, DRY, and Zen of Python
* Secure environment variable handling
* Clear documentation
* Proper authentication
* Pagination support
* Dockerized deployment
* Unit test coverage
* Modular and professional project structure

---

## 🙌 Author

**Apurv Choudhary**
GitHub: [https://github.com/ApurvArc](https://github.com/ApurvArc)
