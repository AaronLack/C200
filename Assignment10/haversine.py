#change lat,lon to radians
import math
from math import radians, sin, cos, sqrt, asin 

### TODO: Answer Questions in comments here
# DD accounts for error but not hd.
# Drawbacks is the error is only calculated the further north you go and not in any other directions.  
# No I am not suprised the Euclidian distance is inaccurate because it does not use trig to take into account Earth's shape.  

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    r = 3961 # radius in miles
    p1 = (loc2[0] - loc1[0]) /2
    p2 = (loc2[1] - loc1[1]) /2
    d = (math.sin(p1)**2) + (math.cos(loc1[0]) * (math.cos(loc2[0])) * (math.sin(p2)**2))
    d1 = 2 * r * math.asin(d**(1/2))
    return radians(d1)



def dd(loc1,loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    """
    Euclidian Distance Forumula
    """
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))


if __name__ == "__main__":
    #Lindley Hall where we had C200
    l1 = (39.165341,-86.523588)

    #Luddy Hall the new Luddy building, where we have C200
    l2 = (39.172725,-86.523295)

    #Distance between Lindley and Luddy
    print(hd(l1,l2))
    print(eu_distance(l1,l2))
    print(dd(l1,l2))