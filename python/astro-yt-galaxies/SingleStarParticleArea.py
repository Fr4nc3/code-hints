from yt.mods import *
from yt.analysis_modules.star_analysis.api import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)
    
from yt.analysis_modules.halo_finding.halo_objects import RunFOF 

fn = "/astro/data/d0300/data0300/data0300" # parameter file to load



pf = load(fn) # load data
# Now we need a center of our volume to render.  Here we'll just use

#linking_length = 0.017094633 # come from 



# Create a region that is a subset of the entire volume.
#D is calculated by 
#      0.25Mpc (250 kpc) divided by 35.714Mpc to convert to Box units 
#box Units  = 25/h Mpc = 25/0.70 Mpc = 35.714 Mpc 

D = 0.25/35.714 #0.25/35.714
center =[4.027091436e-01 ,   4.714863511e-01 , 4.621095851e-01]
left_corner =  [center[0]-D, center[1]-D, center[2]-D]
right_corner = [center[0]+D, center[1]+D, center[2]+D]
sv = pf.h.region(center, left_corner, right_corner)


haloes = HaloFinder(pf, subvolume = sv,  dm_only=True)

haloes.dump("MyHalosSmall3")
haloes.write_out("HopAnalysisSmall3.out")




## Iterate over the haloes.
#for halo in haloes:
#    ct = halo["creation_time"]
#
#    sm = halo["ParticleMassMsun"]
#    metal = halo["metallicity_fraction"]
#    # Select just the stars.
#    stars = (ct > 0)
#    print stars
#    ct = ct[stars]
#    sm = sm[stars]
#    metal = metal[stars]
#    print ct
#   # print ct.center_of_mass()
#    
    #print halo['centerOfMass']['x'] + " , " + halo['centerOfMass']['y'] + " , " + halo['centerOfMass']['z']