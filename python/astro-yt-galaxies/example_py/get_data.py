import pymongo
import numpy as np
import math   # This will import math module
import simplejson as json
import sys

mongo = pymongo.Connection('localhost')
# Returns Database Object
mongo_db = mongo['astro']
mongo_collection = mongo_db['levels']


local  = sys.argv[1] #ex: d299
next  = sys.argv[2]  #ex: d300
level  = sys.argv[3] #ex: 5 
print "local" + local
print "next" + next
print "level" + level
# Returns Cursor Object
clumps = mongo_collection.find({'local':local, 'level':level})
#1 kpc -> 0.001 Mpc ->  (in units of L)
sm      = (0.020)/(35.714) # Mpc to L units
innersm = (0.015)/(35.714) # Mpc 
'''
PURPOSE OF THIS FILE IS Bring Different Clumps and identify possible candidates  in the next level of data:
EX: Clumps from d300, Level 0 
brings All clumps from level 0 at the data d300 

Looking for the center of mass of he moss massive clumps
'''
str_sm = "%.0f" % (sm*35.714*1000) 
str_inner = "%.0f" % (innersm*35.714*1000)
boxL     = 35.714   # in Mpc

print "radius : " + str_sm+" Kpc"
print "inner radius : " + str_inner +" Kpc"
clumps_centerofgalaxy = mongo_collection.find({'local':next, 'level':"7"})
massive_clump_mass    = 0
massive_clump_mass_obj = []
def IsNotNull(value):
    return value is not None and len(value) > 0

counter_clumps_withmorethan1candidate             = 0
counter_clumps_withuniquecandidatemassless50      = 0
counter_clumps_withuniquecandidatemassmore50      = 0
counter_clumps_outsidesmallradio                  = 0
counter_clumps_clumps_nocandidate                 = 0
counter_clumps_candidatemassmore150               = 0
counter_clumps_withuniquecandidatemassmore150Un   = 0
counter_clumps_candidatemassmore150NoUn           = 0

# here we storage the massive clump of this data
if clumps_centerofgalaxy.count() > 0:
   for massive_clump in clumps_centerofgalaxy:
       TotalMassiveMassThis = np.float64(massive_clump['totalMass'])
       if (TotalMassiveMassThis > massive_clump_mass):
          massive_clump_mass_obj = massive_clump
          massive_clump_mass     = TotalMassiveMassThis
          massive_x = np.float64(massive_clump_mass_obj['centerOfMass']['x'])
          massive_y = np.float64(massive_clump_mass_obj['centerOfMass']['y'])
          massive_z = np.float64(massive_clump_mass_obj['centerOfMass']['z'])
       
