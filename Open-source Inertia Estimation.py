# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7  2025

Authors:
    Jiangkai Peng, Jin Tan
    For more information, please contact: jin.tan@nrel.gov

Description:
    This script, developed by NREL, implements an inertia estimation algorithm using a sliding window approach.
    The inertia (H) is estimated based on frequency deviations and active power deviations, utilizing the swing
    equation from power system dynamics. An example application is provided using the WECC 240-bus system,
    as described in the following reference:

        H. Yuan, R. S. Biswas, J. Tan, and Y. Zhang,
        "Developing a Reduced 240-Bus WECC Dynamic Model for Frequency Response Study of High Renewable Integration,"
        2020 IEEE/PES Transmission and Distribution Conference and Exposition (T&D), Chicago, IL, USA, 2020, pp. 1-5,
        doi: 10.1109/TD39804.2020.9299666.

Dependencies:
    - io (Standard Library): For handling byte streams (useful when reading data from network responses).
    - pandas: For data manipulation and analysis (e.g., reading CSV files).
    - requests: For making HTTP requests (e.g., connecting to a PDC server for live data).
    - numpy: For numerical operations and array handling, including polynomial fitting.
    - matplotlib: For plotting data and visualizing results.
Disclaimer: 
    This Opensource inertia estimation tool is developed based on ambient data from simulations of simplified WECC 240-bus system. 
    Application to  real-world power system data requires further modifications and calibrations based on the grid and operating conditions.
    This software is released under the NREL software record: SWR-25-59. You may freely use, modify, and distribute this software in accordance with the terms of the license.

NOTICE:
    Copyright © 2025 Alliance for Sustainable Energy, LLC
    These data were produced by the Alliance for Sustainable Energy, LLC (Contractor) under Contract No. DE-AC36-08GO28308 with
    the U.S. Department of Energy (DOE).
    During the period of commercialization or such other time period specified by the DOE, the Government is granted for itself
    and others acting on its behalf a nonexclusive, paid-up, irrevocable worldwide license in this data to reproduce, prepare
    derivative works, and perform publicly and display publicly, by or on behalf of the Government.
    Subsequent to that period the Government is granted for itself and others acting on its behalf a nonexclusive, paid-up,
    irrevocable worldwide license in this data to reproduce, prepare derivative works, distribute copies to the public,
    perform publicly and display publicly, and to permit others to do so.
    The specific term of the license can be identified by inquiry made to the Contractor or DOE.
    NEITHER CONTRACTOR, THE UNITED STATES, NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR ANY OF THEIR EMPLOYEES,
    MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,
    COMPLETENESS, OR USEFULNESS OF ANY DATA, APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE
    WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS.


"""
import io
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')


def inertia_est_open_source(frequency_dev, power_dev, dt=1/120, window_size=0.3, step_size=0.1):
    """
    Estimate the equivalent inertia H using a sliding window approach.

    The algorithm divides the time-series data into overlapping windows. For each window,
    a linear regression (first-order polynomial fit) is applied to the frequency deviation
    data to estimate the rate of change of frequency (ROCOF). Then, using the swing equation,
    an equivalent inertia H is estimated with the formula:

        ROCOF = DeltaP / (2 * H)   =>   H = DeltaP / (2 * ROCOF)

    Parameters:
      frequency_dev : array-like
          The COI frequency deviation of one area.
      power_dev : array-like
          The average active power deviation of one area.
      dt : float
          Sample time interval (seconds).
      window_size : float
          Length of the sliding window in seconds (default: 0.3 s).
      step_size : float
          Step (shift) in seconds between consecutive windows (default: 0.1 s).

    Returns:
      t_centers : np.ndarray
          Array of center times for each sliding window.
      H_est : np.ndarray
          Array of estimated equivalent inertia values for each window.
    """
    # Create a time vector matching the input data length
    n_points = len(frequency_dev)
    t = np.arange(0, n_points * dt, dt)
    if len(t) > n_points:
        t = t[:n_points]

    # Convert window size and step size from seconds to number of samples
    window_samples = int(window_size / dt)
    step_samples = int(step_size / dt)

    t_centers = []
    H_est = []
    # Loop over the time series using a sliding window
    for start in range(0, n_points - window_samples + 1, step_samples):
        end = start + window_samples
        t_window = t[start:end]
        f_window = frequency_dev[start:end]
        p_window = power_dev[start:end]

        # Estimate ROCOF (frequency derivative) by fitting a straight line to the frequency data.
        # The slope of the line is the ROCOF.
        try:
            slope, intercept = np.polyfit(t_window, f_window, 1)
        except Exception as e:
            print(f"Polyfit failed for window starting at t = {t[start]:.2f} s: {e}")
            slope = np.nan

        # Define Delta P for the window.
        P_delta = -np.mean(p_window)

        # Compute inertia H from the swing equation relation:
        #   ROCOF = DeltaP/(2*H)  ->  H = DeltaP/(2*ROCOF)
        if np.abs(slope) < 2e-4 or slope*P_delta<0:
            H_val = np.nan  # Avoid division by zero and negative estimations
        else:
            H_val = P_delta / (2 * slope)

        # Save the center time of this window and the corresponding H estimate.
        t_centers.append(t_window[0] + window_size / 2)
        H_est.append(H_val)
        
    return np.array(t_centers), np.array(H_est)

# **************************************** Connect to PDC server  ************************************
# The following block of code (currently commented out) demonstrates how to connect to a PDC 
# server to retrieve live data. Adjust the URL and PORT as needed, and uncomment if real-time data is available.
#
# PORT = 8080  # Port where the Server is bound
# url = f"http://127.0.0.1:{PORT}/data"
# s = requests.get(url, timeout=10)  # Send a GET request with a 10-second timeout
# Data = pd.read_feather(io.BytesIO(requests.get(url, timeout=10).content))


# **************************************** Mock Data ************************************
# For demonstration purposes, we use mock data by reading from CSV files: 'Data_CA1.csv', 'Data_AZ.csv', 'Data_OR.csv'.
# This CSV file should contain at least three columns: 'Time', 'Frequency_dev', and 'Power_dev'.

df = pd.read_csv('Data_OR.csv') 

t = np.array(df['Time'])
f = np.array(df['Frequency_dev']) # Frequency deviation in Hz
P = np.array(df['Power_dev'])*100 # Active power deviation in MW

# Create a matplotlib figure with two subplots arranged vertically.
fig, axs = plt.subplots(2, 1)
# ------------------------ Plot Active Power ------------------------
axs[0].plot(t, P)
axs[0].set_title('Active Power (MW)')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Power (MW)')
axs[0].grid()
# ------------------------ Plot Frequency ------------------------
axs[1].plot(t, f*60)
axs[1].set_title('Frequency (Hz)')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Frequency (Hz)')
axs[1].grid()

# Adjust spacing and show the plot
plt.tight_layout()
plt.show()


# **************************************** Inertia Estimation ************************************
dt = 1/120 # Define the sampling time interval
t_centers, H_est = inertia_est_open_source(f, P, dt) # Call the inertia estimation function with the frequency and power deviation data.
H_av = np.nanmean(H_est) # Calculate the average inertia value across all windows, ignoring any NaN values that may have occurred.
print('Average inertia: ', np.nanmean(H_est)) # Print the average estimated inertia to the console.

