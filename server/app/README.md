# FNOL AI Agent

## Overview

This project is a lightweight AI agent that processes First Notice of Loss (FNOL) documents.

The agent performs the following tasks:

- Extracts key information from FNOL PDF/TXT documents
- Identifies missing mandatory fields
- Classifies the claim
- Routes the claim to the appropriate workflow
- Returns the result in the required JSON format

---

## Features

- PDF and TXT document support
- Field extraction using Regular Expressions
- Missing field validation
- Rule-based claim routing
- JSON response as required by the assessment

---

## Routing Rules

| Condition | Route |
|----------|-------|
| Estimated Damage < 25000 | Fast-track |
| Mandatory fields missing | Manual Review |
| Description contains "fraud", "staged", or "inconsistent" | Investigation Flag |
| Claim Type = Injury | Specialist Queue |

---

## Tech Stack

- Python 3
- FastAPI
- PyMuPDF (fitz)
- Regular Expressions (Regex)
- Uvicorn

---

## Project Structure

Project Structure

```
server/
│
├── app/
│   ├── api/
│   │   └── upload.py
│   │
│   ├── parser/
│   │   └── fnol.py
│   │
│   ├── classifier.py
│   ├── extractor.py
│   ├── main.py
│   ├── schemas.py
│   ├── summarizer.py
│   └── validator.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository

```bash
git clone <your-github-repository-url>
```

Go to project folder

```bash
cd fnol-ai-agent
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Upload FNOL Document

```
POST /upload
```

Upload a PDF or TXT FNOL document.

---

## Sample Output

```json
{
  "extractedFields": {
    "policy_number": "POL555888",
    "policyholder_name": "Robert Williams",
    "effective_dates": "01-Jan-2026 to 31-Dec-2026",
    "incident_date": "2026-07-10",
    "incident_time": "02:45 PM",
    "location": "Bengaluru, Karnataka",
    "description": "Minor rear-end collision at a traffic signal causing bumper damage.",
    "claimant": "Robert Williams",
    "third_parties": "Anita Sharma",
    "contact_details": "+91-9876543210",
    "asset_type": "Car - Hyundai Creta 2024",
    "asset_id": "VINHYD123456789",
    "estimated_damage": "18000",
    "claim_type": "Vehicle Damage",
    "attachments": "Photos, Police Report",
    "initial_estimate": "20000"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below ₹25,000."
}
```

---

## Author

Prajwal R