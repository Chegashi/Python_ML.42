import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid# number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
		self.n = 0
		self.k = ncentroid
		self.p = 3
		self.closest = None

	def fit(self, x):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			None.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		self.n = len(x)
		self.centroids = x[np.random.choice(self.n, self.k, replace=False)]
		closest = np.zeros(self.n).astype(int)
		for iter in range(self.max_iter):
			distances = np.zeros((self.n, self.k))
			for i in range(self.k):
				distances[:,i] =((x - self.centroids[i])**2).sum(axis=1)**0.5
			self.closest = np.argmin(distances, axis =1)
		for i in range(self.k):
			self.centroids[i, :] = x[self.closest == i].mean(axis=0)
		# print(self.closest, self.centroids)

	def predict(self, x):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		self.fit(x)
		x = np.insert(x, 3, self.closest, axis=1)
		mean = np.zeros((3, 4))
		for i in range(4):
			for j in range(3):
				mean[j,i] = x[x[:,3] == i][:,j].mean()
		mean_tmp = mean
		labal = {np.argmax(mean_tmp[0,:]): 'Asteroids’ Belt colonies'}
		mean_tmp = np.delete(mean_tmp, np.argmax(mean_tmp[0,:]), axis=1)
		labal.update({np.where(max(mean_tmp[1,:]) == mean)[1][0]: 'The flying cities of Venus'})
		mean_tmp = np.delete(mean, list(labal.keys()) , axis=1)
		labal.update({np.where(min(mean_tmp[0,:]) == mean)[1][0]: 'United Nations of Earth'})
		mean_tmp = np.delete(mean, list(labal.keys()) , axis=1)
		labal.update({np.where(min(mean_tmp[0,:]) == mean)[1][0]: 'Mars Republic'})
		mean_tmp = np.delete(mean, list(labal.keys()) , axis=1)
		fig = plt.figure(figsize = (10, 7))
		ax = plt.axes(projection ="3d")
		ar_0 = x[x[:, 3] == 0]
		ar_1 = x[x[:, 3] == 1]
		ar_2 = x[x[:, 3] == 2]
		ar_3 = x[x[:, 3] == 3]
		ax.scatter3D(ar_0[:,0], ar_0[:,1], ar_0[:,2], marker='<', s=20, label=str(labal[0]))
		ax.scatter3D(ar_1[:,0], ar_1[:,1], ar_1[:,2], marker='+', s=20, label=str(labal[1]))
		ax.scatter3D(ar_2[:,0], ar_2[:,1], ar_2[:,2], marker='*', s=20, label=str(labal[2]))
		ax.scatter3D(ar_3[:,0], ar_3[:,1], ar_3[:,2], marker='o', s=20, label=str(labal[3]))
		plt.legend(loc="upper right")
		plt.rcParams["figure.autolayout"] = True
		plt.title("simple 3D scatter plot")
		plt.show()		

def main(*arg, **kwarg):
	try:
		dict_arg = {'filepath=' : '', 'ncentroid': 0, 'max_iter' : 0}
		dict_arg.update(dict(arg.split('=') for arg in sys.argv[1:]))
		kmeans = KmeansClustering(int(dict_arg["max_iter"]), int(dict_arg["ncentroid"]))
		x = np.genfromtxt(dict_arg["filepath"], delimiter=',')
		x = np.delete(x, 0, 1)
		x = np.delete(x, 0, 0)
		kmeans.predict(x)
	except:
		print("Erreur")
		exit(1)
	
if __name__ == "__main__":
    main()
