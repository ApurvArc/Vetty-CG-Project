📈 Crypto Market API

FastAPI-based cryptocurrency market data service powered by the CoinGecko API.
Implements authentication, pagination, INR/CAD currency conversion, categories, and coin lookups.

🚀 Features (Version 1.0)
✅ Basic Requirements

List all coins (with coin IDs)

List all coin categories

Fetch market data for a specific coin

Market prices returned in INR (₹) and CAD ($)

Pagination support

page_num → default 1

per_page → default 10

Token-based authentication

API requires a valid x-api-key header

Swagger documentation available at /docs

Unit tests included (pytest, pytest-cov)

⭐ Extra Features

Docker + Docker Compose support

Health check endpoint

Version information endpoint

Environment-based configuration

Linting setup (pyproject.toml)

🗂 Project Structure
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
├── pyproject.toml
├── README.md
└── requirements.txt

🔑 Authentication

Every endpoint requires a valid API key.

Include this header in all requests:

x-api-key: YOUR_INTERNAL_API_KEY


Your .env file should include:

COINGECKO_API_KEY=your-key-here
INTERNAL_API_KEY=your-secret-token


Do not commit real secrets. Only commit .env.example.

🔧 Installation & Local Development
1️⃣ Clone the repository
git clone https://github.com/ApurvArc/crypto_market_api.git
cd crypto_market_api

2️⃣ Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file
copy .env.example .env


Add your API keys.

5️⃣ Run the API locally
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000


API will start at:

http://localhost:8000


Swagger docs:

http://localhost:8000/docs

📡 API Endpoints
🔹 GET /coins

List coins (paginated).

Example:

GET /coins?page_num=1&per_page=10


Headers:

x-api-key: YOUR_INTERNAL_API_KEY

🔹 GET /categories

Returns list of cryptocurrency categories.

🔹 GET /coins/{coin_id}

Returns detailed market data for a specific coin.

Example:

GET /coins/bitcoin


Currency output:

{
  "bitcoin": {
    "inr": 7450000,
    "cad": 122000
  }
}

📦 Running with Docker
Build image
docker build -t crypto-market-api .

Run container
docker run -p 8000:8000 --env-file .env crypto-market-api

With docker-compose
docker-compose up --build

🧪 Running Tests

Run unit tests:

pytest


Run with coverage:

pytest --cov=app

🩺 Health & Version Endpoints
GET /health

Checks:

Application status

CoinGecko service availability

GET /version

Returns:

{
  "version": "1.0.0",
  "framework": "FastAPI",
  "python": "3.11"
}

🧹 Code Quality

Linting + formatting:

ruff check .
black .
isort .


(Packages configured in pyproject.toml)

🛠 Tech Stack

FastAPI

Pydantic

Uvicorn

Requests / HTTPX

Pytest

Docker

Swagger / OpenAPI

🙌 Author

Apurv
GitHub: https://github.com/ApurvArc