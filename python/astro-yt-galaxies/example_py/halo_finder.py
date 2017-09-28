from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *

# If desired, start loop here.
fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data

#halo_list = FOFHaloFinder(pf)
#halo_list.write_out("HopAnalysis.out")

#c = [0.403290331 , 0.471765608 , 0.461319029]

#dd = pf.h.sphere(c, 300.0/pf['kpc']) # only the MK simulation \
#halos = HaloFinder(dd)


hp = HP.HaloProfiler(fn, halo_list_file='/astro/py/HopAnalysis.out')
hp.add_halo_filter(HP.VirialFilter,must_be_virialized=True,
              overdensity_field='ActualOverdensity',
              virial_overdensity=200,
              virial_filters=[['TotalMassMsun','>=','1e8']],
              virial_quantities=['TotalMassMsun','RadiusMpc'])
hp.make_profiles(filename="/astro/py/VirialHaloes.out")

hmf = HaloMassFcn(pf, halo_file="/astro/py/VirialHaloes.out",
sigma8input=0.9, primordial_index=1., omega_baryon0=0.06,
fitting_function=4, mass_column=5, num_sigma_bins=200)
hmf.write_out(prefix='hmf')
# End loop here.