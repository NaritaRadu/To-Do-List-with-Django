FROM python:3.14-slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY src /src

WORKDIR /src

ENV DJANGO_DEBUG_FALSE=1

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]