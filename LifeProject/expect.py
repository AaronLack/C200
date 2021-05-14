# Notes/Plan:

# 1. Figure out most reliable sorting method
# 2. Write a loop which will average life expectancy
# 3. Set year vairalbe; while year == year_int
# 4. Average: (value in male + values in female)/2; This runs in smallest function
# 5. Plot data 


# Cant read the whole file and then process the data
# read whole file, but don't store all info in 1 variable and then process it
# Each column sould be a variable to read in
# Extract the data as you read the files


# write a function given 2 paramaters (state, county) generates a plot of the 
# life expectancy rates for that county for years 1985-2010

import matplotlib.pyplot as plt

filename = "IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"

import csv
with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv", "r", newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row['State'], row['County'], row['fips'], row['Year'], row['Female life expectancy (years)'], row['Female life expectancy (national, years)'], row['Female life expectancy (state, years)'], row['Male life expectancy (years)'], row['Male life expectancy (national, years)'], row['Male life expectancy (state, years)'])
       


# This reads the file line by line instead of reading it all at once,
# This is why I set many variables such as worst, state, county, and average
def worst_county(year):
    with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv", "r", newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        worst = 100                 #Set something higher than it can actually be
        state = ""                  #Set the empty string 
        county = ""                 #Set as an empty string
        average = 110               #Set something higher than it can actually be
        for row in reader:
            average = ((float(row['Female life expectancy (years)']) + float(row['Male life expectancy (years)'])) /2)
            if int(row['Year']) == year:
                if average < worst:
                    worst = average
                    state = row['State']
                    county = row['County']               
    return (state,county)

# Scatter is best for this
# Plotting 6 data types, a seperate color for the gender and a seperate symbol for county/state/national
def plotdata(state,county):
    with open("/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv", "r", newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        plots = csv.reader(csvfile, delimiter = ',')
        
        #Start assigning variables an empty list for plotting
        years = []
        male_county = []
        male_state = []
        male_national = []
        female_county = []
        female_state = []
        female_national = []

        for row in plots:
            if row[1] == county and row[0] == state:   #This will only plot West Virginia McDowell County
                years.append(row[3])                   #Year: x-axis
                female_county.append(row[4])           #Female life expectancy (years)
                female_national.append(row[5])         #Female life expectancy (national,years)
                female_state.append(row[6])            #Female life expectancy (state,years)
                male_county.append(row[7])             #Male life expectancy (years)
                male_national.append(row[8])           #Male life expectancy (national,years)
                male_state.append(row[9])              #Female life expectancy (state,years)
                                        
        # This slices so that we start at the data and not the row headingss
        years = years[1:]
        female_county = female_county[1:]
        female_national = female_national[1:]
        female_state = female_state[1:]
        male_county = male_county[1:]
        male_national = male_national[1:]
        male_state = male_state[1:]


        # Outside the for loop
        # List comprehension for converting i into a float to properly plot the data
        years = [float(i) for i in years]
        female_county = [float(i) for i in female_county]
        female_national = [float(i) for i in female_national]
        female_state = [float(i) for i in female_state]
        male_county = [float(i) for i in male_county]
        male_national = [float(i) for i in male_national]
        male_state = [float(i) for i in male_state]

        # Store to a variable to call when making a legend
        plt.figure(figsize = (12,7))
        p1, = plt.plot(years,female_county, 'r', label = "Female life expectancy (years)")
        p2, = plt.plot(years,female_national, 'r--', label = "Female life expectancy (national,years)")
        p3, = plt.plot(years, female_state, 'r.', label = "Female life expectancy (state,years)")
        p4, = plt.plot(years, male_county, 'b', label = "Male life expectancy (years)")
        p5, = plt.plot(years, male_national, 'b--', label = "Male life expectancy (national,years)")
        p6, = plt.plot(years, male_state, 'b.', label = "Male life expectancy (state, years)")
        
        plt.legend(loc = 'upper left', bbox_to_anchor=(-.1,1.15), labelspacing=.2)
        plt.xlabel('Years')
        plt.ylabel('Life Expectancy')
        plt.title('McDowell County, West Virginia')
        plt.savefig('/Users/Aaron/Desktop/Computer Science/C200/C200-Assignments-alack/Life/state_county.png', dpi = 500)  #Saves as a png
        plt.show()
    

if __name__ == "__main__":
    state,county = worst_county(2010)
    print(state,county)
    plotdata(state,county)