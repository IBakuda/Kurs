import pandas as pd
import plotly.graph_objs as go

def revenueCapitalization():
    data = pd.read_csv("input/NVIDIA-US GAAP.csv")
    data2 = pd.read_csv("input/AMD-US GAAP.csv")

    markercolor = data['d-mpg']
    markercolor2 = data2['d-mpg']

    # Создаем график сравнения активов и операционной прибыли компаний
    fig = go.Figure(data=[
        go.Scatter3d(x=data['Квартал'],
                     y=data['Активы млн $'],
                     z=data['Операционная прибыль млн $'],
                     marker=dict(
                         opacity=1,
                         reversescale=True,
                         color=markercolor,
                         colorscale='aggrnyl',
                     ),
                     name="NVIDIA",
                     ),
        go.Scatter3d(x=data2['Квартал'],
                     y=data2['Активы млн $'],
                     z=data2['Операционная прибыль млн $'],
                     marker=dict(
                         opacity=1,
                         reversescale=True,
                         color=markercolor2,
                         colorscale=[[0, 'rgb(153, 0, 0)'], [1.0, 'rgb(255, 255, 153)']],
                     ),
                     name="AMD"
                     )
    ])

    # Make Plot.ly Layout
    fig.update_layout(scene=dict(
        xaxis_title='Квартал',
        yaxis_title='Активы млн $',
        zaxis_title='Операционная прибыль млн $')
    )
    fig.write_html(file="output/graf2.html",
                   auto_open=True)