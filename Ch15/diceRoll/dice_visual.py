#15-6,7
from die import Die
import pygal

die_1 = Die(8)
die_2 = Die(8)

results=[]
for roll in range(99999999):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides 
for value in range(2, max_results +1): 
    frequency = results.count(value) #count how offten appears each combination value
    frequencies.append(frequency)    

#visualize results
hist = pygal.Bar()

hist.title = "Rolling two D8 dices 999... times"
hist.x_labels = range(2, max_results+1)
hist.x_title = "Result"
hist.y_title = "Frequrency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('dice_visual.svg')

