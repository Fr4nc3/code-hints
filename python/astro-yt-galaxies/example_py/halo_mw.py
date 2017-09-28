from yt.mods import *
from yt.analysis_modules.halo_profiler.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
# Define a custom function to be called on all halos.
# The first argument is a dictionary containing the
# halo id, center, etc.
# The second argument is the sphere centered on the halo.
def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)

fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data
# Now we need a center of our volume to render.  Here we'll just use
# center of our MW 




c = [0.403290331 , 0.471765608 , 0.461319029]

dd = pf.h.sphere(c, 300.0/pf['kpc']) # only the MK simulation \
halos = HaloFinder(dd)

halos.write_out("HopAnalysis.out")


# Instantiate HaloProfiler for this dataset.


hp = HaloProfiler(fn, halo_list_file='HopAnalysis.out')

# Add a filter to remove halos that have no profile points with overdensity
# above 200, and with virial masses less than 1e10 solar masses.
# Also, return the virial mass and radius to be written out to a file.
hp.add_halo_filter(amods.halo_profiler.VirialFilter, must_be_virialized=True,
                   overdensity_field='ActualOverdensity',
                   virial_overdensity=200,
                   virial_filters=[['TotalMassMsun', '>=', '1e10']],
                   virial_quantities=['TotalMassMsun', 'RadiusMpc'])

# Add profile fields.
hp.add_profile('CellVolume', weight_field=None, accumulation=True)
hp.add_profile('TotalMassMsun', weight_field=None, accumulation=True)
hp.add_profile('Density', weight_field='CellMassMsun', accumulation=False)
hp.add_profile('Temperature', weight_field='CellMassMsun', accumulation=False)

# Make profiles and output filtered halo list to FilteredQuantities.h5.
hp.make_profiles(filename="FilteredQuantities.h5",
                 profile_format='hdf5', njobs=-1)

# Add projection fields.
hp.add_projection('Density', weight_field=None)
hp.add_projection('Temperature', weight_field='Density')
hp.add_projection('Metallicity', weight_field='Density')

# Make projections just along the x axis using the filtered halo list.
hp.make_projections(save_cube=False, save_images=True,
                    halo_list='filtered', axes=[0], njobs=-1)

# Run our custom analysis function on all halos in the filtered list.
hp.analyze_halo_spheres(get_density_extrema, njobs=-1)



