import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api
import sys
import matplotlib.pyplot as plt
import h5py
data = [299,300,301,302,303,304,305,306]
candidates = ["B","C","D","E","F","G"]


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


can  = sys.argv[1]
print "candidates"+ can 
###################################
#Density vs CellMassSum
f = h5py.File("profiles_2.h5", "r")
import pylab
pylab.clf()


for d in data:
    dataName      = str(d)
    print dataName
    print clump[can][dataName]
    candidate = clump[can][dataName]
    if candidate>-1:
        linewidth=1
        if(dataName=="306"):
           linewidth=2
        pylab.loglog(f["/DD04i" +dataName+ "_"+can+"/p3/Density"], f["/DD04i" +dataName+ "_"+can+"/p3/CellMassMsun"], '-', label=d,linewidth=linewidth)
plt.legend(loc='upper left')
plt.ylabel('CellMassMsun  ($M_{\odot}$)')
plt.xlabel("Density g/cm^3")
plt.title("level 3 Candidate " + can)
plt.savefig("out_density_vs_CellMassMsun_"+can +".png")



f = h5py.File("profiles_2.h5", "r")
import pylab
pylab.clf()

for d in data:
    dataName      = str(d)
    print dataName
    candidate = clump[can][dataName]
    linewidth=1
    if candidate>-1:
        if(dataName=="306"):
           linewidth=2
        pylab.loglog(f["/DD04i" +dataName+ "_"+can+"/p1/Density"], f["/DD04i" +dataName+ "_"+can+"/p1/Temperature"], '-', label=d,linewidth=linewidth)
plt.legend(loc='upper right')
plt.ylabel('Temperature(K)')
plt.xlabel('Density g/cm^3')
plt.title("level 3 Candidate " + can)
plt.axis([1.e-27, 1.e-24,8e3, 4e5])
plt.savefig("out_density_vs_Temperature_"+can +".png")







f = h5py.File("profiles_2.h5", "r")
import pylab
pylab.clf()
for d in data:
    dataName      = str(d)
    print dataName
    linewidth=1
    candidate = clump[can][dataName]
    if candidate>-1:
        if(dataName=="306"):
           linewidth=2
        pylab.loglog(f["/DD04i" +dataName+ "_"+can+"/p4/Metallicity" ], f["/DD04i" +dataName+ "_"+can+"/p4/CellMassMsun" ], '-', label=d,linewidth=linewidth)
plt.legend(loc='upper left')
plt.ylabel('CellMassMsun ($M_{\odot}$)')
plt.xlabel('Metallicity  ($Z_{\odot}$)')
plt.title("level 3 Candidate " + can)
plt.axis([1.e-2, 1.e0,1000, 100000000])
plt.savefig("out_Metallicity_vs_CellMassMsun_"+can +".png")
