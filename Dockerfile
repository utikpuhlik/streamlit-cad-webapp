FROM python:3.11-slim

WORKDIR /opt

#COPY pyproject.toml ./
COPY poetry.lock ./
COPY README.md ./
COPY streamlit_cad_webapp/ ./streamlit_cad_webapp

# Poetry
ENV PATH="${PATH}:/root/.poetry/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN : \
&& pip install poetry \
&& poetry install --no-interaction --no-ansi \
&& apt-get update && apt-get install -y \
    build-essential \
    curl \
&& : \

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["python", "-m", "streamlit", "run", "streamlit_cad_webapp/__main__.py"]
