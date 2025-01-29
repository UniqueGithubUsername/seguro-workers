import time
import json
import pandas as pd
import matplotlib.pyplot as plt

# input data
file = 'dataset_1000/repository/meters_1_measurement.json'
with open(file, 'r') as f:
    data = json.load(f)

df_input = data[1]
df = pd.DataFrame(df_input)
df['date'] = pd.to_datetime(df[['day','month','year']])

# Make dates with 15 minutes interval
df2 = pd.Series(pd.date_range('1/1/2016', '1/2/2016', freq='15min', closed='left'))

df = df.explode(['laggingReactivePower','leadingReactivePower','consumption'])

print("After explode")
df['date'] = df2
print(df)

# plotting
cols = ['leadingReactivePower','laggingReactivePower','consumption']

for col in cols:
    plt.plot(df['date'], df[col], label='M1 ' + col)

plt.title("Data")
plt.legend()
plt.show()