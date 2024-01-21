import math
from operator import itruediv
from unicodedata import name
from numpy import arange
import requests
import json


from datetime import datetime, date, timedelta
import pandas as pd
import os 
import numpy as np
from pandas import json_normalize


def GatData(station,date):
    response = requests.post("http://webservice.irimo.ir/sajjadeh/dal/login?username=pishbini_2&password=pishbini@irimo",headers={   
    "Content-Type": "application/json" })
    token= response.json()["claims"]["token"]  
    # print("response token: "+str(token))


    params={"params": [
    {"name": "sdate","value": f"{date}"},   
    {"name": "stid", "value": station}]       
    }

    response1 = requests.post("http://webservice.irimo.ir/sajjadeh/dal/dws/odb_temp",headers={"Content-Type": "application/json","Authorization":token },json=params)
    # print("response json: "+str(response1.json()))        
       
    df2 = json_normalize(response1.json())
    return df2.query("td != 0 or dd != 0 or ff != 0 or t != 0 or u != 0 ")

  
if __name__ == '__main__':
    d=GatData('40745','2023-03-01')   
    d.to_excel('l.xlsx')     
    print(d )