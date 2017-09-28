#!/Users/francia/yt/yt-x86_64/bin/python2.7
# EASY-INSTALL-ENTRY-SCRIPT: 'yt==2.3','console_scripts','yt'
__requires__ = 'yt==2.3'
import sys
from yt.mods import * # set up our namespace

from pkg_resources import load_entry_point
import yt.frontends.enzo.api
yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"
from yt.analysis_modules.halo_mass_function.api import *



fn = "/astro/data/redshift0058/redshift0058" # parameter file to load

pf = load(fn) # load data

halos = HaloFinder(pf)

vr = halos[0].virial_radius()


