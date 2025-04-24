# 🔐 Sensitive Data Detection & Anonymization Platform

> Automatically detect and anonymize sensitive data using AI to ensure GDPR compliance.

## 🧠 Project Description

This web application is designed to identify and protect sensitive data using Artificial Intelligence. The tech stack includes:

- 🌐 **Backend**: Django
- 🎨 **Frontend**: React.js
- 🧠 **AI & NLP**: [Presidio](https://github.com/microsoft/presidio) — for analyzing and anonymizing sensitive information
- 🗂️ **Data Classification**: Apache Atlas
- 🔐 **Access Control**: Apache Ranger

The system integrates intelligent detection mechanisms with secure access and structured data classification to facilitate GDPR compliance in data-heavy applications.

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/khadijatarhri/PFA.git

## 🛠️ Set up your virtual environment

```bash
Navigate into the project directory:

cd PFA

Activate the virtual environment:

Linux / macOS:
source env/bin/activate

Windows (CMD):
env\Scripts\activate.bat

Windows (PowerShell):
env\Scripts\Activate.ps1
🔧 Run the backend server
bash
Copier
Modifier
cd backend
python manage.py runserver
🎨 Run the frontend app
bash
Copier
Modifier
cd ../frontend
npm install
npm start
📁 Project Structure
plaintext
Copier
Modifier
PFA/
├── backend/     # Django backend
├── frontend/    # React frontend
├── env/         # Virtual environment
└── README.md
🙌 Contributors
Khadija TARHRI — Software Engineering Student, ENSIAS
