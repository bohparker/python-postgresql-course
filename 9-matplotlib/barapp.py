import bardb
import barchart
import matplotlib.pyplot as plt

barchart.create_bar_chart(bardb.get_polls_and_votes())
plt.show()