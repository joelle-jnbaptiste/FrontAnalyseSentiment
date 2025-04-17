# Sentiment Analysis Frontend

This is a simple Streamlit application for testing a sentiment analysis API.

## Features

- Send text to a remote API for sentiment prediction
- Display the prediction as positive or negative
- Allow user feedback and send it back to the API

## Setup

1. Clone the repository:

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Notes

- The API URL used in the app must be accessible and running.
- SSL verification is disabled for testing purposes. Do not use `verify=False` in production.
