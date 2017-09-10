import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib as mpl

# Make a float from a percentage string
def p2f(x):
    return float(x.strip('%'))/100
# Loop through spines in an axis and set to invisible
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
# Returns a string of X.XXM for a float in the millions.
def str_in_millions(number):
    reduced = number/1000000
    return (str(reduced)+'M')
# Import as pandas dataframe two datasets with different collection frequencies and convert Unemployment Rate
# from percentage string to float.
df1 = pd.read_excel('LAUS_1990-2016.xlsx', index_col=0, thousands=',', converters={'Unemployment Rate':p2f})
df2 = pd.read_excel('LAUS_monthly_1990-2016.xlsx', index_col=0, thousands=',', converters={'Unemployment Rate':p2f})
df3 = pd.read_excel('OED_2011-2016.xlsx', index_col=0)
# Function to plot Occupational Employment Data.
def plot_OED(df):
    print(df.head())

# Function to plot labor data data over time in CO.
def plot_laborforcedata(df):
    # Set x axis as date index from imported monthly report, and convert values to datetime
    x = df.index
    x = list(map(pd.to_datetime, x))
    # Set three y values, and convert population strings to int from monthly data
    y1 = df['Labor Force']
    y1 = pd.to_numeric(y1, errors='ignore')
    y2 = df['Employed']
    y2 = pd.to_numeric(y2, errors='ignore')
    y3 = df['Unemployment Rate']

    # Set up matplotlib figure and axes
    fig, ax1 = plt.subplots()
    # Plot Labor Force and Employed populations over time, filling between to show number of Unemployed
    ax1.plot(x, y1, '-.', label="Labor Force")
    ax1.plot(x, y2, '-.', label="Employed")
    ax1.fill_between(x, y1, y2, facecolor='red', alpha=0.25)
    # Label and set a reasonable y-axis limit
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of People (in millions)')
    ax1.set_ylim([1500000, 3200000])
    ax1ylabels = ax1.get_yticks()
    ax1ylabels = [str_in_millions(x) for x in ax1ylabels]
    ax1.set_yticklabels(ax1ylabels)
    # Set up second axis for Unemployment Rate
    ax2 = ax1.twinx()
    # Plot Unemployment Rate over same period of time
    ax2.plot(x, y3, '-', label="Unemployment Rate")
    # Label and set reasonable limits
    ax2.set_ylabel('Unemployment Rate')
    ax2.set_ylim([0,0.12])
    ax2ylabels = ax2.get_yticks()
    ax2ylabels = [str(x*100)+'%' for x in ax2ylabels]
    ax2.set_yticklabels(ax2ylabels)
    # Dejunkify
    make_patch_spines_invisible(ax1)
    make_patch_spines_invisible(ax2)
    ax2.spines['bottom'].set_visible(True)
    ax2.grid(axis='y')

    # Show the plot
    fig.tight_layout()
    # plt.legend()
    plt.show()

plot_OED(df3)