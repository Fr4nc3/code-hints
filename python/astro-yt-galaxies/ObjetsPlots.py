import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api
import sys


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

################################
# CONVERT CM^3 to KPC^3
################################
def _ConvertCellVolumeKpc(data):
       return data.convert("kpc")**3.0
 
#add_field("CellVolumeKpc", units=r"\rm{kpc}^3",
 #        function=_CellVolume,
  #       convert_function=_ConvertCellVolumeKpc)
#http://yt-project.org/doc/analyzing/creating_derived_fields.html?highlight=convert_function

#add_field("CellVolumeKpc", units=r"\rm{kpc}^3",function=_ConvertCellVolumeKpc, take_log=False)  
#add_field("RadialMassFlux", function=_RadialMassFlux, units=r"\rm{g}/\rm{cm}/\rm{s}", take_log=False)


for d in data:
    dataName      = str(d)
    print dataName
    

    fn = "/astro/data/d0"+dataName+"/data0"+ dataName +"/data0"+dataName # parameter file to load
    
    pf = load(fn, file_style="%s.grid.cpu%%04i") # load data
    
    c = centerPlot[dataName] 

    sphere = pf.h.sphere(c, (250., 'kpc')) # 250.
    
    levels = 8 #8
    mi, ma = sphere.quantities["Extrema"]("Density")[0]
    print "mi, ma =", mi, ma
    mi = 1.e-28   # this range was chosen from the level 0
    ma = 1.e-24   # map, by looking at colors of halo clouds
    print "mi, ma =", mi, ma 
    contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)
    
    print "contour values #" + str(len(contour_values))
    print "connected sets # " + str(len(connected_sets))
    
    #for i in connected_sets:
    for i in connected_sets:
        eb       =  connected_sets[i] 
        #print "level  " + str(i) + " clumsp # " + str(len(eb))
        for j in eb:
            obj = eb[j] 
            com = obj.quantities["CenterOfMass"]()
            #print com
            #['MinLocation', 'StarAngularMomentumVector', 'WeightedVariance', 'TotalMass', 'AngularMomentumVector', 'TotalQuantity', 'IsBound', 'WeightedAverageQuantity', 'CenterOfMass', 'BulkVelocity', 'ParticleSpinParameter', 'Action', 'Extrema', 'MaxLocation', 'BaryonSpinParameter']
            print dataName+" | "+str(i) + " | " + str(j) + " | " + str(obj.quantities["Extrema"]("Density")) +" | " + str(obj['Temperature']) + " | " + str(obj['Density']) + " | " + str(obj['CellMassMsun']) + " | " + str(obj['Metallicity'])
            
#            pc = PlotCollection(pf, com)
#            pc.add_profile_object(obj, ["Density", "Temperature"], weight="CellMassMsun", x_bins=15) # average T(rho)
#            #pc.add_profile_object(obj, ["Density", "CellVolumeKpc"], weight=None, x_bins=15) #
#            pc.add_profile_object(obj, ["Density", "CellVolume"], weight=None,  x_bins=15) #
#            pc.add_profile_object(obj, ["Density", "CellMassMsun"], weight=None,  x_bins=15) #
#            pc.add_profile_object(obj, ["Metallicity", "CellMassMsun"], weight=None,  x_bins=15) #
#            try:
#             
#              pc.save("new_plot_"+dataName+"_"+str(i)+"_" +str(j))
#            except Exception, e:
#               print e
#               continue
       
