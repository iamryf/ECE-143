import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from bokeh.palettes import brewer


def speed(data_o,name):
    '''
    The function loads the PEMS freeway speed data and plot the average, min and max speed
    :param data_o: DataFrame - the dataset
    :param name: str - the name of the dataset
    '''
    
    assert isinstance(data_o,pd.DataFrame)
    assert isinstance(name,str)
    
    average = []
    min = []
    max = []

    for i in range(24):
        data = data_o[data_o['Time']==(str(i)+':00')]
        average.append(data['Speed'].mean())
        min.append(data['Speed'].min())
        max.append(data['Speed'].max())

    x = range(24)
    plt.title('Daily Speed Analysis on Freeway '+name)
    plt.plot(x, average, color='green', label='average speed')
    plt.plot(x, min, color='blue', label='min speed')
    plt.plot(x, max, color='red', label='max speed')
    plt.legend()
    plt.grid(True)
    plt.xlabel('hour of day')
    plt.ylabel('speed')
    
    
def flow(data_o,name):
    '''
    The function loads the PEMS freeway flow data and plot the average, min and max flow
    :param data_o: DataFrame - the dataset
    :param name: str - the name of the dataset
    '''
    
    assert isinstance(data_o,pd.DataFrame)
    assert isinstance(name,str)
    
    average = []
    min = []
    max = []

    for i in range(24):
        data = data_o[data_o['Time']==(str(i)+':00')]
        average.append(data['Flow'].mean())
        min.append(data['Flow'].min())
        max.append(data['Flow'].max())

    x = range(24)
    plt.title('Daily Flow Analysis on Freeway '+name)
    plt.plot(x, average, color='green', label='average flow')
    plt.plot(x, min, color='blue', label='min flow')
    plt.plot(x, max, color='red', label='max flow')
    plt.legend(fontsize=9)
    plt.grid(True)
    plt.xlabel('hour of day')
    plt.ylabel('flow')

    
def flow_agg(data_o,name,fig,color):
    '''
    The function loads several PEMS freeway flow datasets and plot the average flow
    :param data_o: DataFrame - the dataset
    :param name: str - the name of the dataset
    :param fig: figure - figure to be plotted
    :param color: str - color to be plotted
    '''
    
    assert isinstance(data_o,pd.DataFrame)
    assert isinstance(name,str)
    
    average = []

    for i in range(24):
        data = data_o[data_o['Time']==(str(i)+':00')]
        average.append(data['Flow'].mean())

    x = range(24)
    plt.title('Daily Flow Analysis')
    plt.plot(x, average, label=name, color=color, figure = fig)