# 🇪🇪 Estonia e-Residency Compliance Automator

> **Turn manual e-Residency compliance workflows into automated, intelligent pipelines.**

Automate Estonia's e-Residency application and compliance processes with a 4-agent AI pipeline that parses documents, flags risks, tracks status, and generates reports — saving legal teams weeks of manual effort.

---

## 🔍 The Problem

Legal teams, e-Residency applicants, and compliance consultancies face significant manual overhead:

- **Document overload**: Processing passports, business registration forms, bank statements, and supporting documents by hand.
- **Compliance gaps**: Missing requirements or risky clauses in application packages.
- **Status uncertainty**: No single source of truth for application progress and deadlines.
- **Reporting burden**: Manually compiling compliance summaries for stakeholders.

---

## ⚡ The Solution: 4-Agent Compliance Pipeline

This repository deploys four specialized AI agents that work together to automate the entire e-Residency compliance workflow:

### 1. Document Parser 📄

> *Extracts structured data from e-Residency application documents.*

- Parses passports, business registration forms, bank statements, and supporting documents PDF
- Extracts key fields: applicant name, nationality, business structure, shareholders, and financial details
- Converts unstructured documents into structured JSON for downstream processing

===

### 2. Risk Checker 🛡️

> *Flags compliance risks and missing requirements.*

- Cross-references extracted data against Estonia e-Residency eligibility rules
- Flags high-risk nationalities, personas of interest, and suspicious business structures
- Identifies missing documents and inconsistent information across the application package
- Outputs a risk score and prioritized list of required actions

===

### 3. Status Tracker 📊

> *Monitors application status and deadlines.*

- Tracks application progress across all stages: submitted | under review | additional info requested | approved | declined
- Monitors deadlines for document renewals, response windows, and compliance check-ins
- Sends alerts when status changes or deadlines approach
- Provides a unified dashboard of all active applications

===

### 4. Report Generator 📑

> *Creates compliance reports and summaries.*

- Generates executive-summary reports for stakeholders
- Creates detailed compliance reports for audit purposes
- Exports in PDF, Markdown, and JSON formats
- Includes audit trails and regulatory attestations

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    e-Residency Compliance Automator              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   Document   │───▶│    Risk      │───▶│   Status     │       │
│  │   Parser     │    │   Checker    │    │   Tracker    │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         │                   │                   │                │
│         ▼                   ▼                   ▼                │
│  ┌─────────────────────────────────────────────────────┐        │
│  │              Report Generator                        │        │
│  │   (PDF / Markdown / JSON compliance reports)        │        │
│  └─────────────────────────────────────────────────────┘        │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  Storage: PostgreSQL │ Queue: Redis │ API: FastAPI              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Language** | Python 3.11+ |
| **Framework** | FastAPI |
| **Agent Framework** | LangGraph |
| **LLM** | OpenAI GPT-4 / Claude |
| **Document Processing** | PyPDF2, pdfplumber, Tesseract OCR |
| **Database** | PostgreSQL |
| **Task Queue** | Redis + Celery |
| **Testing** | pytest |
| **CI/CD** | GitHub Actions |
| **Containerization** | Docker |

---

## Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Docker (optional)

### Clone & Setup

```bash
git clone https://github.com/phanindraintelligenzit-afk/estonia-e-residency-compliance-automator.git
cd estonia-e-residency-compliance-automator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Configure environment
cp .env.example .env
# Edit .env with your database, Redis, and API key settings

# Run migrations
alembic upgrade head
```

### Docker (Alternative)

```bash
docker compose up -d
```

---

## Quick Start

### 1. Start the API Server

```bash
uvicorn app.main:app --reload --port 8000
```

### 2. Submit a Document for Parsing

```bash
curl -X POST http://localhost:8000/api/v1/documents/parse \
  -H "Content-Type: multipart/form-data" \
  -F "file=@application_package.pdf"
```

### 3. Check Compliance Risk

```bash
curl -X POST http://localhost:8000/api/v1/risk/check \
  -H "Content-Type: application/json" \
  -d '{"application_id": "app_123"}'
```

### 4. Generate a Compliance Report

```bash
curl -X POST http://localhost:8000/api/v1/reports/generate \
  -H "Content-Type: application/json" \
  -d '{"application_id": "app_123", "format": "pdf"}'
```

### 5. Run Tests

```bash
pytest tests/ -v
```

---

## API Endpoints

### Documents

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/documents/parse` | Upload and parse an e-Residency document |
| `GET` | `/api/v1/documents/{id}` | Retrieve parsed document data |
| `GET` | `/api/v1/documents/{id}/status` | Check document processing status |

### Risk Assessment

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/risk/check` | Run compliance risk check on an application |
| `GET` | `/api/v1/risk/{application_id}` | Get risk score and flagged items |
| `GET` | `/api/v1/risk/{application_id}/recommendations` | Get remediation recommendations |

### Status Tracking

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/status/{application_id}` | Get current application status |
| `GET` | `/api/v1/status/dashboard` | Get dashboard of all applications |
| `POST` | `/api/v1/status/{application_id}/update` | Update application status |
| `GET` | `/api/v1/status/deadlines` | Get upcoming deadlines |

### Reports

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/reports/generate` | Generate a compliance report |
| `GET` | `/api/v1/reports/{id}` | Download a generated report |
| `GET` | `/api/v1/reports/{id}/summary` | Get report summary |

### Health

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Service health check |
| `GET` | `/api/v1/agents/status` | Check all agent statuses |

---

## Use Cases

### 🏛️ Legal Teams
Automate the review of e-Residency application packages. Reduce document review time by 80% and ensure no compliance requirement is missed. Generate audit-ready reports for regulatory submissions.

### 🌍 e-Residency Applicants
Get real-time visibility into your application status. Receive proactive alerts about missing documents or upcoming deadlines. Understand compliance risks before submission.

### 🏢 Compliance Consultancies
Manage multiple client applications from a single dashboard. Automate repetitive compliance checks across jurisdictions. Scale your practice without proportionally scaling headcount.

---

## Pricing

| Tier | Cost | Includes |
|---|---|---|
| **Open Source** | **Free** | Clone, test, and deploy yourself. Full source code under MIT license. |
| **Done-for-You Setup** | **$2,000 – $4,000** | We deploy, configure, and customize the pipeline for your organization. Includes agent tuning, integrations, and training. |

> 💡 **Start free.** The repo is fully open-source. Upgrade to Done-for-You setup when you need hands-on deployment support.

---

## Roadmap

- [x] Document Parser agent (PDF extraction, OCR)
- [x] Risk Checker agent (eligibility rules engine)
- [x] Status Tracker agent (application lifecycle)
- [x] Report Generator agent (PDF/MD/JSON export)
- [ ] Multi-language document support (Estonian, Russian)
- [ ] Integration with Estonian Business Register API
- [ ] Webhook notifications (Slack, email, Teams)
- [ ] Bulk application processing
- [ ] Custom compliance rule builder
- [ ] SOC 2 compliance reporting module

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

Built by [AIdentify](https://github.com/phanindraintelligenzit-afk/AIdentify) — AI Automation Marketplace.
