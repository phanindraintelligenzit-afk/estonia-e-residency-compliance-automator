# Setup Guide — Estonia E Residency Compliance Automator

## Prerequisites

- Python 3.11+
- Docker (optional)
- Git

## Installation

```bash
git clone https://github.com/phanindraintelligenzit-afk/estonia-e-residency-compliance-automator.git
cd estonia-e-residency-compliance-automator
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run Tests

```bash
pytest tests/ -v
```

## Run Locally

```bash
uvicorn src.pipeline:app --reload
```

## Deploy with Docker

```bash
docker build -t estonia-e-residency-compliance-automator .
docker run -p 8000:8000 estonia-e-residency-compliance-automator
```
