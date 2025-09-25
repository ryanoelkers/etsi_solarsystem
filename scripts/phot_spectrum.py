import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np

wvs = np.array([937, 873, 763, 713,
                660, 620, 587, 559,
                533, 512, 494, 476,
                467, 448, 435])
wvs_nm = np.array(['937nm', '873nm', '763nm', '713nm',
                   '660nm', '620nm', '587nm', '559nm',
                   '533nm', '512nm', '494nm', '476nm',
                   '467nm', '448nm', '435nm'])
wvs_err = np.array(['937nm_err', '873nm_err', '763nm_err', '713nm_err',
                    '660nm_err', '620nm_err', '587nm_err', '559nm_err',
                    '533nm_err', '512nm_err', '494nm_err', '476nm_err',
                    '467nm_err', '448nm_err', '435nm_err'])
clrs = ['red', 'red', 'orange', 'orange',
        'gold', 'gold', 'green', 'green',
        'blue', 'blue', 'cyan', 'cyan',
        'purple', 'purple', 'black']

depths = np.zeros(15)
depths_err = np.zeros(15)
dy = 2459769.

for idx, nm in enumerate(wvs_nm):

    # read in the light curve
    dt = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/" + nm + ".txt",
                 names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")

    # drop the extra transmission data point
    if idx % 2 == 0:
         dt = dt[:-1].copy().reset_index(drop=True)

    # convert to magnitude
    dt[nm] = dt.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)
    dt[wvs_err[idx]] = dt.apply(lambda x: (np.log(10.) / 2.5) * (np.sqrt(x.flx) / (x.flx - x.bkg)), axis=1)
    dt['jd'] = dt['jd'] - dy

    # normalize to out of transit
    tr = (dt.jd > 0.887) & (dt.jd < 0.891)
    dt[nm] = dt[nm] - dt[~tr][nm].median()

    # insert into main data holder
    if idx == 0:
        lc = dt[['jd', nm, wvs_err[idx]]].copy().reset_index(drop=True)
    else:
        lc[nm] = dt[nm].to_numpy()
        lc[wvs_err[idx]] = dt[wvs_err[idx]].to_numpy()

    depths[idx] = np.median(lc[(lc.jd > 0.888) & (lc.jd < 0.890)][nm])
    depths_err[idx] = np.std(lc[(lc.jd > 0.888) & (lc.jd < 0.890)][nm])

print('hold')
# plt.errorbar(wvs, depths, yerr=depths_err, fmt='none', c='k')
# plt.scatter(wvs, depths, marker='.', c='k')
# plt.xlabel('Wavelength [nm]')
# plt.ylabel('Relative Transit Depth [mag]')
# plt.show()
