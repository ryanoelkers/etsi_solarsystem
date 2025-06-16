import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.signal import medfilt

flx = ["ap1", "ap2", "ap3", "ap4", "ap5", "ap6", "ap7", "ap8"]
mag = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8"]
rmg = ["mr1", "mr2", "mr3", "mr4", "mr5", "mr6", "mr7"]
bkg = ["bkg1", "bkg2", "bkg3", "bkg4", "bkg5", "bkg6", "bkg7", "bkg8"]
x = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
y = ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"]
xr = ["xr1", "xr2", "xr3", "xr4", "xr5", "xr6", "xr7"]
yr = ["yr1", "yr2", "yr3", "yr4", "yr5", "yr6", "yr7"]

tr = pd.read_csv("C:\\Users\\ryanj\\Development\\etsi_solarsystem\\analysis\\titan_transmission.txt",
                 sep=" ")
rf = pd.read_csv("C:\\Users\\ryanj\\Development\\etsi_solarsystem\\analysis\\titan_reflection.txt",
                 sep=" ")

tr = tr[:len(rf)].reset_index(drop=True)
for idx, f in enumerate(flx):
    tr[mag[idx]] = tr.apply(lambda x: 25 - 2.5 * np.log10(x[f] - x[bkg[idx]]), axis=1)
    if idx < 7:
        tr[rmg[idx]] = rf.apply(lambda x: 25 - 2.5 * np.log10(x[f] - x[bkg[idx]]), axis=1)
        tr[xr[idx]] = rf[x[idx]].to_numpy()
        tr[yr[idx]] = rf[y[idx]].to_numpy()

bin_size = 0.000060
bin_strt = tr.jd.min()
bin_end = tr.jd.max()
tr['time_bin'] = 0
ii = 0

while bin_strt < bin_end:
    tr.loc[(tr.jd > bin_strt) & (tr.jd <= bin_strt + bin_size), 'time_bin'] = ii
    bin_strt = bin_strt + bin_size
    ii = ii + 1

df = tr.groupby('time_bin').agg({'jd': 'mean', 'airmass': 'mean',
                                 'x1':'mean', 'y1': 'mean','x2':'mean', 'y2': 'mean',
                                 'x3':'mean', 'y3': 'mean','x4':'mean', 'y4': 'mean',
                                 'x5':'mean', 'y5': 'mean','x6':'mean', 'y6': 'mean',
                                 'x7':'mean', 'y7': 'mean','x8':'mean', 'y8': 'mean',
                                 'm1': 'median', 'm2':'median',
                                 'm3': 'median', 'm4':'median',
                                 'm5': 'median', 'm6':'median',
                                 'm7': 'median', 'm8':'median',
                                 'mr1': 'median', 'mr2':'median',
                                 'mr3': 'median', 'mr4':'median',
                                 'mr5': 'median', 'mr6':'median',
                                 'xr1': 'mean', 'yr1': 'mean', 'xr2': 'mean', 'yr2': 'mean',
                                 'xr3': 'mean', 'yr3': 'mean', 'xr4': 'mean', 'yr4': 'mean',
                                 'xr5': 'mean', 'yr5': 'mean', 'xr6': 'mean', 'yr6': 'mean',
                                 'xr7': 'mean', 'yr7': 'mean',
                                 'mr7': 'median'})

df = df[(df.jd <= 2459769.9) & (df.jd >= 2459769.875)].copy().reset_index(drop=True)
oot = df[(df.jd <= 2459769.884) | (df.jd >= 2459769.894)].copy().reset_index(drop=True)

cc = ['maroon', 'red', 'orange', 'brown', 'yellow', 'gold', 'green',
      'darkgreen', 'cyan', 'dodgerblue', 'blue', 'purple', 'violet', 'pink', 'black']
deps = np.zeros(15)
wvs = np.array([937, 873, 763, 713, 660, 620, 587, 559, 533, 512, 494, 476, 467, 448, 435])

from sklearn.linear_model import LinearRegression
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
xlist = ['jd']
pp = oot[xlist]
depths = np.zeros(15)
for idx, m in enumerate(mag):

    yy = oot[m] - oot[mag[1]]

    rr = df[xlist]
    vv = LinearRegression().fit(pp,yy).predict(rr)

    kernel = ConstantKernel() * RBF()
    # GP model
    gp = GaussianProcessRegressor()
    # Fitting in the gp model
    gp.fit(pp, yy)
    # Make the prediction on test set.
    v = gp.predict(rr)

    if idx == 1:
        depths[idx * 2] = 0
    else:
        df['cln'] = (df[m] - df[mag[1]]) - v

        depths[idx * 2] = df[(df.jd < 2459769.89) & (df.jd > 2459769.888)].cln.mean()

    if idx < 7:

        yy = oot[rmg[idx]] - oot[mag[1]]

        rr = df[xlist]
        vv = LinearRegression().fit(pp, yy).predict(rr)

        kernel = ConstantKernel() * RBF()
        # GP model
        gp = GaussianProcessRegressor()
        # Fitting in the gp model
        gp.fit(pp, yy)
        # Make the prediction on test set.
        v = gp.predict(rr)
        df['cln'] = (df[rmg[idx]] - df[mag[1]]) - v
        depths[idx * 2 + 1] = df[(df.jd < 2459769.89) & (df.jd > 2459769.888)].cln.mean()

plt.plot(wvs, depths)
#plt.gca().invert_yaxis()
plt.show()
print('hold')