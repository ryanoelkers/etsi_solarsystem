import photutils
import pandas as pd
import astropy
from astropy.io import fits
from libraries.utils import Utils

camera = 'reflection'
dir = "/Users/yuw816/Data/solarsystem/titan/images/coadded/" + camera + "/"

files = Utils.get_file_list(dir, ".fits")

from photutils.aperture import RectangularAperture, aperture_photometry, ApertureStats
from photutils.centroids import centroid_com
import numpy as np

# file names
if camera == 'transmission':
    bands = ['937nm', '763nm', '660nm', '587nm', '533nm', '494nm', '467nm', '435nm']
    x_org = [891, 975, 1060, 1147, 1240, 1331, 1430, 1537]
    y_org = [888, 887,  887,  886,  886,  884,  884,  883]
    x_box = 84
    y_box = 26
    sky_mve = 50
else:
    bands = ['873nm', '713nm', '620nm', '559nm', '512nm', '476nm', '448nm']
    x_org = [881, 1035, 1192, 1342, 1496, 1657, 1826]
    y_org = [1344, 1344,  1344,  1344,  1344, 1344,  1344]
    x_box = 150
    y_box = 50
    sky_mve = 75


for idy, ii in enumerate(bands):
    flx = np.zeros(len(files))
    tme = np.zeros(len(files))
    bkg = np.zeros(len(files))
    xs = np.zeros(len(files))
    ys = np.zeros(len(files))
    exp = np.zeros(len(files))

    f = open("/Users/yuw816/Development/etsi_solarsystem/analysis/" + ii + ".txt", "w+")
    x = x_org[idy]
    y = y_org[idy]
    for idx, file in enumerate(files):

        data = fits.getdata(dir + file)
        data_c = data[int(y - y_box/2):int(y + y_box/2), int(x - x_box/2):int(x + x_box/2)]
        hdr = fits.getheader(dir + file)

        # star position
        x1, y1 = centroid_com(data_c)
        positions = [(np.around(x - x_box/2 + x1, decimals=2),
                      np.around(y - y_box/2 + y1, decimals=2))]
        x_cen = np.around(x - x_box/2 + x1, decimals=2)
        y_cen = np.around(y - y_box/2 + y1, decimals=2)

        aperture = RectangularAperture(positions, w=x_box, h=y_box)
        phot_table = aperture_photometry(data, aperture)
        apt_stat = ApertureStats(data, aperture)
        flx[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']
        tme[idx] = np.mean([hdr['COADD_ST'], hdr['COADD_ED']])
        xs[idx] = x_cen
        ys[idx] = y_cen
        exp[idx] = np.mean([hdr['AIRMASSS'], hdr['AIRMASSE']])

        # background
        positions = [(np.around(x - x_box/2 + x1 + sky_mve, decimals=2),
                      np.around(y - y_box/2 + y1 + sky_mve, decimals=2))]

        aperture = RectangularAperture(positions, w=x_box, h=y_box)
        phot_table = aperture_photometry(data, aperture)
        bkg[idx] = phot_table['aperture_sum'].item() / hdr['EXP_TIME']

        f.write(str(np.around(tme[idx], decimals=6)) + " " + str(np.around(flx[idx], decimals=2)) + " " +
                str(np.around(bkg[idx], decimals=2)) + " " + str(np.around(xs[idx], decimals=2)) + " " +
                str(np.around(ys[idx], decimals=2)) + " " + str(np.around(exp[idx], decimals=4)) + "\n")
        x = x_cen
        y = y_cen
    f.close()
