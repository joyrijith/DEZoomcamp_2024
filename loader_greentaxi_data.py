import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
   
    """
    urls = ['https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz','https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz','https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz']

   # count=len(url)
    df0=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    dflist=[df0,df1,df2]

    i=0

    for url in urls:
        
                   

        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'congestion_surcharge': float 
        }
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        
        new_df=pd.read_csv(url,sep=",", compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        dflist[i]=new_df
        
        i=i+1

     
    concatenated_table=pd.concat(dflist)
  
    return concatenated_table
    

