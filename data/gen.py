import random
import matplotlib.pyplot as plt

minutes = 2628
val = 255
val2 = 300
change = 25

# data
x = list(range(0, minutes))
data = []
demand = []
for i in range(0,minutes):
    val = val + random.randint(-10,10)
    val2 = val2 + random.randint(-1,1)
    data.append(val)
    demand.append(val2)

# plotting
plt.title("Flexibilitätsvermarktung") 
plt.xlabel("Minuten") 
plt.ylabel("Energie Nachfrage")
#ax = plt.gca()
#ax.set_ylim([0,500])
#plt.set_ylim([0,500])
plt.plot(x, data , label='Feed in', color='red')
plt.plot(x, demand , label='Demand', color='green')
plt.show()