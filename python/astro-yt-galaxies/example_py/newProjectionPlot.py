from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)
    

fn = "/astro/data/d0301/data0301/data0301" # parameter file to load

#RefineRegionLeftEdge   = 0.347627 0.429308 0.436357
#RefineRegionRightEdge  = 0.436006 0.511214 0.52262
c = [0.402824,0.471554,0.461972]

'''
clump:
local: d300 next: d301 level: 5 clump: 17 centerOfMass (x,y,z) 0.402625,0.471732,0.461585 (Xn,Yn,Zn) =0.402647,0.471724,0.461609 min (Xn,Yn,Zn) =0.402087,0.471164,0.461049 max (Xn,Yn,Zn) =0.403207,0.472284,0.462169 totalMass=1107381.615772

Clumps with mass between 50% and 150%

    level: 5 clump: 9 centerOfMass (X,Y,Z) =0.402862,0.472019,0.461895  totalMass = 1194193.315546 Delta BulkVelocity:366.726051 km/s delta X: 16.551520 D :16.860936
    level: 5 clump: 18 centerOfMass (X,Y,Z) =0.402603,0.471638,0.461454  totalMass = 900883.257440 Delta BulkVelocity:116.336271 km/s delta X: 6.515684 D :20.323478
class yt.visualization.plot_window.ProjectionPlot(pf, axis, fields, center='c', width=None, axes_unit=None, weight_field=None, max_level=None, origin='center-window', fontsize=18, field_parameters=None)[source]
'''

pf = load(fn) # load data
#sphere = pf.h.sphere(c, (250., 'kpc')) # 250.
p = ProjectionPlot(pf,2,'Density','max',(100,'kpc')) #,origin=('upper','left','window')) #,origin='upper-domain'
#p.annotate_point( (0.3, 0.4, 0.5), "Some Text")
#p.set_center((0.402647,0.471724,0.461609))
#p.zoom(1)
#p.set_font({'colors':'w'})
p.annotate_marker((0.402647,0.471724,0.461609),'x')
#p.annotate_point((0.402647,0.471724,0.461609), "p")
p.annotate_point((0.402862,0.472019,0.461895), "c1")
p.annotate_point((0.402603,0.471638,0.461454), "c2")
p.save('sliceplot')