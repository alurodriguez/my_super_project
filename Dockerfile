# FROM python:3.8 as requirements-stage
# WORKDIR /tmp
# RUN pip install poetry
# COPY ./pyproject.toml ./poetry.lock* /tmp/
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.8
WORKDIR /app
# COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
# RUN chmod +x run.sh

ENV PYTHONPATH=/app
EXPOSE 8000

# CMD ["./run.sh"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
