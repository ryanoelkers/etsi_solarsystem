import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np

lc2 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/band2.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc2['mag'] = lc2.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)
lc5 = pd.read_csv("/Users/yuw816/Development/etsi_solarsystem/analysis/band5.txt",
                  names=['jd', 'flx', 'bkg', 'x', 'y', 'ams'], sep=" ")
lc5['mag'] = lc5.apply(lambda x: 25 - 2.5 * np.log10(x.flx - x.bkg), axis=1)

# plt.plot(lc2.jd, lc2.mag - lc2.mag.min(), c='r')
# plt.plot(lc5.jd, lc5.mag - lc5.mag.min(), c='b')
# plt.show()
# np.sqrt((lc2.x - lc5.x) ** 2 + (lc2.y - lc5.y) ** 2)
plt.plot(lc5.ams, lc5.mag - lc2.mag, c='k')
plt.show()