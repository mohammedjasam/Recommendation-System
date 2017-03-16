from surprise import Dataset
from surprise import Reader
import os


from surprise import SVD
from surprise import NMF
from surprise import KNNBasic
from surprise import Dataset
from surprise import evaluate, print_perf
import osfrom surprise import  Reader

#load data from a file
file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)

#splitting data into 3 folds
data.split(n_folds=3)

#SVD Algorithm
algo = SVD()

#PMF Algorithm
# algo = SVD(biased=False)

#NMF Algorithm
# algo = NMF()

#User Based Collaborative Filtering Algorithm
# algo = KNNBasic(sim_options = {'user_based': True})
#To used MSD in User Based Algorithm
# algo = KNNBasic(sim_options = {'name':’MSD’,'user_based': True })
#To used Cosine in User Based Algorithm
#algo = KNNBasic(sim_options = {'name':’cosine’,'user_based': True })

#Item based Collaborative Filtering algorithm.
#algo = KNNBasic(sim_options = {'user_based': False})


perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)
