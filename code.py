# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
damages_updated = []
def damages_in_usd(damages):
  
  for num in damages:
    if num[-1] == 'B':
      damages_updated.append(float(num[:-1]) * conversion['M'])
    elif num[-1] == 'M':
      damages_updated.append(float(num[:-1]) * conversion['M'])
    else:
      damages_updated.append(num)
  return damages_updated

print(damages_in_usd(damages))

# 2 
# Create a Table
hurricane_data = {}
def hurr_record(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths):
  for i in range(len(names)):
    abc={"Name": names[i], "Month": months[i], "Year": years[i], "Max_sustained_winds": max_sustained_winds[i], "Areas_affected":  areas_affected[i], "Damage": damages_updated[i], "Death_count": deaths[i]} 

    hurricane_data[names[i]]= abc

hurr_record(names,months,years,max_sustained_winds,areas_affected,damages_updated,deaths)

print(len(hurricane_data))
#print(hurricane_data.keys())
#print(hurricane_data.values())
for key,value in hurricane_data.items():
  print("________________________________________________________________________________________________________________________________________")
  print(key,':',value)

print("_______________________________________________________________________________________________________________________")
# 3
# Organizing by Year
year_dict=[]
def hurricane_by_year(year):
  for i in hurricane_data:
    if hurricane_data[i]["Year"] == year:
      year_dict.append(hurricane_data[i])
  return hurricane_by_year
#years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]
hurricane_by_year(2017)
hurricane_by_year(1924)
for i in year_dict:
  print(i)
print("_______________________________________________________________________________________________________________________")
# 4
# Counting Damaged Areas

affected_area_count = {}
def area(areas_affected):
  for i in areas_affected:
    for j in i:
      if j not in affected_area_count:
        affected_area_count[j] = 1
      else:
        affected_area_count[j] += 1

affected_area = area(areas_affected)    
print(affected_area_count)
for key,value in affected_area_count.items():
  print("The number of Areas Affected by Hurricanes are--" + key,":",value)

print("_______________________________________________________________________________________________________________________")
# 5 
# Calculating Maximum Hurricane Count
def most_hurricanes_area(affected_area_count):
  maximum_num = max(affected_area_count.values())
  for i in affected_area_count:
    if affected_area_count[i] == maximum_num:
      max_area = i  
  return "The maximum num of hurricane was {value} on {key}".format(key = max_area, value = maximum_num)

max_value = most_hurricanes_area(affected_area_count)
print(max_value)

print("_______________________________________________________________________________________________________________________")
# 6
# Calculating the Deadliest Hurricane
def num_death_hurricane(deaths):
  max_deaths_area = ''
  max_death_count = 0
  for i, j in hurricane_data.items():
    if max_death_count < hurricane_data[i]["Death_count"]:
      max_deaths_area = i
      max_death_count = hurricane_data[i]["Death_count"]

    
  return "The maximum num of death was {value} by {key} hurricane".format(key = max_deaths_area, value = max_death_count)

deaths_num = num_death_hurricane(deaths)
print(deaths_num)

print("_______________________________________________________________________________________________________________________")

# 7
# Rating Hurricanes by Mortality
dictionary_mortality_rate = {}
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
list_hurricane1 = []
list_hurricane2 = []
list_hurricane3 = []
list_hurricane4 = []
list_hurricane5 = []
deaths.sort()

def mortality_rate(hurricane_data):
  for i, j in hurricane_data.items():
    if hurricane_data[i]["Death_count"] > 0 and hurricane_data[i]["Death_count"] <= 100:
      list_hurricane1.append(i)
      dictionary_mortality_rate[0] = list_hurricane1

    elif hurricane_data[i]["Death_count"] > 100 and hurricane_data[i]["Death_count"] <= 500:
      list_hurricane2.append(i)
      dictionary_mortality_rate[1] = list_hurricane2

    elif hurricane_data[i]["Death_count"] > 500 and hurricane_data[i]["Death_count"] <= 1000:
      list_hurricane3.append(i)
      dictionary_mortality_rate[2] = list_hurricane3

    elif hurricane_data[i]["Death_count"] > 1000 and hurricane_data[i]["Death_count"] <= 10000:
      list_hurricane4.append(i)
      dictionary_mortality_rate[3] = list_hurricane4

    elif hurricane_data[i]["Death_count"] > 10000:
      list_hurricane5.append(i)
      dictionary_mortality_rate[4] = list_hurricane5

  return dictionary_mortality_rate

print(mortality_rate(hurricane_data))
    
print("_______________________________________________________________________________________________________________________")

# 8 Calculating Hurricane Maximum Damage
def hurricane_damage(hurricane_data):
  max_damage = 0.0
  for i, j in hurricane_data.items():
    if hurricane_data[i]['Damage'] != 'Damages not recorded':
      if hurricane_data[i]['Damage'] > max_damage:
        hurricane = i
        max_damage = hurricane_data[i]['Damage']
  return "The greatest damage was {} USD caused by {}".format(max_damage, hurricane)

print(hurricane_damage(hurricane_data))

print("_______________________________________________________________________________________________________________________")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
dictionary_damage_rate = {}

def damage_rate(hurricane_data):
  range_damage1 = 0
  range_damage2 = 0
  range_damage3 = 0
  range_damage4 = 0
  range_damage5 = 0

  for i, j in hurricane_data.items():
    if hurricane_data[i]['Damage'] != 'Damages not recorded':
      if hurricane_data[i]['Damage'] >= damage_scale[0] and hurricane_data[i]['Damage'] < damage_scale[1]:
    
        
        if hurricane_data[i]['Damage'] > range_damage1:
          range_damage1 = hurricane_data[i]['Damage']
          dictionary_damage_rate[0] = range_damage1

      elif hurricane_data[i]['Damage'] > damage_scale[1] and hurricane_data[i]['Damage'] < damage_scale[2]:
       
        if hurricane_data[i]['Damage'] > range_damage2:
          range_damage2 = hurricane_data[i]['Damage']
          dictionary_damage_rate[1] = range_damage2

      elif hurricane_data[i]['Damage'] > damage_scale[2] and hurricane_data[i]['Damage'] < damage_scale[3]:
        
        if hurricane_data[i]['Damage'] > range_damage3:
          range_damage3 = hurricane_data[i]['Damage']
          dictionary_damage_rate[2] = range_damage3

      elif hurricane_data[i]['Damage'] > damage_scale[3] and hurricane_data[i]['Damage'] < damage_scale[4]:
       
        if hurricane_data[i]['Damage'] > range_damage4:
          range_damage4 = hurricane_data[i]['Damage']
          dictionary_damage_rate[3] = range_damage4

      elif hurricane_data[i]['Damage'] > damage_scale[4]:
        
        if hurricane_data[i]['Damage'] > range_damage5:
          range_damage5 = hurricane_data[i]['Damage']
          dictionary_damage_rate[4] = range_damage5
        
  return dictionary_damage_rate

print(damage_rate(hurricane_data))




    
   
