import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np

wvs = np.array([973, 763, 660, 587, 533, 494, 467, 435])

lc1 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/873nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc1['mag'] = lc1.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

plt.plot(lc1.jd, lc1.mag)
plt.show()
lc2 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/763nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc2['mag'] = lc2.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc3 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/660nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc3['mag'] = lc3.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc4 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/587nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc4['mag'] = lc4.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc5 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/533nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc5['mag'] = lc5.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc6 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/494nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc6['mag'] = lc6.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc7 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/467nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc7['mag'] = lc7.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

lc8 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/435nm.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc8['mag'] = lc8.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

dy = 2459769.
lc1.jd = lc1.jd - dy
lc2.jd = lc2.jd - dy
lc3.jd = lc3.jd - dy
lc4.jd = lc4.jd - dy
lc5.jd = lc5.jd - dy
lc6.jd = lc6.jd - dy
lc7.jd = lc7.jd - dy
lc8.jd = lc8.jd - dy

lc1 = lc1[(lc1.jd > 0.87) & (lc1.jd < 0.91)].copy().reset_index(drop=True)
lc2 = lc2[(lc2.jd > 0.87) & (lc2.jd < 0.91)].copy().reset_index(drop=True)
lc3 = lc3[(lc3.jd > 0.87) & (lc3.jd < 0.91)].copy().reset_index(drop=True)
lc4 = lc4[(lc4.jd > 0.87) & (lc4.jd < 0.91)].copy().reset_index(drop=True)
lc5 = lc5[(lc5.jd > 0.87) & (lc5.jd < 0.91)].copy().reset_index(drop=True)
lc6 = lc6[(lc6.jd > 0.87) & (lc6.jd < 0.91)].copy().reset_index(drop=True)
lc7 = lc7[(lc7.jd > 0.87) & (lc7.jd < 0.91)].copy().reset_index(drop=True)
lc8 = lc8[(lc8.jd > 0.87) & (lc8.jd < 0.91)].copy().reset_index(drop=True)

# tr = (lc5.jd > 0.885) & (lc5.jd < 0.895)
tr = (lc5.jd > 0.887173) & (lc5.jd < 0.891270)
lc1['nmag'] = lc1['mag'] - lc1[~tr].mag.mean()
lc2['nmag'] = lc2['mag'] - lc2[~tr].mag.mean()
lc3['nmag'] = lc3['mag'] - lc3[~tr].mag.mean()
lc4['nmag'] = lc4['mag'] - lc4[~tr].mag.mean()
lc5['nmag'] = lc5['mag'] - lc5[~tr].mag.mean()
lc6['nmag'] = lc6['mag'] - lc6[~tr].mag.mean()
lc7['nmag'] = lc7['mag'] - lc7[~tr].mag.mean()
lc8['nmag'] = lc8['mag'] - lc8[~tr].mag.mean()

depths = np.zeros(8)
dp_tm = (lc2.jd > 0.888) & (lc2.jd < 0.891)
from sklearn.linear_model import LinearRegression

lc1['trd2'] = lc2['nmag']
lc1['trd3'] = lc3['nmag']
lc1['trd4'] = lc4['nmag']
lc1['trd5'] = lc5['nmag']
lc1['trd6'] = lc6['nmag']
lc1['trd7'] = lc7['nmag']
lc1['trd8'] = lc8['nmag']

