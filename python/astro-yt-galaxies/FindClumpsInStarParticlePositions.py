import pymongo
import numpy as np
import math  # This will import math module


mongo = pymongo.Connection('localhost')
# Returns Database Object
mongo_db = mongo['astro']

level_collection = mongo_db['levels']
starParticles_collection = mongo_db['starsParticle']





data = [299, 300, 301, 302, 303, 304, 305, 306]

level = "5"

#small distance to the center of Star Particle
sm = (0.020) / (35.714)  # Mpc to L units


for d in data:

    dataName = "d" + str(d)
    print "Data Name:" + dataName
    stars = starParticles_collection.find({'data': dataName})

    #1 kpc -> 0.001 Mpc ->  (in units of L)
    location = (0.015) / (35.714)  # Mpc to L units

    str_sm = "%.0f" % (location * 35.714 * 1000)
    boxL = 35.714  # in Mpc

    print "radius : " + str_sm + " Kpc"

    if stars.count() > 0:
        for this_star in stars:

            minl_x = np.float64(this_star['centerOfStarsParticles']['x']) - sm
            minl_y = np.float64(this_star['centerOfStarsParticles']['y']) - sm
            minl_z = np.float64(this_star['centerOfStarsParticles']['z']) - sm

            maxl_x = np.float64(this_star['centerOfStarsParticles']['x']) + sm
            maxl_y = np.float64(this_star['centerOfStarsParticles']['y']) + sm
            maxl_z = np.float64(this_star['centerOfStarsParticles']['z']) + sm


            clumps = level_collection.find({
                'local' : dataName,
                'centerOfMass.x' : { '$gt': minl_x, '$lt': maxl_x },
                'centerOfMass.y' : { '$gt': minl_y, '$lt': maxl_y },
                'centerOfMass.z' : { '$gt': minl_z, '$lt': maxl_z }
            })

            if  clumps.count() > 0:
                for this_clump in clumps:
                    this_clump_string = " clump: " +  this_clump['clump']  +  " centerOfMass (x,y,z) " + "%.6f" % this_clump['centerOfMass']['x'] +  "," +  "%.6f" % this_clump['centerOfMass']['y'] + "," +  "%.6f" %  this_clump['centerOfMass']['z'] + " totalMass=" +  "%.6f" % this_clump['totalMass']
                    print "Data :" + dataName + " Star Particle"+ str(this_star['starParticle'])   + " center of Mass " + "%.6f" % this_star['centerOfStarsParticles']['x'] +  "," +  "%.6f" % this_star['centerOfStarsParticles']['y'] + "," +  "%.6f" %  this_star['centerOfStarsParticles']['z']
                    print this_clump_string
                    print "Star  Velocity: " + "%.6f" % this_star['Velocity']['x']   + "," +  "%.6f" % this_star['Velocity']['y']   + "," + "%.6f" % this_star['Velocity']['z']
                    print "Clump Velocity: " + "%.6f" % this_clump['bulkVelocity']['x']   + "," +  "%.6f" %  this_clump['bulkVelocity']['y']  + "," + "%.6f" % this_clump['bulkVelocity']['z']
                    print "\n\n"