import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    years_extended = list(range(1880, 2051))
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best fit line 1880-2050')
    
    # Create second line of best fit
    recent_data = data[data["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    years_recent_extended = list(range(2000, 2051))
    plt.plot(years_recent_extended, [slope_recent * year + intercept_recent for year in years_recent_extended], label='Best fit line 2000-2050', color='red')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
