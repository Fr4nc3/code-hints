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


data = [299]#,300,301,302,303,304,305,306]
##################################################################################
#CENTER OF DENSEST CELL FOR EACH DATA
#COLLECTED FROM HALO FINDER
##################################################################################
centerPlot ={}
centerPlot["299"] = [4.026331263e-01 ,   4.714540963e-01 , 4.622243906e-01]
# centerPlot["300"] = [4.027091436e-01 ,   4.714863511e-01 , 4.621095851e-01]
# centerPlot["301"] = [4.067627915e-01 ,   4.723197619e-01 , 4.596178269e-01]
# centerPlot["302"] = [4.028744583e-01 ,   4.715630154e-01 , 4.618947428e-01]
# centerPlot["303"] = [4.029489628e-01 ,   4.715991739e-01 , 4.617865227e-01]
#
# centerPlot["304"] = [4.030269645e-01 ,   4.716397766e-01 , 4.616750455e-01]
# centerPlot["305"] = [4.031041336e-01 ,   4.716763146e-01 , 4.615712357e-01]
# centerPlot["306"] = [4.031828656e-01 ,   4.717151386e-01 , 4.614570797e-01]






#define a moving average function
def moving_average(x,y,step_size=.1,bin_size=1):
    bin_centers  = np.arange(np.min(x),np.max(x)-0.5*step_size,step_size)+0.5*step_size
    bin_avg = np.zeros(len(bin_centers))

    for index in range(0,len(bin_centers)):
        bin_center = bin_centers[index]
        items_in_bin = y[(x>(bin_center-bin_size*0.5) ) & (x<(bin_center+bin_size*0.5))]
        bin_avg[index] = np.mean(items_in_bin)

    return bin_centers,bin_avg





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

    lev2contours = connected_sets[4]
    eb  =lev2contours[27]

    y =  eb["Density"] * eb["CellVolume"]
    x = eb["Density"]
    bins = [-28.0,-27.75,-27.5,-27.25,-27.0,-26.75,-26.5,-26.25,-26.0,-25.75,-25.5,-25.25,-24.0]
    n, bins, patches = plt.hist(np.log10(x), bins=bins, weights=np.log10(y), histtype='barstacked', normed=0, facecolor='green', alpha=0.5)
    plt.ylabel('CellMassMsum')
    plt.xlabel('Density')

    plt.savefig("plots/"+dataName +"_clump_test_hist_density_ranges")
    exit()
    for j in connected_sets:
        lev2contours = connected_sets[j]
        for i in lev2contours:
            print "clump"
            print i
            eb       =  lev2contours[i]
            # #print eb.quantities.keys()
            # eb
            # cen      = eb.quantities["CenterOfMass"]()
            # totm     = eb.quantities["TotalQuantity"]("CellMassMsun")[0]
            # #bound    = eb.quantities["IsBound"]() #removed because it takes too long
            # bound = ""
            # minl    = eb.quantities["MinLocation"]("Density")
            # BulkVelocity    = eb.quantities["BulkVelocity"]()
            # StarAngularMomentumVector = eb.quantities["StarAngularMomentumVector"]()
            # StarAngularMomentumVector =  ""
            # angularMomentumVector = eb.quantities["AngularMomentumVector"]()
            # WeightedAverageQuantity    = eb.quantities["WeightedAverageQuantity"]("Temperature", "CellMassMsun")
            # ParticleSpinParameter = eb.quantities["ParticleSpinParameter"]()
            # maxl = eb.quantities["MaxLocation"]("Density")
            # BaryonSpinParameter = eb.quantities["BaryonSpinParameter"]()
            # Extrema =eb.quantities["Extrema"]("Density")
            # print "metalicity len"
            # print len(eb["Metallicity"])
            #
            # print "Density len"
            # print len(eb["Density"])
            # print eb["Density"] * eb["Temperature"]
            # print "\n"
            # # for k in range(0, len(eb["Density"])-1):
            # #     print "density x temperature::"
            # #     print eb["Density"][k] * eb["Temperature"][k]
            # #     print "\n\n"
            # print eb["Metallicity"].sum()/len(eb["Metallicity"])
            # print eb["Density"].sum()/len(eb["Density"])
            # print eb["Temperature"].sum()/len(eb["Temperature"])
            #plot the data
            # print "len density"
            # print len(eb["Density"])
            # print "\n"
            # print "len temp"
            # print len (eb["Temperature"])
            # print eb["Temperature"]
            # print "\n"
            # print "len cell"
            # print eb["CellMassMsum"]
            # print  eb.quantities["TotalQuantity"]("CellMassMsun"))
            # print len(eb.quantities["TotalQuantity"]("CellMassMsun")[0]))
            #
            # print "\n\n\n"

            y =  eb["Density"] * eb["CellVolume"]

            x = eb["Density"]

            print type(y)
            print type(x)
            if(len(x)==len(y)):
                #num_bins=int(2*math.pow(len(x),(1.0/3.0))) # the square root of the number of data points in the sample (used by Excel histograms and many others).
                delta=x.min()-x.max()
                print delta
                delta = abs(delta)/4.0
                # num_bins = []
                # num_bins.append(x.min())
                # num_bins.append(x.min()+(delta*1))
                # num_bins.append(x.min()+(delta*2))
                # num_bins.append(x.min()+(delta*3))
                # num_bins.append(x.min()+(delta*4))
                # num_bins.append(x.max())
                #
                # print "num_bins"
                # print(num_bins)
                bins = -28.0 * arange(13)*0.25 #[-28.0,-27.75,-27.5,-27.25,-27.0,-26.75,-26.5,-26.25,-26.0,-25.75,-25.5,-25.25,-24.0]
                n, bins, patches = plt.hist(np.log10(x), bins=bins, weights=np.log10(y), histtype='barstacked', normed=0, facecolor='green', alpha=0.5)

                #plt.hist2d(np.log10(x), np.log10(x),  weights=np.log10(y), bins=bins, norm=LogNorm())
                #plt.colorbar()
                #plt.loglog(x,y, color='purple', linestyle='-')
                plt.ylabel('CellMassMsum')
                plt.xlabel('Density')
                #plt.gca().set_xscale("log")
                plt.savefig("plots/"+dataName +"_clump_"+ str(i)+"_level_"+str(j)+ "_hist_density_ranges")
            else:
                print "x:"+ str(len(x)) + "y :" + str(len(y))




print "ended.\n"