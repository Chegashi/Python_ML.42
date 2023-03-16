import matplotlib.pyplot as plt
import pandas as pd
from FileLoader import FileLoader
class MyPlotLib:
    def histogram(self, data, features):
        if len(features) == 1:
            plt.hist(data[features[0]])
            plt.title(features[0])
        else :
            figure, axis = plt.subplots(1,len(features))
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
        fig = plt.figure()
        fig.add_subplot()
        data.boxplot(column=features, grid=False)
        plt.show()

def main():
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    m = MyPlotLib()


    m.density(data, ["Weight"])
    m.density(data, ["Weight", "Height"])
    m.density(data, ["Weight", "Height", "Age"])

    m.histogram(data, ["Weight"])
    m.histogram(data, ["Weight", "Height"])
    m.histogram(data, ["Weight", "Height", "Age"])

    m.pair_plot(data, ["Weight"])
    m.pair_plot(data, ["Weight","Height"])
    m.pair_plot(data, ["Weight", "Height", "Age"])

    m.box_plot(data, ["Weight"])
    m.box_plot(data, ["Weight", "Height"])
    m.box_plot(data, ["Weight", "Height", "Age"])

if __name__=="__main__":
    main()
