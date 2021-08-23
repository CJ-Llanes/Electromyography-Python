import matplotlib.pyplot as plt
import numpy as np

import scipy as sp
from scipy import signal


#---------declaracion de funciones----------------
def band_pass_filter(F_low, F_high, Fs, emg):
    high = F_low/(Fs/2)
    low = F_high/(Fs/2)
    b, a = sp.signal.butter(4, [high,low], btype='bandpass')

    # process EMG signal: filter EMG
    emg_filtered = sp.signal.filtfilt(b, a, emg)
    return emg_filtered

#-------------------------------------------------

def envelope(emg, F_low, Fs):
    emg_rectified = abs(emg)
    low_pass = F_low/Fs
    b2, a2 = sp.signal.butter(4, low_pass, btype='lowpass')
    emg_envelope = sp.signal.filtfilt(b2, a2, emg_rectified)      
    return emg_envelope

#--------------------------------------------------

#---------EMG---features---------------------------
#-----------MAV------------------------------------
def MAV(emg):
    MAV = 0
    MAV = np.sum(abs(emg))/len(emg)
    return MAV
#--------------------------------------------------
#------------------WL------------------------------
def WL(emg):
    WL = np.sum(abs(np.ediff1d(emg)))
    return WL

#--------------------------------------------------
#-------------RMS----------------------------------
def RMS(emg):
    rms = np.sqrt(np.mean(emg**2))
    return rms


#-------normalizar-------------------------
def normalization_mean_std(dato, media, desv):
    norm = (dato - media)/desv
    return norm

