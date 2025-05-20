import photutils
import pandas as pd
import astropy
from astropy.io import fits
from libraries.utils import Utils

dir = "/Users/yuw816/Data/solarsystem/titan/images/coadded/"

files = Utils.get_file_list(dir, ".fits")

from photutils.aperture import RectangularAperture, aperture_photometry, ApertureStats
from photutils.centroids import centroid_com
import numpy as np
x=975
y=886
x_box = 84
y_box = 26

flx = np.zeros(len(files))
tme = np.zeros(len(files))
bkg = np.zeros(len(files))
xs = np.zeros(len(files))
ys = np.zeros(len(files))
exp = np.zeros(len(files))

f = open("/Users/yuw816/Development/etsi_solarsystem/analysis/band2.txt", "w+")
for idx, file in enumerate(files):

    data = fits.getdata(dir + file)
    data_c = data[int(y-y_box/2):int(y+y_box/2), int(x-x_box/2):int(x+x_box/2)]
    hdr = fits.getheader(dir + file)

    x1, y1 = centroid_com(data_c)

    positions = [(np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1, decimals=2))]

    x = np.around(x-x_box/2 + x1, decimals=2)
    y = np.around(y-y_box/2 + y1, decimals=2)

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    phot_table = aperture_photometry(data, aperture)
    apt_stat = ApertureStats(data, aperture)
    flx[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']
    tme[idx] = np.mean([hdr['COADD_ST'], hdr['COADD_ED']])
    xs[idx] = x
    ys[idx] = y
    exp[idx] = np.mean([hdr['AIRMASSS'], hdr['AIRMASSE']])
    positions = [(np.around(x-x_box/2 + x1 + 100, decimals=2), np.around(y-y_box/2 + y1 + 100, decimals=2))]

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    phot_table = aperture_photometry(data, aperture)
    bkg[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']

    f.write(str(np.around(tme[idx], decimals=6)) + " " + str(np.around(flx[idx], decimals=2)) + " " +
            str(np.around(bkg[idx], decimals=2)) + " " + str(np.around(xs[idx], decimals=2)) + " " +
            str(np.around(ys[idx], decimals=2)) + " " + str(np.around(exp[idx], decimals=4)) + "\n")
f.close()

x=1240
y=887
x_box = 84
y_box = 26

flx = np.zeros(len(files))
tme = np.zeros(len(files))
bkg = np.zeros(len(files))
xs = np.zeros(len(files))
ys = np.zeros(len(files))
exp = np.zeros(len(files))

f = open("/Users/yuw816/Development/etsi_solarsystem/analysis/band5.txt", "w+")
for idx, file in enumerate(files):

    data = fits.getdata(dir + file)
    data_c = data[int(y-y_box/2):int(y+y_box/2), int(x-x_box/2):int(x+x_box/2)]
    hdr = fits.getheader(dir + file)

    x1, y1 = centroid_com(data_c)

    positions = [(np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1, decimals=2))]

    x = np.around(x-x_box/2 + x1, decimals=2)
    y = np.around(y-y_box/2 + y1, decimals=2)

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    phot_table = aperture_photometry(data, aperture)
    apt_stat = ApertureStats(data, aperture)
    flx[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']
    tme[idx] = np.mean([hdr['COADD_ST'], hdr['COADD_ED']])
    xs[idx] = x
    ys[idx] = y
    exp[idx] = np.mean([hdr['AIRMASSS'], hdr['AIRMASSE']])
    positions = [(np.around(x-x_box/2 + x1 + 100, decimals=2), np.around(y-y_box/2 + y1 + 100, decimals=2))]

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    phot_table = aperture_photometry(data, aperture)
    bkg[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']

    f.write(str(np.around(tme[idx], decimals=6)) + " " + str(np.around(flx[idx], decimals=2)) + " " +
            str(np.around(bkg[idx], decimals=2)) + " " + str(np.around(xs[idx], decimals=2)) + " " +
            str(np.around(ys[idx], decimals=2)) + " " + str(np.around(exp[idx], decimals=4)) + "\n")
f.close()
