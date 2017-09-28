from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
import sys
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"

    

data = [299,300,301,302,303,304,305,306]


for d in data:
    dataName      = str(d)
    print dataName
    fn = "/astro/data/d0"+dataName+"/data0"+ dataName +"/data0"+dataName # parameter file to load

    pf = load(fn, file_style="%s.grid.cpu%%04i") # load data

    halo_list = HaloFinder(pf)
    halo_list.write_out("final_HaloFinder_"+dataName+"_HopAnalysis.txt")
