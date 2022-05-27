import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from urllib.request import urlopen
import json

init_notebook_mode(connected=True) 

import pandas as pd

import plotly.express as px

df = pd.read_csv("mps.csv")
df. rename(columns = {'Party':'Party', 'Constituency':'PCON20NM'}, inplace = True)

with urlopen('https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Westminster_Parliamentary_Constituencies_December_2020_UK_BUC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson') as response:
    uk_constituencies=json.load(response)


fig = px.choropleth_mapbox(df, geojson=uk_constituencies, locations='PCON20NM', featureidkey="properties.PCON20NM", color='Party',range_color=(0,12), mapbox_style="carto-positron", zoom=5, center= {"lat": 55, "lon": 0}, opacity=0.5, labels={'Party':'Party'}, color_discrete_map={'Labour':'rgb(220,36,31)', 'Conservative':'rgb(0,135,220)','Scottish National Party':'rgb(255,255,0)', 'Liberal Democrat':'rgb(253,187,48)','Green':'#6AB023','Sinn Féin':'#326760','DUP':'#D46A4C','Independant':'#dddddd', 'Labour/Co-operative':'rgb(220,36,31)','Social Democratic and Labour Party':'#2AA82C', 'Alliance':'#F6CB2F', 'Alba':'#005EB8', 'Speaker':'white','Plaid Cymru':'#005B54'}
)

fig.update_geos(fitbounds="locations", visible=False)
