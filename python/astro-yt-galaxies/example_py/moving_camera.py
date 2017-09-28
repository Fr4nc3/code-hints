import sys
from yt.mods import * # set up our namespace

from pkg_resources import load_entry_point
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"


# Follow the simple_volume_rendering cookbook for the first part of this.
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load
pf = load(fn) # load data
c = [0.403290331 , 0.471765608 , 0.461319029]
dd = pf.h.sphere(c, 300.0/pf['kpc']) # only the MK simulation 


mi, ma = dd.quantities["Extrema"]("Density")[0]

# Set up transfer function
tf = ColorTransferFunction((na.log10(mi), na.log10(ma)))
tf.add_layers(6, w=0.05)

# Set up camera paramters

L = [1, 1, 1] # Normal Vector
W = 0.01 # Width
Nvec = 512 # Pixels on a side

# Specify a north vector, which helps with rotations.
north_vector = [0.,0.,1.]

# Find the maximum density location, store it in max_c
v,max_c = pf.h.find_max('Density')

# Initialize the Camera
cam = pf.h.camera(c, L, W, (Nvec,Nvec), tf, north_vector=north_vector)
frame = 0

# Do a rotation over 5 frames
for i, snapshot in enumerate(cam.rotation(na.pi, 5, clip_ratio = 8.0)):
    write_bitmap(snapshot, 'camera_movement_%04i.png' % frame)
    frame += 1

# Move to the maximum density location over 5 frames
for i, snapshot in enumerate(cam.move_to(max_c, 5, clip_ratio = 8.0)):
    write_bitmap(snapshot, 'camera_movement_%04i.png' % frame)
    frame += 1

# Zoom in by a factor of 10 over 5 frames
for i, snapshot in enumerate(cam.zoomin(10.0, 5, clip_ratio = 8.0)):
    write_bitmap(snapshot, 'camera_movement_%04i.png' % frame)
    frame += 1
    
print "End "