from yt.mods import * # set up our namespace

import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"


fn = "/astro/data/redshift0058/redshift0058" # parameter file to load
field = "Density" # this is the field we look for contours over -- we could do
                  # this over anything.  Other common choices are 'AveragedDensity'
                  # and 'Dark_Matter_Density'.
step = 10.0 # This is the multiplicative interval between contours.

pf = load(fn) # load data




dd = pf.h.sphere("max", 100.0/pf['kpc'])
print dd.quantities["Extrema"]("ThermalEnergy")
exit()

# Now we set some sane min/max values between which we want to find contours.
# This is how we tell the clump finder what to look for -- it won't look for
# contours connected below or above these threshold values.
c_min = 10**na.floor(na.log10(data_source[field]).min()  )
c_max = 10**na.floor(na.log10(data_source[field]).max()+1)

# Now find get our 'base' clump -- this one just covers the whole domain.
master_clump = amods.level_sets.Clump(data_source, None, field)

# This next command accepts our base clump and we say the range between which
# we want to contour.  It recursively finds clumps within the master clump, at
# intervals defined by the step size we feed it.  The current value is
# *multiplied* by step size, rather than added to it -- so this means if you
# want to look in log10 space intervals, you would supply step = 10.0.
amods.level_sets.find_clumps(master_clump, c_min, c_max, step)

# As it goes, it appends the information about all the sub-clumps to the
# master-clump.  Among different ways we can examine it, there's a convenience
# function for outputting the full hierarchy to a file.
f = open('%s_clump_hierarchy.txt' % pf,'w')
amods.level_sets.write_clump_hierarchy(master_clump,0,f)
f.close()

# We can also output some handy information, as well.
f = open('%s_clumps.txt' % pf,'w')
amods.level_sets.write_clumps(master_clump,0,f)
f.close()
# If you'd like to visualize these clumps, a list of clumps can be supplied to
# the "clumps" callback on a plot.