print "clump: " + massive_clump_mass_obj['clump'] + " level:" +  massive_clump_mass_obj['level']
print "Massive Clump center of mass " + "%.6f" %  massive_x + ","+ "%.6f" %  massive_y + "," + "%.6f" % massive_z 
clumps_collections = []
total_clumps               =  clumps.count()
unique_clumps              = 0
non_unique_clumps          = 0
counter_clumps_nocandidate = 0
clumps_outside             = 0
clumps_weights             = 0
if clumps.count() > 0:
   for this_clump in clumps:
       
       '''
        Calculate the minimun and maximum location of possible clump candidates 
       '''
       minl_x = np.float64(this_clump['next_location']['x'])-sm
       minl_y = np.float64(this_clump['next_location']['y'])-sm
       minl_z = np.float64(this_clump['next_location']['z'])-sm
       #clump BulkVelocity
       thisvel_x = np.float64(this_clump['bulkVelocity']['x'])
       thisvel_y = np.float64(this_clump['bulkVelocity']['y'])
       thisvel_z = np.float64(this_clump['bulkVelocity']['z'])
     
     
       minl_x_str = "%.6f" % minl_x 
       minl_y_str = "%.6f" % minl_y
       minl_z_str = "%.6f" % minl_z
     
     
       maxl_x = np.float64(this_clump['next_location']['x'])+sm
       maxl_y = np.float64(this_clump['next_location']['y'])+sm
       maxl_z = np.float64(this_clump['next_location']['z'])+sm
       
       
       maxl_x_str = "%.6f" %  maxl_x 
       maxl_y_str = "%.6f" %  maxl_y
       maxl_z_str = "%.6f" %  maxl_z
       
       next_location_x =np.float64(this_clump['next_location']['x'])
       next_location_y =np.float64(this_clump['next_location']['y'])
       next_location_z =np.float64(this_clump['next_location']['z'])
       
       '''
        Smaller location Radio 
       '''
       inn_minl_x = np.float64(this_clump['next_location']['x'])-innersm
       inn_minl_y = np.float64(this_clump['next_location']['y'])-innersm
       inn_minl_z = np.float64(this_clump['next_location']['z'])-innersm
     
       inn_maxl_x = np.float64(this_clump['next_location']['x'])+innersm
       inn_maxl_y = np.float64(this_clump['next_location']['y'])+innersm
       inn_maxl_z = np.float64(this_clump['next_location']['z'])+innersm
       
       
       TotalMassThis = np.float64(this_clump['totalMass'])
       totalMassPlus50Per = TotalMassThis+(TotalMassThis)/2 
       totalMassLess50Per = (TotalMassThis)/2 
       next_clumps = mongo_collection.find({
                                             'local' : this_clump['next'],
                                             'level': this_clump['level'],
                                             'centerOfMass.x' : { '$gt': minl_x, '$lt': maxl_x },
                                             'centerOfMass.y' : { '$gt': minl_y, '$lt': maxl_y },
                                             'centerOfMass.z' : { '$gt': minl_z, '$lt': maxl_z }
                                            })
     
       this_clump_string = "local: " + this_clump['local'] +  " next: "+ this_clump['next'] + " level: " +  this_clump['level'] + " clump: " +  this_clump['clump'] + " centerOfMass (x,y,z) " + "%.6f" % this_clump['centerOfMass']['x'] +  "," +  "%.6f" % this_clump['centerOfMass']['y'] + "," +  "%.6f" %  this_clump['centerOfMass']['z'] + " (Xn,Yn,Zn) =" +  "%.6f" % this_clump['next_location']['x'] +  "," +  "%.6f" % this_clump['next_location']['y']+ "," +  "%.6f" % this_clump['next_location']['z'] + " min (Xn,Yn,Zn) =" + minl_x_str +  "," +  minl_y_str + "," + minl_z_str + " max (Xn,Yn,Zn) =" + maxl_x_str +  "," + maxl_y_str + "," + maxl_z_str+ " totalMass=" +  "%.6f" % this_clump['totalMass'] 
       #print "-----"
       #print "Clump: "
       #print this_clump_string
       counted                 = 0
       thisClump               = {}
       thisClump["clump"]      = this_clump_string
       thisClump["unique"] = []
       thisClump["candidates"] = []
       thisClump["masses"]     = 0 
       thisClump["distance"]   = ""
       count_candidates = 0
       next_clump_count_unique = 0
       if next_clumps.count() > 0:
           '''
           (a) 1 clump -> 1 candidate (clump) : match -- simplest case
           (b) 1 clump -> 2 clumps : separation
           (c) 2 clumps -> 1 clump : merging
           (d, e) 1 clump -> 0 clump : disappearance OR merging w/ the disk  [Judge based on the distance to the disk -- or the center of the most massive clump in a given data set]
           '''
           count  =  next_clumps.count() 
           for next_clump in next_clumps:
               TotalMassNext = np.float64(next_clump['totalMass'])
               com_x =  np.float64( next_clump['centerOfMass']['x'])
               com_y =  np.float64( next_clump['centerOfMass']['y'])
               com_z =  np.float64( next_clump['centerOfMass']['z'])
               #candidate Bulk Velocity 
               vel_x =  np.float64(next_clump['bulkVelocity']['x'])
               vel_y =  np.float64(next_clump['bulkVelocity']['y'])
               vel_z =  np.float64(next_clump['bulkVelocity']['z'])
               
               #delta Bulk Velocity between candidate and clumps
               delta_X = math.sqrt(math.pow((next_location_x-com_x),2) + math.pow((next_location_y-com_y),2) + math.pow((next_location_z-com_z),2) )*boxL*1000 # deltax in Kpc
               distance_candiate = math.sqrt(math.pow((massive_x-com_x),2) + math.pow((massive_y-com_y),2) + math.pow((massive_z-com_z),2) )*boxL*1000 # deltax in Kpc
               delta_vel = math.sqrt(math.pow((thisvel_x-vel_x),2) + math.pow((thisvel_y-vel_y),2) + math.pow((thisvel_z-vel_z),2) )*0.00001 # 10*^-5km/s
               #candidate printable data
               per_mass = (TotalMassNext*100)/TotalMassThis
               candidate = "    level: "+ next_clump['level'] +" clump: "+ next_clump['clump'] + " centerOfMass (X,Y,Z) =" + "%.6f" % next_clump['centerOfMass']['x'] +  "," + "%.6f" %next_clump['centerOfMass']['y']+ "," + "%.6f" % next_clump['centerOfMass']['z']   +"  totalMass = " + "%.6f" %next_clump['totalMass'] + " Delta BulkVelocity:" + "%.6f" %  delta_vel + " km/s" + " delta X: " + "%.6f" % delta_X + " D :" +  "%.6f" % distance_candiate + " Mass % : " + "%.6f" % per_mass 

               if((inn_minl_x < com_x < inn_maxl_x)  & (inn_minl_y < com_y < inn_maxl_y) & (inn_minl_z < com_z <inn_maxl_z)): # candidate is inside smaller radio
                   if(count == 1) :
                         if  totalMassLess50Per < TotalMassNext  < totalMassPlus50Per: 
                             thisClump["unique"].append(candidate) 
                             unique_clumps +=1 
                         else: #unique but mass is greater or smaller than 50% and 150%
                             if count_candidates == 0:
                                clumps_weights +=1
                                count_candidates = 1
                   else:#more than one candidate 
                         if  totalMassLess50Per < TotalMassNext  < totalMassPlus50Per: 
                             thisClump["candidates"].append(candidate) 
                             thisClump["masses"]+=TotalMassNext
                         if count_candidates == 0:
                            non_unique_clumps +=1
                            count_candidates = 1
               else: # candidates outside the small radius 
                    if count_candidates == 0:
                       clumps_outside +=1
                       count_candidates = 1

                         
       else: #clumps doesn't have candidate
             #calculate the distance from the clumps (expected location to the center of the moss massive clump 
             '''
             distance between three points 
             D = ((x2-x1)^2+(y2-y1)^2+(z2-z1)^2)^1/2  in in units of L
             Dx35.714  distance in Mpc 
             '''
             D = (math.sqrt(math.pow((next_location_x-massive_x),2)+math.pow((next_location_y-massive_y),2)+math.pow((next_location_z-massive_z),2)))*35.714*1000  # in kpc 
             #print "Clump with no candidates; its distance to the center of the disk (kpc)= "
             #print D
             thisClump["distance"] = D 
             counter_clumps_nocandidate            += 1
                 
       clumps_collections.append(thisClump)

else:
    print "no clumps"
'''
report with n# candidates each case, multiples, no candidates
'''
print "Report:"
print "# clumps  : " + "%.1f" % total_clumps 
print "# clumps with unique candidate: " + "%.1f" %  unique_clumps   
print "# clumps with more than one candidate: " + "%.1f" % non_unique_clumps 
print "# clumps with candidates outside radious : " + "%.1f" %clumps_outside                  


print "clumps" 
for thisClump in clumps_collections:
       print "clump:" 
       print thisClump["clump"]
       if thisClump["unique"]:
           print "Unique clump"
           for clmp in thisClump["unique"]:
               print clmp
       if thisClump["candidates"]:
           print "Clumps with mass between 50% and 150%"
           for clmp in thisClump["candidates"]:
               print clmp        
       if(thisClump["masses"] ):
           print "Mass of the candidates "  
           print thisClump["masses"]  
       if(thisClump["distance"] ):
           print "Clump with no candidates; its distance to the center of the disk (kpc)= "  
           print thisClump["distance"]  
       print "-------------------------"                          


#print json.dumps(clumps_collections, indent=4)


