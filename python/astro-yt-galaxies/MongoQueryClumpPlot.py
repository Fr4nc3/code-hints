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
from datetime import datetime



mongo = pymongo.Connection('127.0.0.1')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection_cells = mongo_db['levels_new_data_cells1']

# DATA CELL STRUCTURE
# {
#     "_id" : ObjectId("53f28f385778bb0bd1d3b4b0"),
#     "dataName" : "299",
#     "dataNumb" : 299,
#     "cellmassum" : 2.877355428603579e+37,
#     "temp" : 415983.65625,
#     "level" : 0,
#     "cellvol" : 2.816468569311119e+65,
#     "id_c" : 4,
#     "density" : 1.021618156849289e-28,
#     "clump" : 1
# }
#Level 3 Candidate Name C
# clump["C"]["299"] = 17
# clump["C"]["300"] = 22
# clump["C"]["301"] = 28
# clump["C"]["302"] = 26
# clump["C"]["303"] = 25
# clump["C"]["304"] = 32
# clump["C"]["305"] = 40
# clump["C"]["306"] = 36

tstart = datetime.now()
level = 3
dataNumb = 306
clump1 = 36

clump = mongo_collection_cells.find({
    'dataNumb' : dataNumb,
    'level':level,
    'clump':clump1

}).sort('id_c',1)

if  clump.count() > 0:
    temp = []
    cellvol = []
    density = []
    y=[]


    for this in clump:
        temp.append(this['temp'])
        cellvol.append(this['cellvol'])
        density.append(this['density'])
        y.append(this['cellvol']*this['density'])


    #y = density * cellvol
    x = density
    print x
    print y
    print type(y)
    print type(x)
    if(len(x)==len(y)):
       # bins = [-28.0,-27.75,-27.5,-27.25,-27.0,-26.75,-26.5,-26.25,-26.0,-25.75,-25.5,-25.25,-24.0]

        n, bins, patches = plt.hist(np.log10(x), bins=35, weights=np.log10(y), histtype='barstacked', normed=0, facecolor='green', alpha=0.5)
        plt.ylabel('CellMassMsum')
        plt.ylim(0,2500)
        plt.xlabel("Density clump " + str(clump1) + " data " + str(dataNumb)+ " level "+str(level))
        plt.savefig("plots/single_plot_Density_clump_" + str(clump1) + "_data_" + str(dataNumb) + "_level_" +str(level))

tend = datetime.now()
print tend - tstart
print "ended.\n"