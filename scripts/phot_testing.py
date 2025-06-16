from libraries.utils import Utils
from skimage import io
from astropy.time import Time
from photutils.aperture import RectangularAperture, aperture_photometry, ApertureStats
from photutils.centroids import centroid_com
import numpy as np
from astropy.io import fits
from libraries.utils import Utils

dir = "G:\\July2022\\2022-07-08\\Titan\\raw\\transmission\\"

files = Utils.get_file_list(dir, ".fits")

x_box = 84
y_box = 26

xx = (886.5012, 975.59263, 1058.5634, 1144.091, 1239.5534, 1331.9513, 1435.4845, 1537.0783)
yy = (885.65929, 886.68251, 886.21227, 885.52201, 887.48408, 888.54775, 889.59711, 888.6933)


f = open("C:\\Users\\barristan\\Development\\etsi_development\\analysis\\titan_transmission.txt", "w+")
for idx, file in enumerate(files):
    data = fits.getdata(dir + file)
    hdr = fits.getheader(dir + file)

    positions = []
    sky_pos = []

    for x, y in zip(xx, yy):

        data_c = data[int(y-y_box/2):int(y+y_box/2), int(x-x_box/2):int(x+x_box/2)]

        x1, y1 = centroid_com(data_c)

        positions.append((np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1, decimals=2)))
        sky_pos.append((np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1 + 100, decimals=2)))

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    sky = RectangularAperture(sky_pos, w=x_box, h=y_box)

    apt_stat = ApertureStats(data, aperture)
    sky_stat = ApertureStats(data, sky)

    if idx == 0:
        f.write("jd exp_time airmass ha zd ra dec humidity temp "
                "ap1 bkg1 x1 y1 ap2 bkg2 x2 y2 ap3 bkg3 x3 y3 ap4 bkg4 x4 y4 "
                "ap5 bkg5 x5 y5 ap6 bkg6 x6 y6 ap7 bkg7 x7 y7 ap8 bkg8 x8 y8\n")

    f.write(str(np.around(Time(hdr['DATE-OBS']).jd, decimals=6)) + " " +
            str(np.around(hdr['HIERARCH EXPOSURE TIME'], decimals=6)) + " " +
            str(np.around(hdr['AIRMASS'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH OBSERVED_HA_HOUR'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH OBSERVED_ZD_DEGREE'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH FLEX_RA_HOUR'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH FLEX_DEC_DEGREE'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH HUMIDITY_PERCENT'], decimals=6)) + " " +
            str(np.around(hdr['HIERARCH TEMPERATURE_C'], decimals=6)) + " " +
            str(np.around(apt_stat.sum[0], decimals=0)) + " " + str(np.around(sky_stat.sum[0], decimals=0)) + " " +
            str(np.around(positions[0][0], decimals=2)) + " " + str(np.around(positions[0][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[1], decimals=0)) + " " + str(np.around(sky_stat.sum[1], decimals=0)) + " " +
            str(np.around(positions[1][0], decimals=2)) + " " + str(np.around(positions[1][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[2], decimals=0)) + " " + str(np.around(sky_stat.sum[2], decimals=0)) + " " +
            str(np.around(positions[2][0], decimals=2)) + " " + str(np.around(positions[2][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[3], decimals=0)) + " " + str(np.around(sky_stat.sum[3], decimals=0)) + " " +
            str(np.around(positions[3][0], decimals=2)) + " " + str(np.around(positions[3][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[4], decimals=0)) + " " + str(np.around(sky_stat.sum[4], decimals=0)) + " " +
            str(np.around(positions[4][0], decimals=2)) + " " + str(np.around(positions[4][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[5], decimals=0)) + " " + str(np.around(sky_stat.sum[5], decimals=0)) + " " +
            str(np.around(positions[5][0], decimals=2)) + " " + str(np.around(positions[5][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[6], decimals=0)) + " " + str(np.around(sky_stat.sum[6], decimals=0)) + " " +
            str(np.around(positions[6][0], decimals=2)) + " " + str(np.around(positions[6][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[7], decimals=0)) + " " + str(np.around(sky_stat.sum[7], decimals=0)) + " " +
            str(np.around(positions[7][0], decimals=2)) + " " + str(np.around(positions[7][1], decimals=2)) + "\n")

    if idx % 1000 == 0:
        Utils.log("Image completed. " + str(len(files)-(idx + 1)) + " files remain.", "info")
f.close()

dir = "G:\\July2022\\2022-07-08\\Titan\\raw\\reflection\\"

files = Utils.get_file_list(dir, ".tiff")

x_box = 140
y_box = 60

xx = (867.14183, 1024.1916, 1193.6613, 1336.828, 1501.4269, 1664.5681, 1825.3117)
yy = (1354.5117, 1354.2431, 1353.4492, 1352.5239, 1343.0083, 1339.4632, 1341.8843)

f = open("C:\\Users\\barristan\\Development\\etsi_development\\analysis\\titan_reflection.txt", "w+")

for idx, file in enumerate(files):

    data = io.imread(dir + file)

    positions = []
    sky_pos = []

    for x, y in zip(xx, yy):

        data_c = data[int(y-y_box/2):int(y+y_box/2), int(x-x_box/2):int(x+x_box/2)]

        x1, y1 = centroid_com(data_c)

        positions.append((np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1, decimals=2)))
        sky_pos.append((np.around(x-x_box/2 + x1, decimals=2), np.around(y-y_box/2 + y1 + 100, decimals=2)))

    aperture = RectangularAperture(positions, w=x_box, h=y_box)
    sky = RectangularAperture(sky_pos, w=x_box, h=y_box)

    apt_stat = ApertureStats(data, aperture)
    sky_stat = ApertureStats(data, sky)

    if idx == 0:
        f.write("ap1 bkg1 x1 y1 ap2 bkg2 x2 y2 ap3 bkg3 x3 y3 ap4 bkg4 x4 y4 "
                "ap5 bkg5 x5 y5 ap6 bkg6 x6 y6 ap7 bkg7 x7 y7\n")

    f.write(str(np.around(apt_stat.sum[0], decimals=0)) + " " + str(np.around(sky_stat.sum[0], decimals=0)) + " " +
            str(np.around(positions[0][0], decimals=2)) + " " + str(np.around(positions[0][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[1], decimals=0)) + " " + str(np.around(sky_stat.sum[1], decimals=0)) + " " +
            str(np.around(positions[1][0], decimals=2)) + " " + str(np.around(positions[1][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[2], decimals=0)) + " " + str(np.around(sky_stat.sum[2], decimals=0)) + " " +
            str(np.around(positions[2][0], decimals=2)) + " " + str(np.around(positions[2][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[3], decimals=0)) + " " + str(np.around(sky_stat.sum[3], decimals=0)) + " " +
            str(np.around(positions[3][0], decimals=2)) + " " + str(np.around(positions[3][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[4], decimals=0)) + " " + str(np.around(sky_stat.sum[4], decimals=0)) + " " +
            str(np.around(positions[4][0], decimals=2)) + " " + str(np.around(positions[4][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[5], decimals=0)) + " " + str(np.around(sky_stat.sum[5], decimals=0)) + " " +
            str(np.around(positions[5][0], decimals=2)) + " " + str(np.around(positions[5][1], decimals=2)) + " " +
            str(np.around(apt_stat.sum[6], decimals=0)) + " " + str(np.around(sky_stat.sum[6], decimals=0)) + " " +
            str(np.around(positions[6][0], decimals=2)) + " " + str(np.around(positions[6][1], decimals=2)) + "\n")

    if idx % 1000 == 0:
        Utils.log("Image completed. " + str(len(files)-(idx + 1)) + " files remain.", "info")
f.close()
