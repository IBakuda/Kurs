import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def costComparison():
    data = pd.read_csv("input/NVIDIA-US GAAP.csv")
    data2 = pd.read_csv("input/AMD-US GAAP.csv")
    markercolor = data['d-mpg']
    markercolor2 = data2['d-mpg']
    start, end = 20, 150

    fig = make_subplots(rows=2, cols=2,
                        specs=[[{'type': 'scene'}, {'rowspan': 2}],
                               [{'type': 'scene'}, None]]
                        )

    fig.add_trace(go.Scatter3d(
        x=data['Квартал'][start:end],
        y=data['НИОКР млн $'][start:end],
        z=data['Опер.расходы млн $'][start:end],
        text=data['Валюта отчета'][start:end],
        mode='markers',
        name='NVIDIA НИОКР млн $ / Опер.расходы млн $',
        marker=dict(
            sizemode='diameter',
            sizeref=120,
            size=data['Выручка млн $'][start:end],
            color=markercolor,
            colorscale='aggrnyl',
            line_color='rgb(140, 140, 170)'
        )
    ),
        row=1, col=1
    )
    fig.add_trace(go.Scatter3d(
        x=data2['Квартал'][start:end],
        y=data2['НИОКР млн $'][start:end],
        z=data2['Опер.расходы млн $'][start:end],
        text=data2['Валюта отчета'][start:end],
        mode='markers',
        name='AMD НИОКР млн $ / Опер.расходы млн $',
        marker=dict(
            sizemode='diameter',
            sizeref=120,
            size=data2['Выручка млн $'][start:end],
            color=markercolor2,
            colorscale=[[0, 'rgb(153, 0, 0)'], [1.0, 'rgb(255, 255, 153)']],
            line_color='rgb(140, 140, 170)'
        )
    ), row=1, col=1
    )

    fig.add_trace(go.Scatter3d(
        x=data['Квартал'][start:end],
        y=data['Долг млн $'][start:end],
        z=data['Чистый долг млн $'][start:end],
        text=data['Валюта отчета'][start:end],
        mode='markers',
        name='NVIDIA Долг млн $ / Чистый долг млн $',
        marker=dict(
            sizemode='diameter',
            sizeref=120,
            size=data['Выручка млн $'][start:end],
            color=markercolor,
            colorscale='aggrnyl',
            line_color='rgb(140, 140, 170)'
        )
    ), row=2, col=1
    )
    fig.add_trace(go.Scatter3d(
        x=data2['Квартал'][start:end],
        y=data2['Долг млн $'][start:end],
        z=data2['Чистый долг млн $'][start:end],
        text=data2['Валюта отчета'][start:end],
        mode='markers',
        name='AMD Долг млн $ / Чистый долг млн $',
        marker=dict(
            sizemode='diameter',
            sizeref=120,
            size=data2['Выручка млн $'][start:end],
            color=markercolor2,
            colorscale=[[0, 'rgb(153, 0, 0)'], [1.0, 'rgb(255, 255, 153)']],
            line_color='rgb(140, 140, 170)'
        )
    ), row=2, col=1
    )

    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["НИОКР млн $"], name="NVIDIA НИОКР млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,183,37)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Чистый долг млн $"], name="NVIDIA Чистый долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(129,228,0)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Долг млн $"], name="NVIDIA Долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(49,171,11)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Опер.расходы млн $"], name="NVIDIA Опер.расходы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(101,239,58)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["НИОКР млн $"], name="AMD НИОКР млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,0,60)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Чистый долг млн $"], name="AMD Чистый долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,87,177)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Долг млн $"], name="AMD Долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(155,0,186)'),), row=1, col=2)
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Опер.расходы млн $"], name="AMD Опер.расходы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(213,0,255)'),), row=1, col=2)

    fig.update_layout(scene1=dict(
        xaxis_title='Квартал',
        yaxis_title='НИОКР млн $',
        zaxis_title='Опер.расходы млн $'),
        scene2=dict(
            xaxis_title='Квартал',
            yaxis_title='Долг млн $',
            zaxis_title='Чистый долг млн $'),
    )

    fig.write_html(file="output/graf4.html",
                   auto_open=True)