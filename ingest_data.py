#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import pandas as pd
import pyarrow.dataset as ds
import sqlalchemy
import psycopg2

from sqlalchemy import create_engine, text
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    taxi_table_name = params.taxi_table_name
    zones_table_name = params.zones_table_name
    taxi_csv_name = params.taxi_csv_name
    zones_csv_name = params.zones_csv_name

    # csv_name = "C:\Users\BLESSING\Desktop\Data_Engineering\Data-Engineering\yellow_tripdata_2025-01.parquet"

    # os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    #    reading the parquet file using pandas
    taxi_data = pd.read_parquet(taxi_csv_name, engine='fastparquet')
    taxi_zones = pd.read_csv(zones_csv_name)


    taxi_df = ds.dataset(taxi_csv_name, format="parquet")

    # to add the column names to the local database 
    taxi_data.head(n=0).to_sql(name = taxi_table_name, con = engine, if_exists = "replace")
    taxi_zones.head(0).to_sql(name = zones_table_name, con = engine, if_exists = "replace")
    
    taxi_zones.to_sql(name = zones_table_name, con = engine, if_exists = "append")

    # to add other data to the local database

    for chunk in taxi_df.to_batches(batch_size=100000):
        df_chunk = chunk.to_pandas()
        # Process df_chunk
        t_start = time()

        df_chunk.to_sql(name = taxi_table_name, con = engine, if_exists = "append")
        
        t_end = time()
        
        print("inserted another chunk..., took %.3f seconds"% (t_end - t_start))
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Ingest CSV data to Postgress")


    parser.add_argument('--user', help = "username for postgress")
    parser.add_argument('--password', help = "password for postgress")
    parser.add_argument('--host', help = "host for postgress")
    parser.add_argument('--port', help = "port for postgress")
    parser.add_argument('--db', help = "database for postgress")
    parser.add_argument('--taxi_table_name', help = "name of the table where we will write the results of yellow taxi to")
    parser.add_argument('--zones_table_name', help = "name of the table where we will write the results of the zone table to")
    parser.add_argument('--taxi_csv_name', help = "csv_name of the taxi csv file")
    parser.add_argument('--zones_csv_name', help = "csv_name of the zones csv file")

    args = parser.parse_args()

    main(args)


