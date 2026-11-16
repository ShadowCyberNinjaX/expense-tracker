# Student Expense Tracker

### Track Your Expenses. Manage Your Budget. Build Better Saving Habits.

\<p align="center">   \<img src="[https://img.shields.io/badge/Python-3.x-blue?logo=python](https://img.shields.io/badge/Python-3.x-blue?logo=python)" />   \<img src="[https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)" />   \<img src="[https://img.shields.io/badge/HTML-Frontend-orange?logo=html5](https://img.shields.io/badge/HTML-Frontend-orange?logo=html5)" />   \<img src="[https://img.shields.io/badge/CSS-Styling-blue?logo=css3](https://img.shields.io/badge/CSS-Styling-blue?logo=css3)" />   \<img src="[https://img.shields.io/badge/JavaScript-Interactive-yellow?logo=javascript](https://img.shields.io/badge/JavaScript-Interactive-yellow?logo=javascript)" /> \</p>

## Overview

Student Expense Tracker is a Flask-based web application designed to help students manage their personal finances and monitor their spending habits.

The application provides a simple way to record daily expenses, track monthly expenditure, monitor budgets and estimate potential savings.

It aims to make personal financial management easier by organizing expense records and presenting useful summaries of spending patterns.

## Project Objectives

- Simplify personal expense management for students.
- Maintain records of daily expenditures.
- Monitor monthly spending patterns.
- Track budget utilization.
- Estimate potential savings.
- Present financial information in an organized and understandable format.

## Features

### 1. Expense Management

- Add new expense records.
- Delete existing expense records.
- Maintain an organized expense history.

### 2. Monthly Reports

- View monthly expenditure summaries.
- Monitor spending patterns over time.
- Understand how expenses change across months.

### 3. Budget Tracking

- Monitor expenditure against a defined budget.
- Keep track of remaining budget.
- Understand monthly budget utilization.

### 4. Savings Estimation

- Estimate potential savings based on income, budget and expenditure.
- Observe the relationship between spending and available savings.

### 5. Expense Visualization

- Present financial information through visual summaries.
- Use charts to make spending patterns easier to understand.

## Application Workflow

The following flowchart illustrates the overall working process of the application.

```mermaid
flowchart TD
    A(["User"]) --> B["Open Expense Tracker"]
    B --> C["Flask Application"]
    C --> D["Dashboard"]

    D --> E{"Select Operation"}

    E --> F["Add Expense"]
    E --> G["Delete Expense"]
    E --> H["View Monthly Reports"]
    E --> I["Track Budget"]
    E --> J["Estimate Savings"]

    F --> K["Validate Expense Details"]
    K --> L["Update Expense Records"]

    G --> L

    L --> M["Update Financial Summary"]
    H --> M
    I --> M
    J --> M

    M --> N["Generate Visual Summaries"]
    N --> O["Display Updated Dashboard"]
    O --> P(["User Views Results"])

    P --> D

    classDef user fill:#172554,stroke:#60A5FA,color:#FFFFFF,stroke-width:2px
    classDef frontend fill:#E0F2FE,stroke:#0284C7,color:#0C4A6E,stroke-width:1.5px
    classDef operation fill:#DCFCE7,stroke:#16A34A,color:#14532D,stroke-width:1.5px
    classDef processing fill:#F3E8FF,stroke:#9333EA,color:#581C87,stroke-width:1.5px
    classDef output fill:#FFEDD5,stroke:#EA580C,color:#7C2D12,stroke-width:1.5px

    class A,P user
    class B,C,D frontend
    class E,F,G,H,I,J operation
    class K,L,M processing
    class N,O output
```

## Technology Stack

| Category                  | Technology              |
| ------------------------- | ----------------------- |
| Programming Language      | Python                  |
| Backend Framework         | Flask                   |
| Frontend                  | HTML                    |
| Styling                   | CSS                     |
| Client-side Functionality | JavaScript              |
| Data Visualization        | Chart.js                |
| Templating Engine         | Jinja2                  |
| Data File Included        | Excel (`expenses.xlsx`) |

## Repository Structure

```text
expense-tracker/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── HTML templates
│
├── app.py
├── expenses.xlsx
├── .gitignore
├── README.md
│
└── Student_Expense_Tracker_Documentation.pdf
```

*The directory names shown inside `static/` and `templates/` are illustrative. Adjust them to match the actual files in your repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ShadowCyberNinjaX/expense-tracker.git

cd expense-tracker
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install Flask and the additional packages required by the application:

```bash
pip install flask
```

If the application uses additional Python libraries, install those as well.

### 4. Run the Application

```bash
python app.py
```

Open the application in your browser at:

```text
http://127.0.0.1:5000/
```

## Screenshots

Add screenshots of the application here to demonstrate its interface and functionality.

Suggested screenshots:

| Screenshot         | Description                              |
| ------------------ | ---------------------------------------- |
| Dashboard          | Main application interface               |
| Expense Management | Adding and deleting expenses             |
| Monthly Reports    | Monthly expenditure summaries            |
| Budget Tracking    | Budget utilization and remaining balance |
| Savings Estimation | Estimated savings overview               |

Example Markdown for adding screenshots:

```markdown
![Dashboard](screenshots/dashboard.png)

![Monthly Reports](screenshots/monthly-reports.png)
```

## Future Improvements

- User authentication and individual expense profiles.
- Category-based expense filtering.
- CSV and Excel report downloads.
- More detailed monthly and yearly analytics.
- Improved budget alerts and spending notifications.
- Enhanced dashboard visualizations.
- Responsive interface for mobile devices.

## Learning Outcomes

This project provides practical experience in:

- Developing web applications using Flask.
- Connecting frontend interfaces with backend Python logic.
- Working with HTML, CSS and JavaScript.
- Using Jinja2 for dynamic page rendering.
- Managing and organizing financial records.
- Presenting data through reports and visualizations.

## Author

**Priyasha Haldar**

GitHub: [ShadowCyberNinjaX](https://github.com/ShadowCyberNinjaX)

---

**Project:** Student Expense Tracker
**Category:** Web Development / Personal Finance Management
