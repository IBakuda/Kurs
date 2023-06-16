import pandas as pd
import plotly.graph_objs as go

def comparisonRevenues(): #Первый график
    z1 = data = pd.read_csv("input/NVIDIAv.csv")
    z2 = data2 = pd.read_csv("input/AMDv.csv")
    x = ['1', '2', '3', '4']
    fig = go.Figure(data=[
        go.Surface(x=x,z=z1, colorscale='greens', showscale=False, reversescale=True, name="NVIDIA"), #emrld   greens   Aggrnyl
        go.Surface(x=x,z=z2, colorscale='hot', showscale=False, name="AMD")
    ])

    fig.update_layout(scene=dict(
        xaxis_title='Квартал',
        yaxis_title='Год',
        zaxis_title='Выручка, млн$')
    )

    fig.write_html(file="output/graf1.html",
                   auto_open=True)