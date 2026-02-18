FROM apache/airflow:2.11.0-python3.10

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git libglib2.0-0 \
    libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libharfbuzz-subset0 libre2-dev\
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --no-cache-dir apache-airflow==2.11.0 -r ./requirements.txt
