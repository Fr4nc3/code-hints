import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api
import sys

dataName  = sys.argv[1]

fn = "/astro/data/d0"+dataName+"/data0"+ dataName +"/data0"+dataName # parameter file to load

pf = load(fn, file_style="%s.grid.cpu%%04i") # load data


centerPlot ={}
centerPlot["299"] = [0.3918165,0.470261,0.4794885]

centerPlot["300"] = [0.40328598,0.47176743,0.46131516]

centerPlot["301"] = [0.3918165,0.470261,0.4794885]   
centerPlot["302"] = [4.028744583e-01 ,   4.715630154e-01 ,   4.618947428e-01]   
centerPlot["303"] = [4.029489628e-01 ,   4.715991739e-01  ,  4.617865227e-01]
centerPlot["304"] = [4.030269645e-01 ,   4.716397766e-01  ,  4.616750455e-01]   
centerPlot["305"] = [4.031041336e-01  ,  4.716763146e-01  ,  4.615712357e-01]   
centerPlot["306"] = [4.031828656e-01  ,  4.717151386e-01  ,  4.614570797e-01]  
c = centerPlot[dataName] 

sphere = pf.h.sphere(c, (250., 'kpc')) # 250.

levels = 8 #8
mi, ma = sphere.quantities["Extrema"]("Density")[0]
print "mi, ma =", mi, ma

contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)

print "contour values #" + str(len(contour_values))
print "connected sets # " + str(len(connected_sets))

#for i in connected_sets:
for i in connected_sets:
    eb       =  connected_sets[i] 
    print "level  " + str(i) + " clmsp# " + str(len(eb))
    for j in eb:
        obj = eb[j] 
        com = obj.quantities["CenterOfMass"]()
        print com
        pc = PlotCollection(pf, com)
        pc.add_profile_object(obj, ["Density", "Temperature"],weight="CellMassMsun") # average T(rho)
        pc.add_profile_object(obj, ["Density", "CellVolume"], weight=None) #
        pc.add_profile_object(obj, ["Density", "CellMassMsun"], weight=None) #
        try:
          pc.save("sliceplot_"+dataName+"_"+str(i)+"_" +str(j))
        except Exception, e:
           print e
           continue
   
