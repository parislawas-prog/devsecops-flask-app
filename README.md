# devsecops-flask-app

A small Flask web app that serves a hello world page and a `/weather` route. The weather route calls the free [Open-Meteo](https://open-meteo.com/) API and displays the current temperature and wind speed for a given location. This is the base project for my DevSecOps portfolio.

## Features

- `/` returns a "Hello, world!" message.
- `/weather` returns the current weather for latitude and longitude values you pass in. Defaults to New York if none are given.

## Requirements

- Python 3.10 or newer
- Git

## Setup

Clone the repo and create a virtual environment:

```bash
git clone https://github.com/parislawas-prog/devsecops-flask-app.git
cd devsecops-flask-app
python -m venv .venv
```

Activate the environment:

- Mac/Linux: `source .venv/bin/activate`
- Windows (Git Bash): `source .venv/Scripts/activate`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

```bash
python app.py
```

Then open:

- `http://127.0.0.1:5000/` for the hello world page
- `http://127.0.0.1:5000/weather?lat=51.5&lon=-0.12` for the weather (replace the coordinates with your own)

## Project structure

```
app.py              # Flask routes
requirements.txt    # Python dependencies
.gitignore          # Files Git should ignore (e.g., .venv/)
```

## Roadmap

This repo is built up over time as part of a DevSecOps learning plan. Upcoming work includes containerizing the app with Docker, adding a CI/CD pipeline with GitHub Actions, and deploying to AWS with Terraform.