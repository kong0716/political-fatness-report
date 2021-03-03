import csv
import numpy as np
import matplotlib.pyplot as plt
import numpy

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

aggregateFatScore = dict()
aggregatePPScore = dict()
stateDistrictAmount = dict()

for i in range(len(stateDistrictID)):
    state = stateDistrictID[i][:2]
    if state in aggregateFatScore:
        #Running sum of score or any median, mean to get the score of the entire state
        aggregateFatScore[state] += fatness2[i]
        aggregatePPScore[state] += polsbyPopper[i]
        stateDistrictAmount[state] += 1
    else:
        aggregateFatScore[state] = fatness2[i]
        aggregatePPScore[state] = polsbyPopper[i]
        stateDistrictAmount[state] = 0
meanFatScore = dict()
meanPPScore = dict()
states = list(stateDistrictAmount.keys())
for i in range(len(states)):
    state = states[i]
    meanFatScore[state] = aggregateFatScore[state] / stateDistrictAmount[state]
    meanPPScore[state] = aggregatePPScore[state] / stateDistrictAmount[state]
labels = aggregateFatScore.keys()
'''
populationFatness = aggregateFatScore.values()
ppScores = aggregatePPScore.values()
'''
populationFatness = meanFatScore.values()
ppScores = meanPPScore.values()

x = np.arange(len(labels))
width = .35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, populationFatness, width, label='FatScore')
rects2 = ax.bar(x + width/2, ppScores, width, label='PolsbyPopper')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by Fatness and PolsbyPopper')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

'''
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

'''
#autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()

plt.show()