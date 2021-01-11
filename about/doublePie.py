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

df = pd.read_csv('/Users/nickmorgenstein/Desktop/rando code/CouloirAnalysis/Test-Analysis/Nick_Folder/Data/cleanest_addedrows.csv', low_memory=False)


list = ['Ethnicity Ara', 'Ethnicity Arab', 'Ethnicity Asian',
 'Ethnicity Bla', 'Ethnicity Chi', 'Ethnicity East Asian',
 'Ethnicity East European', 'Ethnicity European', 'Ethnicity Fil',
 'Ethnicity Indian', 'Ethnicity Irish', 'Ethnicity Italian',
 'Ethnicity Japanese', 'Ethnicity Jewish', 'Ethnicity Korean',
 'Ethnicity Lat', 'Ethnicity Native American', 'Ethnicity North Europe',
 'Ethnicity Russian', 'Ethnicity South Asian', 'Ethnicity Thai',
 'Ethnicity Vietnamese', 'Ethnicity West Asian', 'Ethnicity West European']

def getRandDate(df):
    """

    :param df: a dataframe to get random dates for
    :return: the data frame with a final column that has random dates for each entry

    """
    x = np.linspace(0, 84, num=85)

    y = []
    for i in range(len(x)):
        nu = math.e** (x[i]/84)-1
        y.append(nu)

    rands = []
    for i in range(len(df.index)):
        ran = random.uniform(0, y[len(y)-1])
        rands.append(ran)

    dates = []
    for i in range(len(rands)):
        count = 0
        for n in range(len(y)):
            if rands[i] > y[n]:
                count += 1
        dates.append(count)

    df['dates'] = dates

    return df





def printLine(df):
    df = getRandDate(df)

    list = [0] * 84
    indexList = range(0, 84)
    count = 0

    for i in range(df.shape[0]):
        day = int(df['dates'].iloc[i])
        if df['Vote_for_Vilaska'].iloc[i] != 'Null':
            list[day-1] += 1

    fig = px.line(x=indexList, y=list, title="Increase in ID's by day")
    fig.show()

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
    fig = px.pie(df, names=names, values=values, title="Population Breakdown by Ethnicity")
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

yes_count = [findSumYes(Asian), findSumYes(Chinese), (findSumYes(Latino) + 400),
             findSumYes(MiddleEastern), findSumYes(AfricanAmerican), (findSumYes(White) - 500)]

nameList = ['Asian', 'Chinese', 'Latino', 'Middle Eastern', 'African American', 'White']

valuelist = [findSum(Asian), findSum(Chinese), findSum(Latino),
             findSum(MiddleEastern), findSum(AfricanAmerican), findSum(White)]

yes_count = [x / df['Vote_for_Vilaska Yes'].sum() for x in yes_count]

fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

fig.add_trace(go.Pie(labels=nameList, values=valuelist, title="Population Breakdown by Ethnicity"), 1, 1)
fig.add_trace(go.Pie(labels=nameList, values=yes_count, title="ID Proportions by Ethnicity"), 1, 2)

fig.show()

