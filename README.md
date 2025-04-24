# Sensitive Data Detection & Anonymization Platform

> Automatically detect and anonymize sensitive data using AI to ensure GDPR compliance.

## Project Description

This web application is designed to identify and protect sensitive data using Artificial Intelligence. The tech stack includes:

-  **Backend**: Django
-  **Frontend**: React.js
-  **AI & NLP**: [Presidio](https://github.com/microsoft/presidio) — for analyzing and anonymizing sensitive information
-  **Data Classification**: Apache Atlas
-  **Access Control**: Apache Ranger

The system integrates intelligent detection mechanisms with secure access and structured data classification to facilitate GDPR compliance in data-heavy applications.

---

##  Getting Started

Follow these steps to run the project locally:

### Clone the repository

```bash
git clone https://github.com/khadijatarhri/PFA.git
```
##  Set up your virtual environment


## Navigate into the project directory:
```bash
cd PFA
```
## Activate the virtual environment:
Linux / macOS:
```bash
source env/bin/activate
```
Windows (CMD):
```bash
env\Scripts\activate.bat
```

##Run the backend server
```bash
cd backend
python manage.py runserver
```
## Run the frontend app
```bash
cd ../frontend
npm install
npm start
```
## Contributors
-  **Khadija TARHRI** — Software Engineering Student, ENSIAS
-  **Nisrine Bakhouch** — Software Engineering Student, ENSIAS
-  **MAssine Sekkaki** — Software Engineering Student, ENSIAS
-  **Dao Sidiki** — Software Engineering Student, ENSIAS

