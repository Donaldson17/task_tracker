# Task Tracker

A simple and elegant task management web application built with Flask.

## Features

- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Clean, modern UI with responsive design
- SQLite database for data persistence

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```

2. Open your browser and go to `http://localhost:5000`

3. Start adding and managing your tasks!

## Project Structure

```
task_tracker/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # Application routes
│   ├── models.py            # Database models
│   ├── forms.py             # WTF forms
│   └── templates/
│       └── index.html       # Main template
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

## Technologies Used

- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **WTForms** - Form handling
- **SQLite** - Database
- **HTML/CSS** - Frontend