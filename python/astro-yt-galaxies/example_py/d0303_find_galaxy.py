from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *


fn = "/astro/data/d0303/data0303/data0303" # parameter file to load

#RefineRegionLeftEdge   = 0.347627 0.429308 0.436357
#RefineRegionRightEdge  = 0.436006 0.511214 0.52262

pf = load(fn) # load data
# Now we need a center of our volume to render.  Here we'll just use
# center of our MW 

'''
halo_list = HaloFinder(pf)
halo_list.write_out("d0303_HopAnalysis.txt")
'''

file_to_write = '/tmp/d0303_clumps_out1_test.txt' 
c = [4.029489628e-01 ,   4.715991739e-01  ,  4.617865227e-01] # densest cell coord.


sphere = pf.h.sphere(c, (250., 'kpc')) # 250.

levels = 8 #8
mi, ma = sphere.quantities["Extrema"]("Density")[0]

print "mi, ma =", mi, ma
mi = 1.e-28   # this range was chosen from the level 0
ma = 1.e-24   # map, by looking at colors of halo clouds

print "mi, ma =", mi, ma
contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)


lev2contours = connected_sets

f = open(file_to_write, 'a+b')
header_line = ' level | clump | centerOfMass | totalMass  | BulkVelocity  | MinLocation | StarAngularMomentumVector | angularMomentumVector | IsBound | WeightedAverageQuantity |  ParticleSpinParameterAction | MaxLocation | BaryonSpinParameter | Extrema \n'
f.write(header_line)
print header_line

for j in connected_sets:
    lev2contours = connected_sets[j]
    for i in lev2contours:
        eb       =  lev2contours[i]
        #print eb.quantities.keys()
        cen      = eb.quantities["CenterOfMass"]()
        totm     = eb.quantities["TotalQuantity"]("CellMassMsun")[0]
        #bound    = eb.quantities["IsBound"]()
        bound = ""
        minl    = eb.quantities["MinLocation"]("Density")
        BulkVelocity    = eb.quantities["BulkVelocity"]()
        StarAngularMomentumVector = eb.quantities["StarAngularMomentumVector"]()
        StarAngularMomentumVector =  ""
        angularMomentumVector = eb.quantities["AngularMomentumVector"]()
        WeightedAverageQuantity    = eb.quantities["WeightedAverageQuantity"]("Temperature", "CellMassMsun")
        ParticleSpinParameter = eb.quantities["ParticleSpinParameter"]()
        maxl = eb.quantities["MaxLocation"]("Density") #ask Ryan
        BaryonSpinParameter = eb.quantities["BaryonSpinParameter"]()
        Extrema =eb.quantities["Extrema"]("Density")
        data_feed =j,'  | '  , i , '  | '   , cen ,'  | '  , totm ,'  | '  , BulkVelocity,'  | '  , minl, '  | ' ,StarAngularMomentumVector, '  | ' , angularMomentumVector, '  | ' , bound, '  | ' , WeightedAverageQuantity, '  | ' , ParticleSpinParameter, '  | ' ,  maxl, '  | ' , BaryonSpinParameter, '  | ' , Extrema, "\n"
        print data_feed
#print j, ' ', i, ' ', cen, ' ', totm, ' ',
# f.write(data_feed)


f.close()
open(file_to_write, 'rb').read()


print "ended.\n"