from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
import pymongo
import numpy as np
import math   # This will import math module
#import simplejson as json
import sys



def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)


distance  =  250 #int(sys.argv[1])
level     =   "5" #sys.argv[2]


#distance 250 kpc
#level 5
print distance
print level

data = [299,300,301,302,303,304,305,306]

dimensionArray = [0,1,2]
for d in data:
    dataName      = str(d)
    for dm in dimensionArray:
        dimension     = dm
        fn = "/astro/data/d0"+dataName+"/data0"+ dataName +"/data0"+dataName # parameter file to load

        mongo = pymongo.Connection('127.0.0.1')
        # Returns Database Object
        mongo_db = mongo['astro']
        level_collection = mongo_db['levels']
        starParticles_collection  = mongo_db['starsParticles']

        clumps = level_collection.find({'local':"d"+dataName, 'level':level})
        stars = starParticles_collection.find({'data':"d"+dataName})


        pf = load(fn) # load data

        p = ProjectionPlot(pf,dimension ,'Density','max',(distance,'kpc'))
        p.set_zlim('Density',  5.e-5, 5.e-2)

        #get the clumps for the defined level and add them to the plot
        colorDic = dict(color='white')
        if clumps.count() > 0:
            for this_clump in clumps:
                centerOfMass=(np.float64(this_clump['centerOfMass']['x']),np.float64(this_clump['centerOfMass']['y']),np.float64(this_clump['centerOfMass']['z']))
                p.annotate_point(centerOfMass, "c"+this_clump['clump'],text_args=colorDic)
                p.annotate_marker(centerOfMass, "x",plot_args=colorDic)

        #get te star particles center of mass and add them to the plot
        colorDic = dict(color='green')
        if stars.count() > 0:
            for this_star in stars:
                centerOfMass=(np.float64(this_star['centerOfStarsParticles']['x']),np.float64(this_star['centerOfStarsParticles']['y']),np.float64(this_star['centerOfStarsParticles']['z']))
                p.annotate_point(centerOfMass, "s" + str(this_star['starParticle']) ,text_args=colorDic)
                p.annotate_marker(centerOfMass, "*",plot_args=colorDic)

        p.save("plot_"+dataName+"_"+level)