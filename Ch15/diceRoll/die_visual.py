from die import Die
import pygal

#create a D6 - 6 sided die
die_1 = Die()
die_2 = Die()

#make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dices 1k times"
#hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = range(2,13)
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
