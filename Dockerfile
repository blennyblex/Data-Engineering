FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 pyarrow fastparquet

WORKDIR /app
COPY ingest_data.py ingest_data.py

# ENTRYPOINT [ "bash" ]

ENTRYPOINT [ "python", "ingest_data.py" ]