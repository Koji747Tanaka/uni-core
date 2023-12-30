#!/bin/sh

if [ "$PIP_INSTALL" == "true" ]; then
    echo Running pip install
    pip install --no-cache-dir -r requirements.txt
fi

echo "Running Django Server ..."
python manage.py runserver 0.0.0.0:8000