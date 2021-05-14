import gmplot

#create map Showalter Location
gmap = gmplot.GoogleMapPlotter(39.168451, -86.51891, 15)

#Lindely Hall 
l1 = (39.165341, -86.523588)
#Luddy Hall
l2 = (39.172725, -86.523295)

#Indiana University -- Musical Arts Center
l3 = (39.1666, -86.5176)

#list of points
lats = [l1[0],l2[0],l3[0]]
lons = [l1[1],l2[1],l3[1]]

#add points to map
gmap.scatter(lats,lons,'red', size = 30, marker = False)
#add line
gmap.plot(lats,lons,'cornflowerblue', size = 30, marker = False)
#save to map
gmap.draw("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Assignment9/hellobloomington.html")

#I Think I got it right, but I'm not sure, ask