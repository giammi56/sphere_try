import glob
import math
import numpy as np
import pandas as pd

import plotly.graph_objects as go

name_sphere = r"sphere.csv"
df_sphere = pd.read_csv(name_sphere, names=["x", "y", "z"], header=0)

x_s = df_sphere.iloc[:,0].to_numpy()
y_s = df_sphere.iloc[:,1].to_numpy()
z_s = df_sphere.iloc[:,2].to_numpy()
X_s = x_s.reshape(5,11)
Y_s = y_s.reshape(5,11)
Z_s = z_s.reshape(5,11)

fig1 = go.Figure(data=[go.Surface(z=Z_s, x=X_s, y=Y_s)])
fig1.update_layout(title='test sphere', autosize=False,
                #   width=500, height=500,
                #   margin=dict(l=65, r=50, b=65, t=90))
                  margin=dict(l=0, r=0, b=0, t=0))
fig1.show()

fig2 = go.Figure(data=[go.Scatter3d(x=x_s, y=y_s, z=z_s,
                    mode='markers',
                    marker=dict(
                        size=5,
                        colorscale='Viridis',   # choose a colorscale
                        showscale=True          # to show the legend according to the color
                   )
                )])
fig2.update_layout(title='sphere scattered',margin=dict(l=0, r=0, b=0, t=0))
fig2.show()