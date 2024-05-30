#!/bin/bash
export PYTHONUNBUFFERED=true
export FLASK_APP=app.py
export FLASK_ENV=production

# gunicorn --bind 0.0.0.0:$PORT app:app
