import sys
from yt.mods import * # set up our namespace
import yt.frontends.enzo.api
from pkg_resources import load_entry_point

yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"




fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data
# Now we need a center of our volume to render.  Here we'll just use
# center of our MW 
c = [0.403290331 , 0.471765608 , 0.461319029]

dd = pf.h.sphere(c, 250.0/pf['kpc']) # only the MK simulation 


# Get the bounds of density
mi, ma = dd.quantities["Extrema"]("Density")[0]


tf = ColorTransferFunction((na.log10(mi), na.log10(ma)))

# Now we add some Gaussians on.  Work is underway to transform this into a
# graphical user interface, and the initial steps can be found in
# transfer_function_widget.py .

# We now just add a couple gaussians, sampled inside the colormap "gist_stern"
# at equally-spaced locations in the transfer function.  We make them a bit
# wider, too.
tf.add_layers(6, w=0.02)


# Our image plane will be normal to some vector.  For things like collapsing
# objects, you could set it the way you would a cutting plane -- but for this
# dataset, we'll just choose an off-axis value at random.  This gets normalized
# automatically.
L = [0.4, 0.3, 0.5]

# Our "width" is the width of the image plane as well as the depth -- so we set
# it to be 1.0 so we get the whole domain.
W = 0.01

# Now we decide how big an image we want.  512x512 should be sufficient.
Nvec = 512

# Now we call the ray caster, which handles the rest.
# Note that we feed whole_box, which means that it won't apply any cuts to the
# considered grids.  This may be unnecessary for most appliations.
cam = pf.h.camera(c, L, W, Nvec, tf)

# Now we tell the camera object to take a snapshot, casting the rays
image = cam.snapshot()

# If we want to save the image when we take this snapshot, we can use the
# keyword fn= :
# image = cam.snapshot("%s_volume_rendering.png" % pf)

# Othwerwise, we can then write out the image using our direct bitmap writer
write_bitmap(image, "%s_volume_rendered.png" % pf)
