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
