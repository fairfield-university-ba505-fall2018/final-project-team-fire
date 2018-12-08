import pandas as pd

def data_import(file):
    data= pd.read_csv(file, header=0, parse_dates=[2,8,9,10,11], infer_datetime_format=True)
    data.drop(columns=['Incident Status','Address on Wildland','Mutual Aid Flag','Mutual Aid Flag Description','Inc Mutual Aid','HazMat Released Code','HazMat Released Code Description'], inplace=True)
    return data