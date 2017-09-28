import sys
from yt.mods import * # set up our namespace
from yt.analysis_modules.halo_finding.api import *
from pkg_resources import load_entry_point
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"


# Follow the simple_volume_rendering cookbook for the first part of this.
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load
pf = load(fn) # load data
c = [0.403290331, 0.471765608, 0.461319029]
l = [0.383290331, 0.451765608, 0.441319029]
r = [0.423290331, 0.491765608, 0.481319029]

data_source = pf.h.region(c,l,r) 

levels = 10
halos =  HaloFinder(pf,  subvolume = data_source )
halos.write_out("HopAnalysisVolumeConnectHALONormalRyanCenterNew2.txt")

sphere = halos[0].get_sphere()
mi, ma = sphere.quantities["Extrema"]("Density")[0]
contour_values, connected_sets = sphere.extract_connected_sets("Density", levels, mi, ma)
#connected_sets 


# Choose a vector representing the viewing direction.
L = [0.5, 0.2, 0.7]

# Set the width of the image.
# Decreasing or increasing this value
# results in a zoom in or out.
W = 1.0

# The number of pixels along one side of the image.
# The final image will have Npixel^2 pixels.
Npixels = 512





# Specify a north vector, which helps with rotations.
north_vector = [0.,0.,1.]
#print connected_sets

for i in connected_sets:
    eb       =  connected_sets[i][0] 
    print eb.quantities.keys() 
    cen      = eb.quantities["CenterOfMass"]()
    limits   = eb.quantities["Extrema"]("Density")[0]
    tf = ColorTransferFunction(na.log10(limits))
    # five layers, with the kamae colormap, 0.001 dex wide each
    tf.add_layers(8, colormap="kamae", w=0.001)
    # Create a camera object.
    # This object creates the images and
    # can be moved and rotated.
    cam = pf.h.camera(cen, L, W, Npixels, tf)

    cam.snapshot( "%s_imageHOPNew2.png" % i) # clip by 4.0 * std()


print "end \n"