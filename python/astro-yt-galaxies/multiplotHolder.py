import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api
import sys
import matplotlib.pyplot as plt
import h5py
data = [299,300,301,302,303,304,305,306]



level     =   3




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



clump = {}
clump["B"] ={}
clump["C"] ={}
clump["D"] ={}
clump["E"] ={}
clump["F"] ={}
clump["G"] ={}


clump["B"]["299"] = -1
clump["B"]["300"] = 17
clump["B"]["301"] = 26
clump["B"]["302"] = 19
clump["B"]["303"] = 48
clump["B"]["304"] = 51
clump["B"]["305"] = 54
clump["B"]["306"] = 58


clump["C"]["299"] = 17
clump["C"]["300"] = 22
clump["C"]["301"] = 28
clump["C"]["302"] = 26
clump["C"]["303"] = 25
clump["C"]["304"] = 32
clump["C"]["305"] = 40
clump["C"]["306"] = 36


clump["D"]["299"] = -1
clump["D"]["300"] = -1
clump["D"]["301"] = 7
clump["D"]["302"] = 7
clump["D"]["303"] = 4
clump["D"]["304"] = 33
clump["D"]["305"] = 39
clump["D"]["306"] = 37




clump["E"]["299"] = 15
clump["E"]["300"] = 20
clump["E"]["301"] = 27
clump["E"]["302"] = 25
clump["E"]["303"] = 23
clump["E"]["304"] = 29
clump["E"]["305"] = -1
clump["E"]["306"] = -1



clump["F"]["299"] = -1
clump["F"]["300"] = 5
clump["F"]["301"] = 12
clump["F"]["302"] = 9
clump["F"]["303"] = 8
clump["F"]["304"] = 10
clump["F"]["305"] = 11
clump["F"]["306"] = 41




clump["G"]["299"] = -1
clump["G"]["300"] = -1
clump["G"]["301"] = -1
clump["G"]["302"] = -1
clump["G"]["303"] = 0
clump["G"]["304"] = 4
clump["G"]["305"] = 26
clump["G"]["306"] = 6


candidates = ["B","C","D","E","F","G"]
for d in data:
    dataName      = str(d)
    print dataName




    
f = h5py.File("profiles_2.h5", "w")  
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
    for can in candidates:
        print clump[can][dataName]
        candidate = clump[can][dataName]

        
        if candidate>-1:
            obj = connected_sets[level][candidate]
            com = obj.quantities["CenterOfMass"]()
        
            pc = PlotCollection(pf, com)
            p1 =  pc.add_profile_object(obj, ["Density", "Temperature"], weight="CellMassMsun", x_bins=15) # average T(rho)
            #p2 = pc.add_profile_object(obj, ["Density", "CellVolume"], weight=None,  x_bins=15) #
            p3 = pc.add_profile_object(obj, ["Density", "CellMassMsun"],  weight=None,  x_bins=15) #
            p4 = pc.add_profile_object(obj, ["Metallicity", "CellMassMsun"],  weight=None,  x_bins=15) #
            f.create_group("/DD04i" +dataName+ "_"+can)
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p1/Density", data=p1.data["Density"])
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p1/Temperature", data=p1.data["Temperature"])   
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p3/Density" , data=p3.data["Density"])
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p3/CellMassMsun", data=p3.data["CellMassMsun"])   
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p4/CellMassMsun" , data=p4.data["CellMassMsun"]) 
            f.create_dataset("/DD04i" +dataName+ "_"+can+"/p4/Metallicity", data=p4.data["Metallicity"])  
    
f.close()




