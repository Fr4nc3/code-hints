from yt.mods import *
from yt.analysis_modules.star_analysis.api import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api

yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"

import pymongo
import numpy as np
import sys

mongo = pymongo.Connection('127.0.0.1')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection = mongo_db['starsParticlesMore']

def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)


from yt.analysis_modules.halo_finding.halo_objects import RunFOF


data = [299, 300, 301, 302, 303, 304, 305, 306]


##################################################################################
#CENTER OF DENSEST CELL FOR EACH DATA
#COLLECTED FROM HALO FINDER 
##################################################################################
centerPlot = {}
centerPlot["299"] = [4.026331263e-01, 4.714540963e-01, 4.622243906e-01]
centerPlot["300"] = [4.027091436e-01, 4.714863511e-01, 4.621095851e-01]
centerPlot["301"] = [4.067627915e-01, 4.723197619e-01, 4.596178269e-01]
centerPlot["302"] = [4.028744583e-01, 4.715630154e-01, 4.618947428e-01]
centerPlot["303"] = [4.029489628e-01, 4.715991739e-01, 4.617865227e-01]

centerPlot["304"] = [4.030269645e-01, 4.716397766e-01, 4.616750455e-01]
centerPlot["305"] = [4.031041336e-01, 4.716763146e-01, 4.615712357e-01]
centerPlot["306"] = [4.031828656e-01, 4.717151386e-01, 4.614570797e-01]

for d in data:
    dataName = str(d)
    print dataName

    fn = "/astro/data/d0" + dataName + "/data0" + dataName + "/data0" + dataName # parameter file to load
    # Now we need a center of our volume to render.  Here we'll just use
    # center of our MW 
    c = centerPlot[dataName]
    pf = load(fn) # load data
    # Now we need a center of our volume to render.  Here we'll just use

    # Create a region that is a subset of the entire volume.
    #D is calculated by 
    #      0.25Mpc (250 kpc) divided by 35.714Mpc to convert to Box units 
    #box Units  = 25/h Mpc = 25/0.70 Mpc = 35.714 Mpc 

    D = 0.25 / 35.714 #0.25/35.714
    center = c
    left_corner = [center[0] - D, center[1] - D, center[2] - D]
    right_corner = [center[0] + D, center[1] + D, center[2] + D]
    sv = pf.h.region(center, left_corner, right_corner)

    haloes = HaloFinder(pf, subvolume=sv, dm_only=False)

    haloes.dump("MyHalosSubVol" + dataName)
    haloes.write_out("HopAnalysisSubVol" + dataName + ".out")
    haloes.write_particle_lists("HopAnalysisSubVol" + dataName + ".out")
    haloes.write_particle_lists_txt("HopAnalysisSubVol" + dataName + ".out")
    '''
    haloCount=0
    for halo in haloes:

        ct = halo["creation_time"]

        sm = halo["ParticleMassMsun"]
        metal = halo["metallicity_fraction"]
        # Select just the stars.
        stars = (ct > 0)
        #print stars
        ct = ct[stars]
        sm = sm[stars]
        metal = metal[stars]
        mx = (halo["particle_position_x"][stars] * sm).sum()/sm.sum()
        my = (halo["particle_position_y"][stars] * sm).sum()/sm.sum()
        mz = (halo["particle_position_z"][stars] * sm).sum()/sm.sum()
        #IF MX MY MZ ARE DEFINED INSERT TO DB
        if not np.isnan(mx) and not np.isnan(my) and not np.isnan(mz):
            print mx
            print my
            print mz
            print "enter"
            print dataName
            insert_id = mongo_collection.insert({
                'starParticle': haloCount,
                'data' : "d"+dataName,
                'dataNum' : dataName,
                'centerOfStarsParticles': {
                    'x': np.float64(mx),
                    'y': np.float64(my),
                    'z': np.float64(mz)
                }
            })
            haloCount = haloCount+1


        print haloCount
        print "--------\n\n"
    '''

