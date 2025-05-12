import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sealevel_data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(sealevel_data['Year'], sealevel_data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linreg = linregress(sealevel_data['Year'], sealevel_data['CSIRO Adjusted Sea Level'])
    years = list(range(1880, 2051))
    prediction = []
    for year in years:
        prediction.append(linreg.slope * year + linreg.intercept)
    plt.plot(years, prediction)
    
    # Create second line of best fit
    sealevel_data2 = sealevel_data[sealevel_data['Year'] >= 2000]
    linreg2 = linregress(sealevel_data2['Year'], sealevel_data2['CSIRO Adjusted Sea Level'])
    years2 = list(range(2000, 2051))
    prediction2 = []
    for year in years2:
        prediction2.append(linreg2.slope * year + linreg2.intercept)
    plt.plot(years2, prediction2, color='blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()