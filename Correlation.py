import csv
import numpy as np
import plotly.express as px
def getdata (datapath):
    icecreamsales=[]
    TemperatureSales=[]
    with open(datapath) as  csv_file:
        csvreader=csv.DictReader(csv_file)
        for row in csvreader:
            icecreamsales.append(float(row["icecreamsales"]))
            TemperatureSales.append(float(row["Temperature"]))
    return {"x":TemperatureSales,"y":icecreamsales}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation",correlation[0,1])
    
def setup():
    datapath='data.csv'
    datasource=getdata(datapath)
    findcorrelation(datasource)

setup()


    
