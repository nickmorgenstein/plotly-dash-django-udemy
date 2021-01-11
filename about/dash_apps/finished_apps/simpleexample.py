import dash_core_components as dcc
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)
"""
app.layout = html.Div([
    #html.H1('Campaign Progress'),

    dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                },
                'font': {
                }
            }
            )
])

app.layout = html.Div([
    html.H1('Insert Name Here'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
               Output('example-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
              
"""

import pandas as pd

df = pd.read_csv('/Users/nickmorgenstein/Desktop/rando code/CouloirAnalysis/plotly-dash-django-udemy/about/dash_apps/finished_apps/Cleanest with Dates.csv', low_memory=False)

def returnSum(parameter, df):
    """
    :param parameter: list where every odd value is string of column name and even number
    is corresponding value to search for. Ex. ['Ethnicity White', 1]. Length may vary.
    :return: Sum of all columns given the parameter
    """
    column = parameter[0]
    value = parameter[1]

    if len(parameter) == 2:

        return len(df[df[column] == value])
    else:

        newdf = df[df[column] == value]
        del parameter[0:2]
        return returnSum(parameter, newdf)


total_ids = returnSum(['Vote_for_Vilaska Yes', 1], df)
total_ppl = int(len(df))
total_attempted = (total_ppl - int(returnSum(['Vote_for_Vilaska Null', 1], df)))
days_elapsed = 85

"""app.layout = html.Div([
    html.H1('Insert Name Here'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [total_ids, 0, 0], 'type': 'bar', 'name': 'Total IDs'},
                {'x': [0, total_attempted, 0], 'type': 'bar', 'name': 'Total Population'},
                {'x': [0, 0, total_attempted], 'type': 'bar', 'name': 'Total Attempted'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
app.layout = html.Div([
    #html.H1('Campaign Progress'),
    dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': ['Total Population'], 'y': [total_ppl], 'type': 'bar', 'name': 'Total Population'},
                    {'x': ["Total Attempted"], 'y': [total_attempted], 'type': 'bar', 'name': 'Total Attempted'},
                    {'x': ["Total Ids"], 'y': [total_ids], 'type': 'bar', 'name': "Total Id's"},
                ],
                'layout': {
                    'title': 'Your Campaign Overview'
                },
                'font': {
                }
            }
            )
])
"""

"""
fig = go.Figure(data=[go.Bar(
    x=['Total Population', 'Total Attempted', 'Total IDs'],
    y=[total_ppl, total_attempted, total_ids],
)], output=)
#fig.update_layout(title_text='Campaign Overview')

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig, id='example-graph')
])
"""
colors = ['lightsalmon', 'lightblue', 'lightgreen']
y=[total_ppl, total_attempted, total_ids]

fig = go.Figure(data=[go.Bar(
    x=['Total Population', 'Total Attempted', 'Total IDs'],
    y=[total_ppl, total_attempted, total_ids],
    text=y,
    textposition='auto',
    marker_color=colors
)])
text_A = ('Campaign Overview: ' + str(total_attempted) + ' voters out of '
                  + str(total_ppl) + ' voters contacted. ' + str(total_ids) + " IDs. Keep up the hard work!")
percent1 = (total_attempted / total_ppl) * 100
percent2 = (total_ids / total_attempted) * 100
text_B = ('Campaign Overview: ' + str(round(percent1, 2)) + '% of voters attempted, '
          + str(round(percent2, 2)) + '% of attemped voters resulted in IDs.'
          )

fig.update_layout(title_text=text_B)

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])

@app.callback(Output('graph', 'figure'))




def display_value(value):


    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i*i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}


