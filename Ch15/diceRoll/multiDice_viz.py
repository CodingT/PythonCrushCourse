#15-9 Multiplication
from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)

results=[]
for roll in range(1000):
    result = die_1.roll() * die_2.roll() #multiply dices roll results
    results.append(result)

#analyze results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results + 1): 
    frequency = results.count(value) #count how offten appears each combination value
    frequencies.append(frequency)    

#visualize results
hist = pygal.Bar()

hist.title = "Rolling three D6 1k times"
hist.x_labels = range(2, max_results + 1)
hist.x_title = "Result"
hist.y_title = "Frequrency of Result"

hist.add("D6 X D6", frequencies)
hist.render_to_file('multiDice_visual.svg')
