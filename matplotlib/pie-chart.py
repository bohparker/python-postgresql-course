import matplotlib.pyplot as plt


option_votes = [63, 28, 8]
option_name = [
    "Flask",
    "Django",
    "Depends"
]

figure = plt.figure()
axes = figure.add_subplot()

axes.pie(option_votes, labels=option_name)

plt.show()