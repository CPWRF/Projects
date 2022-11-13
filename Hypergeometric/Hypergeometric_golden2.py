# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3.8.10 ('workspace')
#     language: python
#     name: python3
# ---

from scipy.stats import hypergeom
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.io import templates

M = int(input ("Enter Lot size (>=2):"))
# Hypergeom & Sampling plan

# +
#M : Total number of objects, N : N drawn without replacement, n : Total number of Type I objects
#Sampling plan
if 2 <= M <= 170:
    sample_size = [5,12,32,80,170]
elif 171 <= M <= 288:
    sample_size = [6,12,32,80,192,288]
elif 289 <= M <= 544:
    sample_size = [8,16,32,80,192,512]
elif 545 <= M <= 960:
    sample_size = [10,20,40,80,192,512,960]
elif 961 <= M <= 1632:
    sample_size = [12,24,48,96,192,512,1280]
elif 1633 <= M <= 3072:
    sample_size = [12,32,64,128,256,512,1280]
elif 3073 <= M <= 5440:
    sample_size = [12,32,80,160,320,640,1280]
elif 5441 <= M <= 9126:
    sample_size = [12,32,80,192,384,768,1536]
elif 9217 <= M <= 17408:
    sample_size = [12,32,80,192,512,1024,2048]
elif 17409 <= M <= 30720:
    sample_size = [12,32,80,192,512,1280,2560]
else:
    sample_size = [12,32,80,192,512,1280,3072]

result = [(M, N, n, hypergeom(M, n, N).pmf(0)) for N in sample_size for n in range(int(M/10))]
df = pd.DataFrame(result, columns=['Total', 'N_drawn', 'NG_unit', 'Prob_Accept'])
df.Prob_Accept = (df.Prob_Accept * 100).round(2)
df['Lot_Defective'] = 100*(df.NG_unit / df.Total).round(4)


# -

# AOQ function

def AOQ(Total, N_drawn, NG_unit, Prob_Accept):
    return (Prob_Accept * (NG_unit/Total) * (Total-N_drawn))/Total
#df['AOQ'] = vectorize(AOQ)(df.Total, df.N_drawn, df.NG_unit, df.Prob_Accept).round(2)
df['AOQ'] = df[['Total','N_drawn','NG_unit','Prob_Accept']].apply(lambda df: AOQ(df.Total, df.N_drawn, df.NG_unit, df.Prob_Accept), axis=1).round(2)

#df.to_excel('AOQ.xlsx', index=False)
# Set plotly theme

templates.default = "plotly_dark"

# OC curve

fig = px.line(df, x='Lot_Defective', y='Prob_Accept', color='N_drawn',height=600
               ,title=f"Operating Characteristic (OC) curve, population(M)={M}"
               ,labels={
                   'Lot_Defective':'Lot_Defective(%)',
                   'Prob_Accept':'Prob_Accept(%)',
                   'N_drawn':'N_drawn(#)'})
fig.add_hline(y=5, line_dash="dash"
           ,annotation_text="5%"
           ,annotation_position="top left"
           ,annotation_font_size=15)
fig.show()

# # AOQ curve

fig2 = px.line(df, x='Lot_Defective', y='AOQ', color='N_drawn',height=600
               ,title=f"Average Outgoing Quality (AOQ) curve, population(M)={M}"
               ,labels={
                   'Lot_Defective':'Lot_Defective(%)',
                   'AOQ':'AOQ(%Defective)',
                   'N_drawn':'N_drawn(#)'})
fig2.show()
