from yt.mods import *
from yt.analysis_modules.star_analysis.api import *
from yt.analysis_modules.halo_finding.api import *
import yt.analysis_modules.halo_profiler.api as HP
from yt.analysis_modules.halo_mass_function.api import *
import yt.frontends.enzo.api

yt.frontends.enzo.api.EnzoHierarchy._bn = "%s.grid.cpu%%04i"

import pymongo
import numpy as np
import sys

mongo = pymongo.Connection('127.0.0.1')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection = mongo_db['starsParticle']

def get_density_extrema(halo, sphere):
    my_extrema = sphere.quantities['Extrema']('Density')
    mylog.info('Halo %d has density extrema: %s',
               halo['id'], my_extrema)


from yt.analysis_modules.halo_finding.halo_objects import RunFOF


data = [299, 300, 301, 302, 303, 304, 305, 306]


##################################################################################
#CENTER OF DENSEST CELL FOR EACH DATA
#COLLECTED FROM HALO FINDER
##################################################################################
centerPlot = {}
centerPlot["299"] = [4.026331263e-01, 4.714540963e-01, 4.622243906e-01]
centerPlot["300"] = [4.027091436e-01, 4.714863511e-01, 4.621095851e-01]
centerPlot["301"] = [4.067627915e-01, 4.723197619e-01, 4.596178269e-01]
centerPlot["302"] = [4.028744583e-01, 4.715630154e-01, 4.618947428e-01]
centerPlot["303"] = [4.029489628e-01, 4.715991739e-01, 4.617865227e-01]

centerPlot["304"] = [4.030269645e-01, 4.716397766e-01, 4.616750455e-01]
centerPlot["305"] = [4.031041336e-01, 4.716763146e-01, 4.615712357e-01]
centerPlot["306"] = [4.031828656e-01, 4.717151386e-01, 4.614570797e-01]

for d in data:
    dataName = str(d)
    print dataName

    fn = "/astro/data/d0" + dataName + "/data0" + dataName + "/data0" + dataName # parameter file to load
    # Now we need a center of our volume to render.  Here we'll just use
    # center of our MW
    c = centerPlot[dataName]
    pf = load(fn) # load data
    # Now we need a center of our volume to render.  Here we'll just use

    # Create a region that is a subset of the entire volume.
    #D is calculated by
    #      0.25Mpc (250 kpc) divided by 35.714Mpc to convert to Box units
    #box Units  = 25/h Mpc = 25/0.70 Mpc = 35.714 Mpc

    D = 0.25 / 35.714 #0.25/35.714
    center = c
    left_corner = [center[0] - D, center[1] - D, center[2] - D]
    right_corner = [center[0] + D, center[1] + D, center[2] + D]
    sv = pf.h.region(center, left_corner, right_corner)

    haloes = LoadHaloes(pf, "MyHalosSubVol"+dataName)
    haloCount=0
    for halo in haloes:

        ct = halo["creation_time"]
        #http://yt-project.org/docs/2.6/reference/field_list.html?
        sm = halo["ParticleMassMsun"]
        metal = halo["metallicity_fraction"]
        # Select just the stars.
        stars = (ct > 0)
        #print stars
        ct = ct[stars]
        sm = sm[stars]
        metal = metal[stars]
        mx = (halo["particle_position_x"][stars] * sm).sum()/sm.sum()
        my = (halo["particle_position_y"][stars] * sm).sum()/sm.sum()
        mz = (halo["particle_position_z"][stars] * sm).sum()/sm.sum()
        vx = (halo["particle_velocity_x"][stars] * sm).sum()/sm.sum()
        vy = (halo["particle_velocity_y"][stars] * sm).sum()/sm.sum()
        vz = (halo["particle_velocity_z"][stars] * sm).sum()/sm.sum()

        try:
            ds = (halo["Density"][stars] * sm).sum()/sm.sum()
        except:
            ds = -1
            pass

        try:
            tem = (halo["Temperature"][stars] * sm).sum()/sm.sum()
        except:
            tem = -1
            pass

        try:
            te = (halo["TotalEnergy"][stars] * sm).sum()/sm.sum()
        except:
            te = -1
            pass



        #IF MX MY MZ ARE DEFINED INSERT TO DB
        if not np.isnan(mx) and not np.isnan(my) and not np.isnan(mz):
            print mx
            print my
            print mz
            print "enter"
            print dataName
            insert_id = mongo_collection.insert({
                'starParticle': haloCount,
                'data' : "d"+dataName,
                'dataNum' : dataName,
                'density' : ds,
                'temperature': tem,
                'totalEnergy':te,
                'centerOfStarsParticles': {
                    'x': np.float64(mx),
                    'y': np.float64(my),
                    'z': np.float64(mz)
                },
                'Velocity': {
                    'x': np.float64(vx),
                    'y': np.float64(vy),
                    'z': np.float64(vz)
                }

            })
            haloCount = haloCount+1


        print haloCount
        print "--------\n\n"

