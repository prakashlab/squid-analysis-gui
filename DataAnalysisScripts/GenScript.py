#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:55:48 2019

@author: deepak
"""
import imp
import GravityMachineTrack 
imp.reload(GravityMachineTrack)
import numpy as np
import matplotlib.pyplot as plt





Tmin = 0
Tmax = 10

###

# orgDim in mm
track = GravityMachineTrack.gravMachineTrack(Tmin = Tmin, Tmax = Tmax, computeDisp = True, orgDim = 0.1, overwrite_piv=False, overwrite_velocity=True)

mean_vel_z = np.nanmean(track.Vz)
std_vel_z = np.nanstd(track.Vz)

plt.figure()
plt.plot(track.df['Time'], track.Vz, 'ro')
plt.show()

#Index = track.df.index
#
#Frames =np.array(['IMG_2135.tif', 'IMG_2160.tif', 'IMG_2186.tif'])
#
#indices = np.where(np.in1d(track.df['Image name'], Frames))[0]
##indices = 0
#
#print(indices)
#
#
#FM_smooth = track.smoothSignal(track.df['Focus Measure'],1)
#
#plt.figure()
#plt.plot(track.df['Time'],track.smoothSignal(track.df['Focus Measure'],1),'k-')
#plt.show()
#
#plt.figure()
#plt.plot(Index, FM_smooth,'g-')
#plt.scatter(Index[indices],FM_smooth[indices],50,color='r',alpha=0.5) 
#plt.show()
#
#for ii in range(track.trackLen):
#    print(track.df['Time'][ii], track.df['Image name'][ii])
    

# Plot the original velocity and the corrected velocity
plt.figure()

plt.plot(track.df['Time'], track.df['ZobjWheel'], 'ro')
plt.plot(track.df['Time'][track.imageIndex_array][:-1], track.Z_objFluid, 'b.')

plt.xlabel('Time (s)')
plt.ylabel('Z displacement (mm)')

# Plot the original velocity and the corrected velocity
plt.figure()

plt.plot(track.df['Time'], track.Vz, 'ro')
plt.plot(track.df['Time'][track.imageIndex_array], track.Vz_objFluid, 'b.')

plt.xlabel('Time (s)')
plt.ylabel('Z velocity (mm /s)')

