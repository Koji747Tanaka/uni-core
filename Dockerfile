FROM python:3.10

RUN python -m pip install Django

# Allow typing unicode in container bash
ENV LANG=C.UTF-8