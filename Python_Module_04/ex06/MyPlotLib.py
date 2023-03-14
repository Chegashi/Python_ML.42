import matplotlib.pyplot as plt
import pandas as pd

class MyPlotLib:
    def histogram(self, data, features):
        figure, axis = plt.subplots(1, len(features))
        for i in range(len(features)):
                axis[i].hist(data[features[i]])
                axis[i].set_title(features[i])
        figure.tight_layout()
        plt.show()

    def density(self, data, features):
        df = pd.DataFrame(data, columns=features) 
        df.plot.kde()
        plt.show()

    def pair_plot(self, data, features):
        df = pd.DataFrame(data, columns=features)
        pd.plotting.scatter_matrix(df)
        plt.show()

    def box_plot(self, data, features):
        df = pd.DataFrame(data, columns=features)
        df.boxplot(column=features)
        plt.show()