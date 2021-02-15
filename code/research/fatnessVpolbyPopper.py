import csv
import numpy as np
import matplotlib.pyplot as plt
import numpy

stateDistrictID = []
fatness1 = []
#fat2 is the idea of the population of the district over the population of the bounding circle 
fatness2 = []
fatness3 = []
#fat4 improves on the idea of fat2 and weighs population on the edge of the circle less than the ones closer to the center
fatness4 = []
polsbyPopper = []
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['stateDistrictID'], row['fatness1'],  row['fatness2'],  row['polsbyPopper'])
        stateDistrictID.append(row['stateDistrictID'])
        fatness1.append(float(row['fatness1']))
        fatness2.append(float(row['fatness2']))
        fatness3.append(float(row['fatness3']))
        fatness4.append(float(row['fatness4']))
        polsbyPopper.append(float(row['polsbyPopper']))

fatness1 = np.array(fatness1).round(decimals=6)
fatness2 = np.array(fatness2).round(decimals=6)
fatness3 = np.array(fatness3).round(decimals=6)
polsbyPopper = np.array(polsbyPopper).round(decimals=6)

for i in range(len(stateDistrictID)):
    w = fatness4[i]
    x = polsbyPopper[i]
    y = fatness1[i]
    z = fatness2[i]
    plt.plot(x, w, 'bo')
    plt.text(x * (1 + 0.007), w * (1 + 0.007) , stateDistrictID[i], fontsize=6)

plt.ylim(ymin=0)  # this line
plt.xlim(0)
plt.xlabel('PolsbyPopper', fontsize=12)
plt.ylabel('Weighted Fatness (Population)', fontsize=12)
plt.show()