lc1['wht'] = lc1[['nmag', 'trd2', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']].median(axis=1)
model_tr = lc1['wht'].to_numpy()
model_tr[~tr] = 0

x = lc1[~tr][['trd2', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']]
y = lc1[~tr]['nmag']
xx = lc1[['trd2', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc1.jd, lc1.nmag - model + model_tr, c='red', marker='.')
depths[0] = np.median(lc1[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])


lc2['trd1'] = lc1['nmag']
lc2['trd3'] = lc3['nmag']
lc2['trd4'] = lc4['nmag']
lc2['trd5'] = lc5['nmag']
lc2['trd6'] = lc6['nmag']
lc2['trd7'] = lc7['nmag']
lc2['trd8'] = lc8['nmag']

lc2['wht'] = lc2[['trd1', 'nmag', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']].median(axis=1)
x = lc2[~tr][['trd1', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']]
y = lc2[~tr]['nmag']
xx = lc2[['trd1', 'trd3', 'trd4', 'trd5', 'trd6', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc2.jd, lc2.nmag - model + model_tr, c='orange', marker='.')
depths[1] = np.median(lc2[dp_tm].nmag - model[dp_tm] + model_tr[dp_tm])

lc3['trd1'] = lc1['nmag']
lc3['trd2'] = lc2['nmag']
lc3['trd4'] = lc4['nmag']
lc3['trd5'] = lc5['nmag']
lc3['trd6'] = lc6['nmag']
lc3['trd7'] = lc7['nmag']
lc3['trd8'] = lc8['nmag']

lc3['wht'] = lc3[['trd1', 'trd2', 'nmag', 'trd4', 'trd5', 'trd6', 'trd7']].median(axis=1)
x = lc3[~tr][['trd1', 'trd2', 'trd4', 'trd5', 'trd6', 'trd7']]
y = lc3[~tr]['nmag']
xx = lc3[['trd1', 'trd2', 'trd4', 'trd5', 'trd6', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc3.jd, lc3.nmag - model + model_tr, c='yellow', marker='.')
depths[2] = np.median(lc3[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])

lc4['trd1'] = lc1['nmag']
lc4['trd2'] = lc2['nmag']
lc4['trd3'] = lc3['nmag']
lc4['trd5'] = lc5['nmag']
lc4['trd6'] = lc6['nmag']
lc4['trd7'] = lc7['nmag']
lc4['trd8'] = lc8['nmag']

lc4['wht'] = lc4[['trd1', 'trd2', 'trd3', 'nmag', 'trd5', 'trd6', 'trd7']].median(axis=1)
x = lc4[~tr][['trd1', 'trd2', 'trd3', 'trd5', 'trd6', 'trd7']]
y = lc4[~tr]['nmag']
xx = lc4[['trd1', 'trd2', 'trd3', 'trd5', 'trd6', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc4.jd, lc4.nmag - model + model_tr, c='green', marker='.')
depths[3] = np.median(lc4[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])

lc5['trd1'] = lc1['nmag']
lc5['trd2'] = lc2['nmag']
lc5['trd3'] = lc3['nmag']
lc5['trd4'] = lc4['nmag']
lc5['trd6'] = lc6['nmag']
lc5['trd7'] = lc7['nmag']
lc5['trd8'] = lc8['nmag']

lc5['wht'] = lc5[['trd1', 'trd2', 'trd3', 'trd4', 'nmag', 'trd6', 'trd7']].median(axis=1)
x = lc5[~tr][['trd1', 'trd2', 'trd3', 'trd4', 'trd6', 'trd7']]
y = lc5[~tr]['nmag']
xx = lc5[['trd1', 'trd2', 'trd3', 'trd4', 'trd6', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc5.jd, lc5.nmag - model + model_tr, c='b', marker='.')
depths[4] = np.median(lc5[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])

lc6['trd1'] = lc1['nmag']
lc6['trd2'] = lc2['nmag']
lc6['trd3'] = lc3['nmag']
lc6['trd4'] = lc4['nmag']
lc6['trd5'] = lc5['nmag']
lc6['trd7'] = lc7['nmag']
lc6['trd8'] = lc8['nmag']

lc6['wht'] = lc6[['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'nmag', 'trd7']].median(axis=1)
x = lc6[~tr][['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'trd7']]
y = lc6[~tr]['nmag']
xx = lc6[['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'trd7']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc6.jd, lc6.nmag - model + model_tr, c='cyan', marker='.')
depths[5] = np.median(lc6[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])

lc7['trd1'] = lc1['nmag']
lc7['trd2'] = lc2['nmag']
lc7['trd3'] = lc3['nmag']
lc7['trd4'] = lc4['nmag']
lc7['trd5'] = lc5['nmag']
lc7['trd6'] = lc6['nmag']
lc7['trd8'] = lc8['nmag']

lc7['wht'] = lc7[['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'trd6', 'nmag']].median(axis=1)
x = lc7[~tr][['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'trd6']]
y = lc7[~tr]['nmag']
xx = lc7[['trd1', 'trd2', 'trd3', 'trd4', 'trd5', 'trd6']]
model = LinearRegression().fit(x, y).predict(xx)
plt.scatter(lc7.jd, lc7.nmag - model + model_tr, c='purple', marker='.')
depths[6] = np.median(lc7[dp_tm].nmag) # - model[dp_tm] + model_tr[dp_tm])
plt.show()

plt.plot(wvs[:-1], depths[:-1], marker='x')
plt.show()