#!/usr/bin/env python
# Wenchang Yang (wenchang@princeton.edu)
# Tue Oct 30 22:06:48 EDT 2018
import os, os.path, sys, glob

#model = 'FLOR'
#expname = 'CTL1860_tiger3_intelmpi_24_1116PE'
#model = 'AM2.5C360'
#expname = 'CTL1990s_tiger3_intelmpi_24_2430PE'
model = 'CM2.1'
expname = 'CTL1860_tiger3_intelmpi_24_60PE'
#extend_year = 202411
#for ii in range(1,6):
if True:
    #workdir = f'/home/wenchang/{model}/work/amipHadISSTlongChancorr_tiger3_intelmpi_24_1440PE_extend{extend_year}_e{ii}'
    #modelout_dir = f'/tigress/wenchang/MODEL_OUT/{model}/tiger3/amipHadISSTlongChancorr_tiger3_intelmpi_24_1440PE_extend{extend_year}/en{ii:02d}'
    workdir = f'/home/wenchang/{model}/work/{expname}'
    #modelout_dir = f'/projects/GEOCLIM/wenchang/MODEL_OUT2/{model}/{expname}'
    modelout_dir = f'/projects/GEOCLIM/wenchang/MODEL_OUT/{model}/tiger3/{expname}'
    
    # POSTP
    ifiles = glob.glob(f'{workdir}/POSTP/*.nc')
    ifiles.sort()
    for ifile in ifiles:
        basename = os.path.basename(ifile)
        ofile = os.path.join(modelout_dir, 'POSTP', basename)
        if os.path.exists(ofile):
            print('[POSTP Copied]:', ofile)
            os.remove(ifile)
            print('[POSTP Removed]:', ifile)
        else:
            print('\t[POSTP Kept]:', ifile)
            
    # HISTORY 
    ifiles = glob.glob(f'{workdir}/HISTORY/*.nc')
    ifiles.sort()
    for ifile in ifiles:
        basename = os.path.basename(ifile)
        if not glob.glob(f'{workdir}/POSTP/{basename.split(".")[0]}.*.nc'): # the data in POSTP of the same year has been removed
            os.remove(ifile)
            print('[HISTORY Removed]:', ifile)
        else:
            print('\t[HISTORY Kept]:', ifile)
    
    # RESTART
    ifiles = glob.glob(f'{workdir}/RESTART/*.tar')
    ifiles.sort()
    for ifile in ifiles:
        basename = os.path.basename(ifile)
        ofile = os.path.join(modelout_dir, 'RESTART', basename)
        if os.path.exists(ofile):
            print('[RESTART Copied]:', ofile)
            os.remove(ifile)
            print('[RESTART Removed]:', ifile)
        else:
            print('\t[RESTART Kept]:', ifile)
