import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np

wvs = np.array([9370, 8730, 7630, 7130, 6600,
                6200, 5870, 5590, 5330, 5120,
                4940, 4760, 4670, 4480, 4350])

bins = [[9000, 9750], [8470, 9000], [7295, 7970], [6970, 7295], [6400, 6800],
        [6005, 6400], [5745, 6005], [5440, 5745], [5230, 5440], [5030, 5230],
        [4855, 5030], [4680, 4855], [4565, 4680], [4400, 4565], [4300, 4400]]

depths = [0.50799404/1000, 0.63420745/1000, 0.41878001/1000, 0.44664602/1000, 0.41061758/1000,
          0.46575194/1000, 0.4936089/1000 , 0.56301862/1000, 0.63738079/1000, 0.73774987/1000,
          0.79096023/1000, 0.9409084/1000 , 1.03978052/1000, 1.22198131/1000, 1.51426538/1000]

errors = [0.01094719/1000, 0.01273403/1000, 0.00783981/1000, 0.00860013/1000, 0.0070582/1000,
          0.00776459/1000, 0.00770204/1000, 0.00894165/1000, 0.00954744/1000, 0.01109811/1000,
          0.01178225/1000, 0.01431912/1000, 0.0189005/1000, 0.02110805/1000, 0.07164618/1000]

from platon.fit_info import FitInfo
from platon.combined_retriever import CombinedRetriever

retriever = CombinedRetriever()

# Get default fit info for your specific planetary system
# R_sun, M_jup are standard values or can be calculated
# from your observation specifics.
fit_info = retriever.get_default_fit_info(
    Rs=1.0, Mp=1.0, Rp=1.0, T=1200, logZ=0, T_star=6100
)

result = retriever.run_dynesty(bins, depths, errors, None, None, None, fit_info, plot_best=True)

print('hold')
