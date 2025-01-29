import time
import json
import pandas as pd
import matplotlib.pyplot as plt

# input data
file = 'dataset_1000/repository/meters_1_measurement.json'
with open(file, 'r') as f:
    data = json.load(f)

df_input = data
df = pd.DataFrame(df_input)
df = df.explode(['laggingReactivePower','leadingReactivePower','consumption'])
df['date'] = pd.to_datetime(df[['day','month','year']])
print(df['date'])
print(len(df))
df2 = pd.Series(pd.date_range('1/1/2016', '1/31/2017', freq='15min', closed='left'))
print(df2)
print(len(df2))
# plotting
cols = ['leadingReactivePowerSum','laggingReactivePowerSum','maxConsumption','lowConsumptionSum','highConsumptionSum']

for col in cols:
    plt.plot(df['date'], df[col], label='M1 ' + col)

plt.title("Data")
plt.legend()
plt.show()