'''
Universal Field List
AbsDivV
AngularMomentumX
AngularMomentumY
AngularMomentumZ
AveragedDensity
BMagnitude
BPoloidal
BRadial
BToroidal
BaroclinicVorticityMagnitude
BaroclinicVorticityX
BaroclinicVorticityY
BaroclinicVorticityZ
Baryon_Overdensity
CellMass
CellMassCode
CellMassMsun
CellVolume
CellVolumeCode
CellVolumeMpc
CellsPerBin
ChandraEmissivity
ComovingDensity
Contours
CourantTimeStep
CuttingPlaneBx
CuttingPlaneBy
CuttingPlaneVelocityX
CuttingPlaneVelocityY
DensityPerturbation
DiskAngle
DivV
DynamicalTime
Entropy
GridIndices
GridLevel
Height
HeightAU
JeansMassMsun
MachNumber
MagneticEnergy
MagneticPressure
Matter_Density
MeanMolecularWeight
Ones
OnesOverDx
Overdensity
ParticleAngularMomentumX
ParticleAngularMomentumY
ParticleAngularMomentumZ
ParticleMass
ParticleRadius
ParticleRadiusAU
ParticleRadiusCode
ParticleRadiusMpc
ParticleRadiuskpc
ParticleRadiuskpch
ParticleRadiuspc
ParticleSpecificAngularMomentumX
ParticleSpecificAngularMomentumXKMSMPC
ParticleSpecificAngularMomentumY
ParticleSpecificAngularMomentumYKMSMPC
ParticleSpecificAngularMomentumZ
ParticleSpecificAngularMomentumZKMSMPC
ParticleVelocityMagnitude
PlasmaBeta
Pressure
RadialMachNumber
RadialVelocity
RadialVelocityABS
RadialVelocityKMS
RadialVelocityKMSABS
Radius
RadiusAU
RadiusCode
RadiusMpc
Radiuskpc
Radiuspc
SZKinetic
SZY
Shear
ShearCriterion
ShearMach
SoundSpeed
SpecificAngularMomentumX
SpecificAngularMomentumY
SpecificAngularMomentumZ
StarMassMsun
TangentialOverVelocityMagnitude
TangentialVelocity
TempkeV
TotalMass
TotalMassMsun
VelocityMagnitude
VorticityGrowthMagnitude
VorticityGrowthMagnitudeABS
VorticityGrowthTimescale
VorticityGrowthX
VorticityGrowthY
VorticityGrowthZ
VorticityMagnitude
VorticityRPGrowthMagnitude
VorticityRPGrowthMagnitudeABS
VorticityRPGrowthTimescale
VorticityRPGrowthX
VorticityRPGrowthY
VorticityRPGrowthZ
VorticityRadPressureMagnitude
VorticityRadPressureX
VorticityRadPressureY
VorticityRadPressureZ
VorticitySquared
VorticityStretchingMagnitude
VorticityStretchingX
VorticityStretchingY
VorticityStretchingZ
VorticityX
VorticityY
VorticityZ
WeakLensingConvergence
XRayEmissivity
Zeros
cyl_R
cyl_RCode
cyl_RadialVelocity
cyl_RadialVelocityABS
cyl_RadialVelocityKMS
cyl_RadialVelocityKMSABS
cyl_TangentialVelocity
cyl_TangentialVelocityABS
cyl_TangentialVelocityKMS
cyl_TangentialVelocityKMSABS
cyl_theta
cyl_z
dx
dy
dz
gradDensityMagnitude
gradDensityX
gradDensityY
gradDensityZ
gradPressureMagnitude
gradPressureX
gradPressureY
gradPressureZ
particle_density
particle_position_x
particle_position_y
particle_position_z
sph_phi
sph_r
sph_theta
tempContours
x
y
z


Enzo-Specific Field List
Bmag
Comoving_DII_Density
Comoving_DI_Density
Comoving_Electron_Density
Comoving_H2II_Density
Comoving_H2I_Density
Comoving_HDI_Density
Comoving_HII_Density
Comoving_HI_Density
Comoving_HM_Density
Comoving_HeIII_Density
Comoving_HeII_Density
Comoving_HeI_Density
Comoving_MetalSNIa_Density
Comoving_Metal_Density
Comoving_PreShock_Density
DII_Fraction
DII_Mass
DII_MassMsun
DII_NumberDensity
DI_Fraction
DI_Mass
Dark_Matter_Mass
Dark_Matter_MassMsun
Electron_Fraction
Electron_Mass
Gas_Energy
H2II_Fraction
H2II_Mass
H2I_Fraction
H2I_Mass
HDI_Fraction
HDI_Mass
HII_Fraction
HII_Mass
HI_Fraction
HI_Mass
HM_Fraction
HM_Mass
H_NumberDensity
HeIII_Fraction
HeIII_Mass
HeII_Fraction
HeII_Mass
HeI_Fraction
HeI_Mass
IsStarParticle
KineticEnergy
MetalSNIa_Fraction
MetalSNIa_Mass
Metal_Fraction
Metal_Mass
Metallicity
Metallicity3
NumberDensity
ParticleAge
ParticleMass
ParticleMassMsun
PreShock_Fraction
PreShock_Mass
RadiationAcceleration
StarAgeYears
StarCreationTimeYears
StarDynamicalTimeYears
StarMetallicity
ThermalEnergy
TotalEnergy
Total_Energy
cic_particle_velocity_x
cic_particle_velocity_y
cic_particle_velocity_z
dm_density
particle_mass
star_creation_time
star_density
star_dynamical_time
star_metallicity_fraction
tracer_number_density
'''