MapPlot.py
# Name:
# Date:
# Assignment:

import wind_turbines
import pandas as pd 
import matplotlib.pyplot as plt 
turbines = wind_turbines.get_turbines()

print(turbines[0]["Data"]["Number_Turbines"]["Total"])
years = []
totals = []
for turbine in turbines:
    year = turbine["Year"] 
    total = turbine["Data"]["Number_Turbines"]["Total"] 
    if total != 0: 
        years.append(year) 
        totals.append(total)
    #print(year, total)
df = pd.DataFrame({"Year": years, "Total": totals})

print(df) 
#df.plot(kind = 'scatter', x = 'Year', y = 'Total')
plt.plot(years, totals, 'ro')
plt.xlabel("Year")
plt.title("Number of Turbines over time")
plt.savefig("Output.png") 
plt.close() 
