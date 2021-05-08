import numpy as np
import pandas as pd
import plotly.express as px

dataset1=pd.read_csv('./highestprio.csv')
dataset2=pd.read_csv('./lowestprio.csv')
fig1 = px.histogram(dataset1, nbins=50, range_x=[5.3900, 5.5000], template='ggplot2')
fig2 = px.histogram(dataset2, nbins=50, range_x=[5.3900, 5.5000])
fig2.add_trace(fig1.data[0])
fig2.update_layout(barmode='overlay')
fig2.update_traces(opacity=0.60)
print(dataset1.mean())
print(dataset2.mean())
#fig2.show()
