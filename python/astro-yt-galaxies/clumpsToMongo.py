from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
import matplotlib.pyplot as plt
import pymongo
import numpy as np
import math   # This will import math module
#import simplejson as json
import sys
from matplotlib.colors import LogNorm

mongo = pymongo.Connection('127.0.0.1')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection = mongo_db['levels_new_data1']
mongo_collection_cells = mongo_db['levels_new_data_cells1']

data = [299,300,301,302,303,304,305,306]
##################################################################################
#CENTER OF DENSEST CELL FOR EACH DATA
#COLLECTED FROM HALO FINDER
##################################################################################
centerPlot ={}
centerPlot["299"] = [4.026331263e-01 ,   4.714540963e-01 , 4.622243906e-01]
centerPlot["300"] = [4.027091436e-01 ,   4.714863511e-01 , 4.621095851e-01]
centerPlot["301"] = [4.067627915e-01 ,   4.723197619e-01 , 4.596178269e-01]
centerPlot["302"] = [4.028744583e-01 ,   4.715630154e-01 , 4.618947428e-01]
centerPlot["303"] = [4.029489628e-01 ,   4.715991739e-01 , 4.617865227e-01]

centerPlot["304"] = [4.030269645e-01 ,   4.716397766e-01 , 4.616750455e-01]
centerPlot["305"] = [4.031041336e-01 ,   4.716763146e-01 , 4.615712357e-01]
centerPlot["306"] = [4.031828656e-01 ,   4.717151386e-01 , 4.614570797e-01]





for d in data:
    dataName      = str(d)
    print dataName
    fn = "/astro/data/d0"+dataName+"/data0"+ dataName +"/data0"+dataName # parameter file to load

    pf = load(fn, file_style="%s.grid.cpu%%04i") # load data

    file_to_write = "data"+dataName+"_clumps_info.txt"
    c = centerPlot[dataName]

    sphere = pf.h.sphere(c, (250., 'kpc')) # 250.

    levels = 8 #8
    mi, ma = sphere.quantities["Extrema"]("Density")[0]

    print " from the sphere mi, ma =", mi, ma # they are not in use
    mi = 1.e-28   # this range was chosen from the level 0
    ma = 1.e-24   # map, by looking at colors of halo clouds

    print "mi, ma =", mi, ma
    contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)


    for j in connected_sets:
        lev2contours = connected_sets[j]
        for i in lev2contours:
            print "clump"
            print i
            eb       =  lev2contours[i]
            #print eb.quantities.keys()
            eb
            cen      = eb.quantities["CenterOfMass"]()
            totm     = eb.quantities["TotalQuantity"]("CellMassMsun")[0]
            #bound    = eb.quantities["IsBound"]() #removed because it takes too long
            bound = ""
            minl    = eb.quantities["MinLocation"]("Density")
            BulkVelocity    = eb.quantities["BulkVelocity"]()
            StarAngularMomentumVector = eb.quantities["StarAngularMomentumVector"]()
            StarAngularMomentumVector =  ""
            angularMomentumVector = eb.quantities["AngularMomentumVector"]()
            WeightedAverageQuantity    = eb.quantities["WeightedAverageQuantity"]("Temperature", "CellMassMsun")
            ParticleSpinParameter = eb.quantities["ParticleSpinParameter"]()
            maxl = eb.quantities["MaxLocation"]("Density")
            BaryonSpinParameter = eb.quantities["BaryonSpinParameter"]()
            Extrema =eb.quantities["Extrema"]("Density")
            print "metalicity len"
            print len(eb["Metallicity"])

            print "Density len"
            print len(eb["Density"])
            print eb["Density"] * eb["Temperature"]
            print "\n"
            # for k in range(0, len(eb["Density"])-1):

            print "len density"
            print len(eb["Density"])
            print "\n"
            print "len temp"
            print len (eb["Temperature"])
            print eb["Temperature"]
            print "\n"
            print "len cell"
            print eb["CellMassMsun"]


            y =  eb["Density"] * eb["CellVolume"]

            x = eb["Density"]
            print dataName
            print type(y)
            print type(x)
            temp_array = eb["Temperature"]
            density_array = x
            cellvolume_array = eb["CellVolume"]
             #CellMassMsum = eb["CellMassMsun"]
            if(len(x)==len(y)):
                insert_id = mongo_collection.insert({
                                    'level': j,
                                    'clump': i,
                                    'dataName' : dataName,
                                    'dataNumb' : d,
                                    'array_len':len(eb["Density"])

                                    })
                count_cells = 0
                for p in range(len(temp_array)):
                    insert_id = mongo_collection_cells.insert({
                                    'level': j,
                                    'clump': i,
                                    'dataName' : dataName,
                                    'dataNumb' : d,
                                    'id_c': count_cells,
                                    'temp':temp_array[p],
                                    'density':density_array[p],
                                    'cellvol':cellvolume_array[p],
                                    'cellmassum':y[p]
                     })
                    count_cells += 1




            else:
                print "x:"+ str(len(x)) + "y :" + str(len(y))




print "ended.\n"