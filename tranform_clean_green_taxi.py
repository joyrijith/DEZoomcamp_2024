import pandas as pd
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test




@transformer
def transform(data, *args, **kwargs):
        
 
    df=pd.DataFrame()
    df=data
    zero_passenger=data['passenger_count'].isin([0]).sum()
    zero_trip_distance=data['trip_distance'].isin([0]).sum()
    print('Preprocessing: rows with zero passengers', zero_passenger)
    print('Preprocessing: rows with zero trip_distance', zero_trip_distance)
    filtered=(df.passenger_count!=0) & (df.trip_distance!=0)
    df_filtered=df[filtered]
    df_filtered['lpep_pickup_date']=(df_filtered['lpep_pickup_datetime']).dt.date
    df_filtered.columns=df_filtered.columns.str.lower()   
    
    return df_filtered

    

    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'vendorid' in output.columns ,'VendorId is not present in column names'
    assert output['passenger_count'].all()!=0, 'Passenger count is not greater than 0'
    assert output['trip_distance'].all()!=0, 'Trip distance is not greater than 0'
