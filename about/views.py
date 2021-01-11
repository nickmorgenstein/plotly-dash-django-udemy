from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
# Create your views here.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sys
import math
import random
import plotly.graph_objs as go
from plotly.subplots import make_subplots

df = pd.read_csv('/Users/nickmorgenstein/Desktop/rando code/CouloirAnalysis/plotly-dash-django-udemy/home/cleanest_addedrows.csv', low_memory=False)

"""def about(request):
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y = y1
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }"""

def about(request):

    context ={
        'plot1': completePie()
    }

    return render(request, 'about/welcome.html', context)


Asian = ['Ethnicity Asian', 'Ethnicity East Asian',
         'Ethnicity Fil', 'Ethnicity Indian', 'Ethnicity Japanese', 'Ethnicity Korean',
         'Ethnicity Lat', 'Ethnicity South Asian', 'Ethnicity Thai', 'Ethnicity Vietnamese', ]

Chinese = ['Ethnicity Chi']

Latino = ['Ethnicity Lat']

MiddleEastern = ['Ethnicity West Asian', 'Ethnicity Ara', 'Ethnicity Arab']

AfricanAmerican = ['Ethnicity Bla']

White = [
    'Ethnicity East European', 'Ethnicity European', 'Ethnicity Fil', 'Ethnicity Irish', 'Ethnicity Italian',
    'Ethnicity Jewish', 'Ethnicity Native American', 'Ethnicity North Europe',
    'Ethnicity Russian', 'Ethnicity West European']


def findSum(columnList, dataframe=df):
    sum = 0
    for i in range(len(columnList)):
        columnName = columnList[i]
        sum += df[columnName].sum()
    return sum

def printPie(names, values):

    names = pd.Series(names, dtype='object')
    values = pd.Series(values)
    fig = px.pie(df, names=names, values=values, title="Population Breakdown by Ethnicity",  width=800, height=400)
    fig.show()


def findSumYes(columnList, dataframe=df):
    newdf = df[df['Vote_for_Vilaska Yes'] == 1]
    sum = 0

    for i in range(len(columnList)):
        current = df.loc[df[columnList[i]] == 1]
        sum += current['Vote_for_Vilaska Yes'].sum()

    return sum

def findSumLikes(columnList, dataframe=df):
    sum = 0
    columnList.append('Vote_for_Vilaska Yes')
    newdf = df[columnList]

    print(newdf.info())

    return sum

def completePie():

    yes_count = [findSumYes(Asian), findSumYes(Chinese), (findSumYes(Latino) + 400),
                 findSumYes(MiddleEastern), findSumYes(AfricanAmerican), (findSumYes(White) - 500)]

    nameList = ['Asian', 'Chinese', 'Latino', 'Middle Eastern', 'African American', 'White']

    valuelist = [findSum(Asian), findSum(Chinese), findSum(Latino),
                 findSum(MiddleEastern), findSum(AfricanAmerican), findSum(White)]

    yes_count = [x / df['Vote_for_Vilaska Yes'].sum() for x in yes_count]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    fig.add_trace(go.Pie(labels=nameList, values=valuelist, title="Population Breakdown by Ethnicity"), 1, 1, )
    fig.add_trace(go.Pie(labels=nameList, values=yes_count, title="ID Proportions by Ethnicity"), 1, 2)

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)


    return plot_div

