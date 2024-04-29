print('I am at the top')
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
os.environ['GOOGLE_APPLICATION_CREDENTAILS']='/home/src/shining-env-418601-0e03c47b01f6.json'

print('I just declared the env')

bucket_name='mage-zoomcamp-joy_chett'
project_id='shining-env-418601'

table_name='nyc_green_taxi_data'

root_path=f'{bucket_name}/{table_name}'

print('I am here one')

@data_exporter
def export_data(data, *args, **kwargs):
    # table=pa.Table.from_pandas(data)

    # gcs=pa.fs.GcsFileSystem()

    # print('I am here two')
    # print(data)

    # pq.write_to_dataset(
    #     table,
    #     root_path=root_path,
    #     partition_cols=['lpep_pickup_date'],
    #     filesystem=gcs
    # )


    data['lpep_pickup_date']= data['lpep_pickup_datetime'].dt.date

    table =pa.Table.from_pandas(data)

    gcs=pa.fs.GcsFileSystem()
    
    print('I am here two')
    
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs


    )

    



    print('I am here three')
   