import pandas
import seaborn
import matplotlib

FILE = "./puzzle31-lamp2-2downs.csv"

data = pandas.read_csv(FILE, delimiter=";")

correlation_heatmap = seaborn.heatmap(data.corr(method='pearson'), center=0.3, cmap='Purples', annot=True, fmt=".2f", square=True)
correlation_heatmap.figure.set_size_inches(8,8)
matplotlib.pyplot.show()
