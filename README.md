**Description**: This script, developed by NREL, implements an inertia estimation algorithm using a sliding window approach.
    The inertia (H) is estimated based on frequency deviations and active power deviations, utilizing the swing
    equation from power system dynamics. An example application is provided using the WECC 240-bus system.
        
**Authors**:
    Jiangkai Peng, Jin Tan
    For more information, please contact: jin.tan@nrel.gov

**Disclaimer**: 
    This Opensource inertia estimation tool is developed based on ambient data from simulations of simplified WECC 240-bus system. 
    Application to  real-world power system data requires further modifications and calibrations based on the grid and operating conditions.
    This software is released under the NREL software record: **SWR-25-59**. 

**NOTICE**:
    Copyright © 2025 Alliance for Sustainable Energy, LLC
    Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    1. Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.
    
    2. Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.
    
    3. Neither the name of the copyright holder nor the names of its
       contributors may be used to endorse or promote products derived from
       this software without specific prior written permission.

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
