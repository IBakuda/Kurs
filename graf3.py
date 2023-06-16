import pandas as pd
import plotly.graph_objs as go


def companyComparison():
    data = pd.read_csv("input/NVIDIA-US GAAP.csv")
    data2 = pd.read_csv("input/AMD-US GAAP.csv")

    markercolor = data['d-mpg']

    fig = go.Figure() #создание графика
    #отрисовка показателей NVIDIA
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Капитализация млн $"], name="NVIDIA Капитализация млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(84,255,84)'), )),
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Выручка млн $"], name="NVIDIA Выручка млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,183,37)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Операционная прибыль млн $"], name="NVIDIA Операционная прибыль млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,238,48)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Чистая прибыль млн $"], name="NVIDIA Чистая прибыль млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(129,228,0)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Операционный денежный поток млн $"],name="NVIDIA Операционный денежный поток млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(80,141,0)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Активы млн $"], name="NVIDIA Активы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,127,0)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Чистые активы млн $"], name="NVIDIA Чистые активы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(171,255,0)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Наличность млн $"], name="NVIDIA Наличность млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(85,178,14)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Долг млн $"], name="NVIDIA Долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,255,154)'), )),#######
    fig.add_trace(go.Scatter(x=data["Квартал"], y=data["Опер.расходы млн $"], name="NVIDIA Опер.расходы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(0,172,103)'), )),#######

    #отрисовка показателей AMD
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Капитализация млн $"], name="AMD Капитализация млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,84,84)'), )),
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Выручка млн $"], name="AMD Выручка млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(94,0,0)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Операционная прибыль млн $"], name="AMD Операционная прибыль млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,0,60)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Чистая прибыль млн $"], name="AMD Чистая прибыль млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(239,88,0)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Операционный денежный поток млн $"], name="AMD Операционный денежный поток млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(138,0,45)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Активы млн $"], name="AMD Активы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,87,177)'), )),  #######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Чистые активы млн $"], name="AMD Чистые активы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(255,102,255)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Наличность млн $"], name="AMD Наличность млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(170,67,229)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Долг млн $"], name="AMD Долг млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(155,0,186)'), )),#######
    fig.add_trace(go.Scatter(x=data2["Квартал"], y=data2["Опер.расходы млн $"], name="AMD Опер.расходы млн $",
                             marker=dict(opacity=1, reversescale=True, color='rgb(213,0,255)'), )),#######

    #
    fig.update_layout(scene=dict(
        xaxis_title='Квартал',
        yaxis_title='Активы млн $/Долг млн $'
    )
    )

    fig.write_html(file="output/graf3.html",
                   auto_open=True)