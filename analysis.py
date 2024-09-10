import numpy as np
import pandas as pd
data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
columns = ['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']
df = data[columns]
# GDP Per Capita has a REALLY long right tail, so we want to log it for readability.
data["Log GDP Per Capita"] = np.log(data["GDP per capita (constant 2010 US$)"])
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

sns.set_style("whitegrid")

my_chart = (
    so.Plot(
        data, x="Log GDP Per Capita", y="Mortality rate, under-5 (per 1,000 live births)"
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Under-5 Mortality")
    
)

my_chart.show()