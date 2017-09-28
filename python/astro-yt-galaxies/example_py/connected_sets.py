import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api

# Follow the simple_volume_rendering cookbook for the first part of this.
#fn = "~/work/enzo/data/cosmo/L25t128m4r10ps5-MW4/r0058/redshift0058" # parameter file to load
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load
pf = load(fn, file_style="%s.grid.cpu%%04i") # load data

c = [0.40328598, 0.47176743, 0.46131516] # densest cell coord.

#sphere = halos[0].get_sphere()
sphere = pf.h.sphere(c, (50., 'kpc')) # 250.

levels = 3 #8
mi, ma = sphere.quantities["Extrema"]("Density")[0]
print "mi, ma =", mi, ma

mi = na.log10(1.e-28)   # this range was chosen from the level 0
ma = na.log10(2.e-25)   # map, by looking at colors of halo clouds
tf = ColorTransferFunction((mi, ma))
# seven layers, with the kamae colormap, 0.01 dex wide each
tf.add_layers(8, colormap="kamae", w=0.01)

# Camera parameters

L = na.array([0.90798282, 0., 0.41900739]) # orthogonal to the angular momentum vector
W = 0.002 / pf["unitary"]
N = 1024
north_vector = na.array([0.25527702, -0.79298414, -0.55318153])

cam = pf.h.camera(c,                         # center
                  L,                         # view-angle
                  W,                         # FOV
                  (N,N),                     # resolution
                  tf,                        # transfer function
                  north_vector=north_vector) # rotation axis
cam.snapshot( "clumps_image.png", clip_ratio=4.0)   # clip by 4.0 * std()

#alpha=10.0*na.ones(8,dtype='float64')
alpha = [0.1]
print " alpha =", alpha
frame = 0
tf.clear()
tf.add_layers(8, colormap="kamae", w=0.01,alpha=alpha,mi=mi,col_bounds = [-27.5,-25.5], ma=ma)
# Do a rotation over x frames
loop = 180 
print "pi =", na.pi
angle = na.radians(frame)
for i, snapshot in enumerate(cam.rotation(angle, loop, clip_ratio = 4.0)):
    print "angle=", angle
    tf.clear()
    tf.add_layers(8, colormap="kamae", w=0.01,alpha=alpha,mi=mi,col_bounds = [-27.5,-25.5], ma=ma)
    write_bitmap(snapshot, 'camera_movement_%04i.png' % frame)
    frame += 1
    angle = na.radians(frame*2)





contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)

lev2contours = connected_sets[2]

#for i in connected_sets:
for i in lev2contours:
    eb       =  lev2contours[i]
    print eb.quantities.keys()
    cen      = eb.quantities["CenterOfMass"]()
    totm     = eb.quantities["TotalQuantity"]("CellMassMsun")[0]
    print " i =", i, " cen =", cen, " total mass =", totm
    limits   = eb.quantities["Extrema"]("Density")[0]
    print "   limits =", limits


print "ended.\n"
