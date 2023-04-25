import matplotlib.pyplot as plt

plt.figure()
plt.xlabel("Categories")
plt.ylabel("Amounts")
plt.title("Categories vs. Amounts")

plt.plot(["Men", "Women", "Children"], [3,5,9], "ko")
plt.show()