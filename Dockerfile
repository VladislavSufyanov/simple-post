FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --dev
COPY . ./
EXPOSE 8000