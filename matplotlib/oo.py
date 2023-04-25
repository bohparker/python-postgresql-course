import matplotlib.pyplot as plt

# create a variable for the figure
figure = plt.figure()
axes = figure.add_subplot()
axes.set_title("A test line graph")
axes.set_xlabel("Numbers")
axes.set_ylabel("Occurrences")
axes.plot([1,2,3,4], [3,5,9,25])
plt.show()