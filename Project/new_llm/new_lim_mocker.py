#!/usr/bin/env python
from __future__           import division
import numpy              as np
import matplotlib.pylab   as plt
import scipy              as sp
import limlam_mocker      as llm
#Get Parameters for run
import new_params         as params

lbound  = 10 #exponent
ubound  = 12 #exponent

min_masses = 3*np.logspace(lbound, ubound, params.N)


llm.debug.verbose = True
llm.write_time('Starting Line Intensity Mapper')

mapinst      = [[] for i in range(params.N)]

halos        = [[] for i in range(params.N)]
cosmo        = [[] for i in range(params.N)]

k            = [[] for i in range(params.N)]
Pk           = [[] for i in range(params.N)]
Nmodes       = [[] for i in range(params.N)]
Pk_sampleerr = [[] for i in range(params.N)]

for i in range(params.N):

    ### Setup maps to output
    mapinst[i] = llm.params_to_mapinst(params, params.map_output_file[i]);

    ### Load halos from catalogue
    halos[i], cosmo[i] = llm.load_peakpatch_catalogue(params.halo_catalogue_file)
    halos[i]           = llm.cull_peakpatch_catalogue(halos[i], min_masses[i], mapinst[i])

    ### Calculate Luminosity of each halo
    halos[i].Lco    = llm.Mhalo_to_Lco(halos[i], params.model, params.coeffs) # not sure on this one

    ### Bin halo luminosities into map
    mapinst[i].maps = llm.Lco_to_map(halos[i], mapinst[i]) # same here

    ### Output map to file
    llm.save_maps(mapinst[i])

    ### Calculate power spectrum
    k[i], Pk[i], Nmodes[i] = llm.map_to_pspec(mapinst[i], cosmo[i])
    Pk_sampleerr[i] = Pk[i]/np.sqrt(Nmodes[i])

    ### Plot results
    # llm.plot_results(mapinst[i], k[i], Pk[i], Pk_sampleerr[i], params)



llm.write_time('Finished Line Intensity Mapper')
