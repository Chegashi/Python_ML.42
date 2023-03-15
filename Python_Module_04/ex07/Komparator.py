import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Komparator:
    def __init__(self, data):
        self.data = data

    def compare_histograms(self, categorical_var, numerical_var, options=None):
        if options == None:
            options = self.data.dropna()[numerical_var].unique()
        for option in options:
            data = self.data.loc[(self.data[numerical_var] == option)]
            plt.hist(data[categorical_var], alpha=0.2, label=option)
        plt.legend()
        plt.show()
    
    def density(self, categorical_var, numerical_var, density_options=None):
        if density_options == None:
            density_options = self.data.dropna()[numerical_var].unique()
        data_density = pd.DataFrame()
        for option in density_options:
            data_density = self.data.dropna().loc[(self.data[numerical_var] == option)][categorical_var]
            data_density.plot.kde(label=option)
        plt.title(categorical_var)
        plt.legend()
        plt.show()
    
    def compare_box_plots(self, categorical_var, numerical_var, box_plots_options=None):
        if box_plots_options == None:
            box_plots_options = self.data.dropna()[numerical_var].unique()
        figure, axis = plt.subplots(1,len(box_plots_options))
        i = -1
        if len(box_plots_options) == 1:
            data_box_plots = pd.DataFrame(self.data.dropna().loc[(self.data[numerical_var] == box_plots_options[0])])
            plt.boxplot(data_box_plots[categorical_var])
            plt.title(box_plots_options[0])
        else:
            for option in box_plots_options:
                i += 1
                data_box_plots = pd.DataFrame(self.data.dropna().loc[(self.data[numerical_var] == option)])
                axis[i].boxplot(data_box_plots[categorical_var])
                axis[i].set_title(option)
        figure.tight_layout()
        plt.show()

def main():
    data = pd.read_csv('../athlete_events.csv')
    komparator = Komparator(data)
    
    komparator.compare_histograms("Weight", "Sex")
    komparator.compare_histograms("Weight", "Sex", ["F"])
    komparator.compare_histograms("Weight", "Medal", ["Gold", "Silver"])
    komparator.compare_histograms("Weight", "Medal")

    komparator.density("Weight", "Sex")
    komparator.density("Weight", "Sex", ["F"])
    komparator.density("Weight", "Medal", ["Gold", "Silver"])
    komparator.density("Weight", "Medal")

    komparator.compare_box_plots("Weight", "Sex")
    komparator.compare_box_plots("Weight", "Sex", ["F"])
    komparator.compare_box_plots("Weight", "Medal", ["Gold", "Silver"])
    komparator.compare_box_plots("Weight", "Medal")

if __name__ == "__main__":
    main()