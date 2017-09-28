# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from yt.mods import *
import h5py

# <codecell>

f = h5py.File("profiles.h5", "w")
for i in range(47):
    pc = PlotCollection(pf, "c")
    dd = pf.h.all_data()
    p = pc.add_profile_object(dd, ["Density", "Temperature"], weight = "CellMassMsun")
    f.create_group("/DD%04i" % i)
    f.create_dataset("/DD%04i/Density" % i, data=p.data["Density"])
    f.create_dataset("/DD%04i/Temperature" % i, data=p.data["Temperature"])

# <codecell>

f.close()

# <codecell>

f = h5py.File("profiles.h5", "r")
import pylab
pylab.clf()
for i in range(47):
    pylab.loglog(f["/DD%04i/Density" % i], f["/DD%04i/Temperature" % i], '-')
pylab.show()

# <codecell>