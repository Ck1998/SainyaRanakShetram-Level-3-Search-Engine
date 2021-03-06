FROM python:3.7-slim-buster
WORKDIR /opt/front-end
RUN mkdir -p /opt/front-end

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libffi-dev \
        libssl-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/front-end/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /opt/front-end

EXPOSE 8000
RUN python /opt/front-end/manage.py runserver