
import matplotlib.pyplot as plt
with open("ekg_signal.txt","r")as file:
    signal=[float(line)for line in file]
# #
print(signal)
# #
# #
plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
# )