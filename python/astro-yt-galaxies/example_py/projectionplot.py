from yt.mods import *
import yt.frontends.enzo.api
import numpy as na
import matplotlib.colorbar as cb

yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data
#pf = load("redshift0058")

orient = 'horizontal'
fig, axes, colorbars = get_multi_plot(1, 1, colorbar=orient, bw = 4)
#pf.h.print_stats()
#print pf.h.find_max("Density")
#yt : [INFO     ] 2012-06-13 00:19:57,745 Max Value is 2.37163e-23 at 0.4032859802246094 0.4717674255371094 0.4613151550292944 in grid EnzoGrid_15868 at level 10 (11, 11, 15)

# Set central position (from above)
(value, location) = (2.3716325298617172e-23, [ 0.40328598,  0.47176743,  0.46131516])

# Define Radial mass flux

def _RadialMassFlux(field, data):
   return data["RadialVelocity"] * data["Density"]

add_field("RadialMassFlux", function=_RadialMassFlux, units=r"\rm{g}/\rm{cm}/\rm{s}", take_log=False)

# Define Negative radial mass flux (inward)

def _NegativeRadialMassFlux(field, data):
   return na.minimum(data["RadialVelocity"],0.0) * data["Density"]

add_field("NegativeRadialMassFlux", function=_NegativeRadialMassFlux, units=r"\rm{g}/\rm{cm}/\rm{s}", take_log=False)

# Get halo list

#halo_list = yt.analysis_modules.halo_finding.api.FOFHaloFinder(pf)
#halo_list.write_out("HaloAnalysis.out")

# Define sphere and get bulk velocity

sp = pf.h.sphere(location, 250.0/pf['kpc'])
bv = sp.quantities["BulkVelocity"]()
sp.set_field_parameter('bulk_velocity', bv)
print sp.get_field_parameter("bulk_velocity")
fp = {'bulk_velocity' : bv}

pc = PlotCollection(sp, location)
#pc.set_cmap('gist_yarg')
#cb = pc.colorbar(image, orientation='horizontal')


p = pc.add_projection("NegativeRadialMassFlux", 'y', field_parameters=fp, use_colorbar=False)
p.set_zlim(-5000,0)
p.set_cmap("gray") 
#p.set_label(r"$\rm{g}/\rm{cm}/\rm{s}$")

pc.set_width(400, 'kpc')


#pc.save(format="eps")



# Each 'p' is a plot -- this is the Density plot and the Temperature plot.
# Each 'cax' is a colorbar-container, into which we'll put a colorbar.
# zip means, give these two me together.
for p, cax in zip(pc.plots, colorbars):
    # Now we make a colorbar, using the 'image' attribute of the plot.
    # 'image' is usually not accessed; we're making a special exception here,
    # though.  'image' will tell the colorbar what the limits of the data are.
    cbar = cb.Colorbar(cax, p.image, orientation=orient)
    # Now, we have to do a tiny bit of magic -- we tell the plot what its
    # colorbar is, and then we tell the plot to set the label of that colorbar.
    p.colorbar = cbar
    p._autoset_label()

# And now we're done!  Note that we're calling a method of the figure, not the
# PlotCollection.
fig.savefig("%s" % pf)



