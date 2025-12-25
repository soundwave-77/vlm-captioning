FROM python:3.13-slim

ARG VLM_MODEL_REPO
ARG IMAGE_PROCESSOR_FILENAME
ARG VLM_MODEL_FILENAME

ENV VLM_MODEL_REPO=${VLM_MODEL_REPO} \
    IMAGE_PROCESSOR_FILENAME=${IMAGE_PROCESSOR_FILENAME} \
    VLM_MODEL_FILENAME=${VLM_MODEL_FILENAME}

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN hf download ${VLM_MODEL_REPO} ${VLM_MODEL_FILENAME} ${IMAGE_PROCESSOR_FILENAME}

COPY src ./app

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]