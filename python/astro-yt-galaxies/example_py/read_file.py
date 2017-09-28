import pymongo
import numpy as np
import sys
mongo = pymongo.Connection('127.0.0.1')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection = mongo_db['levels']



local  = sys.argv[1]
next  = sys.argv[2]

ins = open( local+"_levels.txt", "r" )
array = []
for line in ins:
    array.append( line )

print "local: " + local
print "next: " + next
'''
PURPOSE OF THIS FILE IS PROCESS THE DATA FROM CLUMPS ANALYSIS AND CONVERT IT TO MONGO:

    level 0| clump 1| centerOfMass 2| totalMass  3| BulkVelocity  4| MinLocation 5| StarAngularMomentumVector 6| angularMomentumVector 7| IsBound 8| WeightedAverageQuantity 9|  ParticleSpinParameterAction 10| MaxLocation 11| BaryonSpinParameter 12| Extrema 13
    1) Distance (d) d= VT
    Use Bulk Velocity of the Clump in cm/s
    Time 1.357e15 (in seconds) (which time? where we get it?) -> d in cm
    Divide by 3.08567758e18 (convert cm to parsec) is this correct -> d in pc
    Divide by 1e6 convert to Mpc -> d in Mpc
    Divide By 35.714 (convert to Box L) -> d in simulation length unit (in units of L)
    (box L = 25/h Mpc = 25/0.70 Mpc = 35.714 Mpc)
    After that, you have three numbers (delta x, delta y, delta z).  Add them respectively to the old center of Mass to get the new coordinate
    1 kpc = 0.001/35.714 Mpc
    center of mass is in simulation units
    
'''
time     = 1.357e15   # time interval in seconds
toParsec = 3.08567758e18
toMpc    = 1e6
boxL     = 35.714   # in Mpc

for i in array:
    objects = i.split("|")
    level   = objects[0].strip(' \t\n\r')
    clump   = objects[1].strip(' \t\n\r')
    centerOfMass    = objects[2].split(",")
    bulkVelocity    = objects[4].split(",")
    Extrema         = objects[13].split(",")
    AngularMomentumVector = objects[7].strip(' \t\n\r').split(",")
    '''
    Calculate next location of a clump
    assumptions: Constant velocity, dissmissed expanding Universe. 
    Xn,Yn,Zn are in simulation units
    '''
    Xn = np.float64(centerOfMass[0])+((((np.float64(bulkVelocity[0])*time)/toParsec)/toMpc)/boxL)
    Yn = np.float64(centerOfMass[1])+((((np.float64(bulkVelocity[1])*time)/toParsec)/toMpc)/boxL)
    Zn = np.float64(centerOfMass[2])+((((np.float64(bulkVelocity[2])*time)/toParsec)/toMpc)/boxL)
    print "extrema min"+ Extrema[0].strip(' \t\n\r') 
    print "extrema max"+ Extrema[1].strip(' \t\n\r') 
    insert_id = mongo_collection.insert({
                                    'level': level,
                                    'clump': clump,
                                    'totalMass': np.float64(objects[3].strip(' \t\n\r')),
                                    'minLocation': objects[5].strip(' \t\n\r'),
                                    'maxLocation': objects[11].strip(' \t\n\r'),
                                    'StarAngularMomentumVector': objects[6].strip(' \t\n\r'),
                                    'WeightedAverageQuantity': objects[9].strip(' \t\n\r'),
                                    'ParticleSpinParameterAction': objects[9].strip(' \t\n\r'),
                                    'BaryonSpinParameter': objects[9].strip(' \t\n\r'),
                                    'Extrema': {
                                            'min': np.float64(Extrema[0].strip(' \t\n\r')),
                                            'max': np.float64(Extrema[1].strip(' \t\n\r'))
                                     },
                                    'next': next,
                                    'local': local,
                                    'angularMomentumVector': {
                                             'x': np.float64(AngularMomentumVector[0]),
                                             'y': np.float64(AngularMomentumVector[1]),
                                             'z': np.float64(AngularMomentumVector[2])
                                          },
                                    'next_location': {
                                             'x': Xn,
                                             'y': Yn,
                                             'z': Zn
                                          },
                                    'centerOfMass': {
                                               'x': np.float64(centerOfMass[0].strip(' \t\n\r')),
                                               'y': np.float64(centerOfMass[1].strip(' \t\n\r')),
                                               'z': np.float64(centerOfMass[2].strip(' \t\n\r'))
                                    },
                                    'bulkVelocity': {
                                               'x': np.float64(bulkVelocity[0].strip(' \t\n\r')),
                                               'y': np.float64(bulkVelocity[1].strip(' \t\n\r')),
                                               'z': np.float64(bulkVelocity[2].strip(' \t\n\r'))
                                    }
                                    
                                    })