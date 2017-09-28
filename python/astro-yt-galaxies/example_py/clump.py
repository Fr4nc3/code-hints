import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api


# Follow the simple_volume_rendering cookbook for the first part of this.
#fn = "~/work/enzo/data/cosmo/L25t128m4r10ps5-MW4/r0058/redshift0058" # parameter file to load
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

#fn = "/astro/yt-dev/yt-x86_64/src/yt-hg/tests/DD0010/moving7_0010"
pf = load(fn, file_style="%s.grid.cpu%%04i") # load data

#pf = load(fn) # load data
file_to_write = '/tmp/redshift0058_clumps_out1_test.txt' 
c = [0.40328598, 0.47176743, 0.46131516] # densest cell coord.

#sphere = halos[0].get_sphere()
sphere = pf.h.sphere(c, (50., 'kpc')) # 250.

levels = 8 #8
mi, ma = sphere.quantities["Extrema"]("Density")[0]

mi = 1.e-28   # this range was chosen from the level 0
ma = 1.e-24   # map, by looking at colors of halo clouds

print "mi, ma =", mi, ma
contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)

L = na.array([0.90798282, 0., 0.41900739]) # orthogonal to the angular momentum vector
W = 0.01 / pf["unitary"]
N = 512

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


#['MinLocation', 'StarAngularMomentumVector', 'TotalMass', 'AngularMomentumVector', 'TotalQuantity', 'IsBound', 'WeightedAverageQuantity', 'CenterOfMass', 'BulkVelocity', 'ParticleSpinParameter', 'Action', 'Extrema', 'MaxLocation', 'BaryonSpinParameter']

f.close()
open(file_to_write, 'rb').read()


print "ended.\n"
