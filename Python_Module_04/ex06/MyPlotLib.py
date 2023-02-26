import matplotlib.pyplot as plt
class MyPlotLib:
    def histogram(data, features=None):
        hist = data['Height'].hist()
        plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=100)
    
    def density(data, features):
        pass
    def pair_plot(data, features):
        pass
    def box_plot(data, features):
        pass