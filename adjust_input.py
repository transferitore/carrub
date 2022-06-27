##
from datetime import datetime
from asyncore import read
from pydoc import describe
from this import d
from bs4 import BeautifulSoup  # html parser
import pandas as pd
import math
from pandasql import sqldf
from itertools import repeat
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import altair as alt
import numpy as np
from vega_datasets import data
import plotly.express as px
import plotly.io as pio
import dtale

pio.templates.default = "plotly_white"
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pysqldf = lambda q: sqldf(q, globals())
import os
##

from datetime import datetime

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("input") if isfile(join("input", f))]

try:
    onlyfiles.remove('.DS_Store')
except ValueError:
    pass

for path in onlyfiles:


    inpt=pd.read_csv('input/'+path)

    place=inpt['Address'][0].split(" ")[-1]
    
    name=inpt['Address'][0].split(" ")[-1]+'_'+inpt['Listing Type'][0].title()+"_New Properties.xlsx"

    inpt=inpt[["Asking Price", "Bedrooms", "Property Type", "Address", "Postcode", "Total Area (Sqft)", "Agent", "Phone Number", "Added Date", "Portal Links"]]


    inpt['Airbnb Link']="https://www.airbnb.co.uk/s/"+inpt['Postcode'].apply(lambda x:x.replace(' ','-'))+'-'+place+'/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&adults="'+ inpt['Bedrooms'].apply(lambda x: str(x*2))
    inpt['Airbnb Link'][0]

    import os

    matching_files=[]
    for root, dirs, files in os.walk(os.path.abspath("input")):
        for file in files:
            if place in file:
                matching_files.append(os.path.join(root, file))

    matching_files=sorted(matching_files)[::-1]
    
    try:
        comp_inpt=pd.read_excel(matching_files[0])
        final=inpt[inpt['Portal Links'].isin(comp_inpt['Portal Links'])==False]
    except IndexError:
        print('New entry')
        final=inpt

    tdy=datetime.today().strftime('%Y%m%d')
    out_directory=f'input/{tdy}'


    if os.path.exists(out_directory) == False:
                    try:
                        os.mkdir(out_directory)
                    except OSError:
                        print("Creation of the directory %s failed" % out_directory)
                    else:
                        print("Successfully created the directory %s " % out_directory)
    final.to_excel(out_directory+'/'+name)
    os.remove('input/'+path)



##
