

```python
# Dependencies for Weather
import requests as req
import openweathermapy.core as owm
from citipy import citipy
#Dependencies for random coordinates
import random
from random import uniform
#Dependencies for Df and Analysis
import numpy as np
import pandas as pd
#Dependencies for Plots
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
#Dependencies for api key
from config import api_key
```


```python
#Define max value for the initial range and sample size
max_coord = 1500
sample = 500
```


```python
#Generate random latitude coordinates with a function
def lat_coordinates():
    return random.uniform(-90,90)
random_lat_coord = [lat_coordinates() for latitude in range(max_coord)]
#random_lat_coord[0]
#Generate random longitude coordinates with a function
def long_coordinates():
    return random.uniform(-180,180)
random_long_coord = [long_coordinates() for longitude in range(max_coord)]
#random_long_coord[0]
#len(random_long_coord)
#len(random_lat_coord)
```


```python
# Functions to remove duplicated elements.I decided not to use this here because of future merging problems in the DF
#test the function random_lat_coord = [2,2,3,4,4,8]
#def Remove(_):
    #latitude_coord = []
    #for coordenate in random_lat_coord:
        #if coordenate not in latitude_coord:
            #latitude_coord.append(coordenate)
    #return latitude_coord
#latitude = Remove(random_lat_coord)
#latitude

#def Remove(_):
    #longitude_coord = []
    #for coordenate in random_long_coord:
        #if coordenate not in longitude_coord:
            #longitude_coord.append(coordenate)
    #return longitude_coord
#longitude = Remove(random_lat_coord)
#longitude
```


```python
#Rename the coordenates list 
latitude = random_lat_coord
longitude = random_long_coord
```


```python
#Test the function to return city and country
#city= citipy.nearest_city(latitude[0],longitude[0])
#city
#city.city_name
#city.country_code
```


```python
#Generate city names for the lat and long coordenates above
city_names = []
for x in range(0,max_coord):
    city_name = citipy.nearest_city(latitude[x],longitude[x])
    city_names.append(city_name)
#city_names

#Generate the city and country lists 
city_list = []
for x in range(0,max_coord):
    city = city_names[x].city_name
    #print(city_names[x].city_name)
    city_list.append(city)

country_list = []
for y in range(0,max_coord):
    country = city_names[y].country_code
    #print(city_names[y].country_code)
    country_list.append(country)

#Generate Dataframe
location_df = pd.DataFrame()

location_df["Latitude"] = ""
location_df["Longitude"] = ""
location_df['City'] = ''
location_df['Country Code'] = ''
location_df = location_df.append(pd.DataFrame.from_dict({"Latitude":latitude,"Longitude":longitude,"City":city_list,"Country Code":country_list,}))
location_df = location_df.reset_index(drop=True)
location_df.shape
#location_df

#Clean the data, drop the duplicated citites and reindex
drop_location_df = location_df.drop_duplicates(['City'])
drop_location_df.shape
new_location_df = drop_location_df.sample(sample)
city_coordinates_df = new_location_df.reset_index(drop=True)

#See the random coordenates in the map for the nearest cities:
import cartopy.crs as ccrs

fig, ax = plt.subplots(figsize = (20,10))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.scatter(list(city_coordinates_df['Longitude']),list(city_coordinates_df['Latitude']), color='red', marker = 'x', transform = ccrs.Geodetic(),)

plt.title('Distribution of 500 random cities')
plt.savefig('50 Cities in the world')
plt.show()
```


![png](output_6_0.png)



```python
#Set the URL
url = "http://api.openweathermap.org/data/2.5/weather?"

#Set the parameters
units = 'imperial'
settings = {"units":"imperial", "appid" :api_key}
```


```python
# Testing the api_key -> Get current weather for first city in the initial city list
try:
    current_weather = owm.get_current(city_list[0], **settings)
    print("Current temperature (F) for %s:" %(city_list[0]).capitalize())
    print(current_weather['main']['temp'])
except:
    print('HTTP Error: Not Found')
```

    Current temperature (F) for Tiksi:
    -21.92



```python
#city_coordinates_df.head()
```


```python
#Requesting weather data for all the cities in the list. I should iterate through all the list
for index, row in city_coordinates_df.iterrows():    
    
    #Set parameters for the query
    city = row['City']
    country = row['Country Code']
    settings['q'] =f"{city},{country}"
    
    #Query the url
    #query_url = "%s%sappid=%s&units=%s&q="%(url,api_key,units,city)
    query_url = f"{url}appid={api_key}&units={units}&q="
    
    # Request information to the endpoint and prit response
    print(f"Retrieve Weather Parameters for: {settings['q']}")
    WeatherPy_response = req.get(query_url + city)
    print(WeatherPy_response.url)
    
    #Create json response
    WeatherPy_response  = WeatherPy_response.json()
    
    #Set values for Temperature, Humidity, Cloudiness, Wind Speed, Latitude and Longitude
    city_coordinates_df.set_value(index,"Temperature",WeatherPy_response.get("main",{}).get("temp_max"))
    city_coordinates_df.set_value(index,"Humidity",WeatherPy_response.get("main",{}).get("humidity"))
    city_coordinates_df.set_value(index,"Cloudiness",WeatherPy_response.get("clouds",{}).get("all"))
    city_coordinates_df.set_value(index,"Wind Speed",WeatherPy_response.get("wind",{}).get("speed"))
    city_coordinates_df.set_value(index,"Latitude",WeatherPy_response.get("coord",{}).get("lat"))
    city_coordinates_df.set_value(index,"Longitude",WeatherPy_response.get("coord",{}).get("lon"))
    
```

    Retrieve Weather Parameters for: saint-philippe,re
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-philippe
    Retrieve Weather Parameters for: inuvik,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=inuvik
    Retrieve Weather Parameters for: kudahuvadhoo,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kudahuvadhoo
    Retrieve Weather Parameters for: gizo,sb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gizo
    Retrieve Weather Parameters for: kalundborg,dk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kalundborg
    Retrieve Weather Parameters for: mount isa,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mount%20isa
    Retrieve Weather Parameters for: hof,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hof
    Retrieve Weather Parameters for: popondetta,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=popondetta
    Retrieve Weather Parameters for: port lincoln,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20lincoln
    Retrieve Weather Parameters for: tokur,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tokur
    Retrieve Weather Parameters for: tarakan,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tarakan
    Retrieve Weather Parameters for: abha,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abha
    Retrieve Weather Parameters for: banmo,mm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=banmo
    Retrieve Weather Parameters for: orotukan,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=orotukan
    Retrieve Weather Parameters for: peniche,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=peniche
    Retrieve Weather Parameters for: saint-augustin,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-augustin
    Retrieve Weather Parameters for: esik,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=esik
    Retrieve Weather Parameters for: huarmey,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=huarmey
    Retrieve Weather Parameters for: barrow,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barrow
    Retrieve Weather Parameters for: vaini,to
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vaini
    Retrieve Weather Parameters for: lorengau,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lorengau
    Retrieve Weather Parameters for: lasa,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lasa
    Retrieve Weather Parameters for: upernavik,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=upernavik
    Retrieve Weather Parameters for: hokitika,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hokitika
    Retrieve Weather Parameters for: nata,bw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nata
    Retrieve Weather Parameters for: esperance,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=esperance
    Retrieve Weather Parameters for: kalmunai,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kalmunai
    Retrieve Weather Parameters for: bagenalstown,ie
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bagenalstown
    Retrieve Weather Parameters for: mindyak,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mindyak
    Retrieve Weather Parameters for: kuytun,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kuytun
    Retrieve Weather Parameters for: cape town,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cape%20town
    Retrieve Weather Parameters for: agirish,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=agirish
    Retrieve Weather Parameters for: verkhoturye,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=verkhoturye
    Retrieve Weather Parameters for: taos,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taos
    Retrieve Weather Parameters for: provideniya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=provideniya
    Retrieve Weather Parameters for: torbay,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=torbay
    Retrieve Weather Parameters for: beringovskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beringovskiy
    Retrieve Weather Parameters for: aripuana,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aripuana
    Retrieve Weather Parameters for: rio grande,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rio%20grande
    Retrieve Weather Parameters for: punta cardon,ve
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=punta%20cardon
    Retrieve Weather Parameters for: qasigiannguit,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qasigiannguit
    Retrieve Weather Parameters for: vaitupu,wf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vaitupu
    Retrieve Weather Parameters for: gunjur,gm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gunjur
    Retrieve Weather Parameters for: belmonte,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=belmonte
    Retrieve Weather Parameters for: iqaluit,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=iqaluit
    Retrieve Weather Parameters for: arraial do cabo,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=arraial%20do%20cabo
    Retrieve Weather Parameters for: back mountain,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=back%20mountain
    Retrieve Weather Parameters for: bosaso,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bosaso
    Retrieve Weather Parameters for: bac lieu,vn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bac%20lieu
    Retrieve Weather Parameters for: richards bay,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=richards%20bay
    Retrieve Weather Parameters for: batagay-alyta,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=batagay-alyta
    Retrieve Weather Parameters for: tsihombe,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tsihombe
    Retrieve Weather Parameters for: kovdor,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kovdor
    Retrieve Weather Parameters for: pisco,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pisco
    Retrieve Weather Parameters for: cam ranh,vn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cam%20ranh
    Retrieve Weather Parameters for: barawe,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barawe
    Retrieve Weather Parameters for: pevek,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pevek
    Retrieve Weather Parameters for: okhotsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=okhotsk
    Retrieve Weather Parameters for: amga,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=amga
    Retrieve Weather Parameters for: verkhnevilyuysk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=verkhnevilyuysk
    Retrieve Weather Parameters for: kahului,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kahului
    Retrieve Weather Parameters for: turukhansk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=turukhansk
    Retrieve Weather Parameters for: kraskino,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kraskino
    Retrieve Weather Parameters for: nuristan,af
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nuristan
    Retrieve Weather Parameters for: yulara,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yulara
    Retrieve Weather Parameters for: grand river south east,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=grand%20river%20south%20east
    Retrieve Weather Parameters for: atuona,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=atuona
    Retrieve Weather Parameters for: ringkobing,dk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ringkobing
    Retrieve Weather Parameters for: aksarayskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aksarayskiy
    Retrieve Weather Parameters for: oussouye,sn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oussouye
    Retrieve Weather Parameters for: krasnoselkup,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=krasnoselkup
    Retrieve Weather Parameters for: bubaque,gw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bubaque
    Retrieve Weather Parameters for: ayr,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ayr
    Retrieve Weather Parameters for: nizhniy kuranakh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nizhniy%20kuranakh
    Retrieve Weather Parameters for: dunedin,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dunedin
    Retrieve Weather Parameters for: benguela,ao
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=benguela
    Retrieve Weather Parameters for: ilulissat,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ilulissat
    Retrieve Weather Parameters for: rungata,ki
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rungata
    Retrieve Weather Parameters for: ust-kamchatsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ust-kamchatsk
    Retrieve Weather Parameters for: boende,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=boende
    Retrieve Weather Parameters for: vila franca do campo,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vila%20franca%20do%20campo
    Retrieve Weather Parameters for: khonuu,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khonuu
    Retrieve Weather Parameters for: black river,jm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=black%20river
    Retrieve Weather Parameters for: kananga,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kananga
    Retrieve Weather Parameters for: sao felix do xingu,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sao%20felix%20do%20xingu
    Retrieve Weather Parameters for: arbroath,gb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=arbroath
    Retrieve Weather Parameters for: laguna de perlas,ni
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=laguna%20de%20perlas
    Retrieve Weather Parameters for: muravlenko,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=muravlenko
    Retrieve Weather Parameters for: the valley,ai
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=the%20valley
    Retrieve Weather Parameters for: nanton,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nanton
    Retrieve Weather Parameters for: havoysund,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=havoysund
    Retrieve Weather Parameters for: samusu,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=samusu
    Retrieve Weather Parameters for: xiangxiang,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=xiangxiang
    Retrieve Weather Parameters for: farafangana,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=farafangana
    Retrieve Weather Parameters for: amderma,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=amderma
    Retrieve Weather Parameters for: krasnaya gora,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=krasnaya%20gora
    Retrieve Weather Parameters for: honningsvag,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=honningsvag
    Retrieve Weather Parameters for: galle,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=galle
    Retrieve Weather Parameters for: barcelos,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barcelos
    Retrieve Weather Parameters for: luderitz,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=luderitz
    Retrieve Weather Parameters for: kemijarvi,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kemijarvi
    Retrieve Weather Parameters for: yangjiang,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yangjiang
    Retrieve Weather Parameters for: buala,sb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=buala
    Retrieve Weather Parameters for: alakurtti,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alakurtti
    Retrieve Weather Parameters for: coahuayana,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coahuayana
    Retrieve Weather Parameters for: san patricio,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20patricio
    Retrieve Weather Parameters for: hilo,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hilo
    Retrieve Weather Parameters for: chuy,uy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chuy
    Retrieve Weather Parameters for: taltal,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taltal
    Retrieve Weather Parameters for: formiga,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=formiga
    Retrieve Weather Parameters for: tiarei,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tiarei
    Retrieve Weather Parameters for: general roca,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=general%20roca
    Retrieve Weather Parameters for: dolbeau,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dolbeau
    Retrieve Weather Parameters for: shahrud,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shahrud
    Retrieve Weather Parameters for: hauterive,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hauterive
    Retrieve Weather Parameters for: sitka,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sitka
    Retrieve Weather Parameters for: yellowknife,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yellowknife
    Retrieve Weather Parameters for: geraldton,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=geraldton
    Retrieve Weather Parameters for: kaputa,zm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaputa
    Retrieve Weather Parameters for: zaysan,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zaysan
    Retrieve Weather Parameters for: kurinjippadi,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kurinjippadi
    Retrieve Weather Parameters for: zapolyarnyy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zapolyarnyy
    Retrieve Weather Parameters for: hervey bay,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hervey%20bay
    Retrieve Weather Parameters for: grand gaube,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=grand%20gaube
    Retrieve Weather Parameters for: saint-joseph,re
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-joseph
    Retrieve Weather Parameters for: rabak,sd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rabak
    Retrieve Weather Parameters for: kiunga,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kiunga
    Retrieve Weather Parameters for: bacolod,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bacolod
    Retrieve Weather Parameters for: kapaa,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kapaa
    Retrieve Weather Parameters for: northport,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=northport
    Retrieve Weather Parameters for: khandyga,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khandyga
    Retrieve Weather Parameters for: cumaribo,co
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cumaribo
    Retrieve Weather Parameters for: teya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=teya
    Retrieve Weather Parameters for: yenagoa,ng
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yenagoa
    Retrieve Weather Parameters for: candawaga,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=candawaga
    Retrieve Weather Parameters for: roros,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=roros
    Retrieve Weather Parameters for: lolua,tv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lolua
    Retrieve Weather Parameters for: gorontalo,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gorontalo
    Retrieve Weather Parameters for: umzimvubu,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=umzimvubu
    Retrieve Weather Parameters for: ramnagar,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ramnagar
    Retrieve Weather Parameters for: coihaique,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coihaique
    Retrieve Weather Parameters for: sept-iles,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sept-iles
    Retrieve Weather Parameters for: cayenne,gf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cayenne
    Retrieve Weather Parameters for: akdepe,tm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=akdepe
    Retrieve Weather Parameters for: gencsapati,hu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gencsapati
    Retrieve Weather Parameters for: vardo,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vardo
    Retrieve Weather Parameters for: kirakira,sb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kirakira
    Retrieve Weather Parameters for: jawar,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jawar
    Retrieve Weather Parameters for: luganville,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=luganville
    Retrieve Weather Parameters for: cabra,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cabra
    Retrieve Weather Parameters for: santa lucia,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=santa%20lucia
    Retrieve Weather Parameters for: saldanha,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saldanha
    Retrieve Weather Parameters for: zhigalovo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zhigalovo
    Retrieve Weather Parameters for: aginskoye,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aginskoye
    Retrieve Weather Parameters for: ozgon,kg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ozgon
    Retrieve Weather Parameters for: toliary,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=toliary
    Retrieve Weather Parameters for: malinovoye ozero,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=malinovoye%20ozero
    Retrieve Weather Parameters for: mandalgovi,mn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mandalgovi
    Retrieve Weather Parameters for: adeje,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=adeje
    Retrieve Weather Parameters for: lakatoro,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lakatoro
    Retrieve Weather Parameters for: taoudenni,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taoudenni
    Retrieve Weather Parameters for: hendijan,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hendijan
    Retrieve Weather Parameters for: bethel,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bethel
    Retrieve Weather Parameters for: angra,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=angra
    Retrieve Weather Parameters for: ambunti,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ambunti
    Retrieve Weather Parameters for: soe,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=soe
    Retrieve Weather Parameters for: nizhneyansk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nizhneyansk
    Retrieve Weather Parameters for: isiro,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=isiro
    Retrieve Weather Parameters for: hithadhoo,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hithadhoo
    Retrieve Weather Parameters for: attawapiskat,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=attawapiskat
    Retrieve Weather Parameters for: ginda,er
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ginda
    Retrieve Weather Parameters for: road town,vg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=road%20town
    Retrieve Weather Parameters for: skjervoy,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=skjervoy
    Retrieve Weather Parameters for: bud,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bud
    Retrieve Weather Parameters for: araouane,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=araouane
    Retrieve Weather Parameters for: hay river,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hay%20river
    Retrieve Weather Parameters for: nabire,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nabire
    Retrieve Weather Parameters for: hue,vn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hue
    Retrieve Weather Parameters for: kuopio,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kuopio
    Retrieve Weather Parameters for: ponta do sol,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ponta%20do%20sol
    Retrieve Weather Parameters for: zatoka,ua
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zatoka
    Retrieve Weather Parameters for: beipiao,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beipiao
    Retrieve Weather Parameters for: souillac,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=souillac
    Retrieve Weather Parameters for: cody,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cody
    Retrieve Weather Parameters for: sungaipenuh,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sungaipenuh
    Retrieve Weather Parameters for: kangaatsiaq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kangaatsiaq
    Retrieve Weather Parameters for: kununurra,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kununurra
    Retrieve Weather Parameters for: uruzgan,af
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=uruzgan
    Retrieve Weather Parameters for: burica,pa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=burica
    Retrieve Weather Parameters for: nanortalik,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nanortalik
    Retrieve Weather Parameters for: cidreira,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cidreira
    Retrieve Weather Parameters for: el alto,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=el%20alto
    Retrieve Weather Parameters for: formosa,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=formosa
    Retrieve Weather Parameters for: airai,pw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=airai
    Retrieve Weather Parameters for: buraydah,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=buraydah
    Retrieve Weather Parameters for: akyab,mm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=akyab
    Retrieve Weather Parameters for: ajka,hu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ajka
    Retrieve Weather Parameters for: harsin,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=harsin
    Retrieve Weather Parameters for: lompoc,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lompoc
    Retrieve Weather Parameters for: avarua,ck
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=avarua
    Retrieve Weather Parameters for: dandong,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dandong
    Retrieve Weather Parameters for: high level,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=high%20level
    Retrieve Weather Parameters for: sztum,pl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sztum
    Retrieve Weather Parameters for: louisbourg,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=louisbourg
    Retrieve Weather Parameters for: tilichiki,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tilichiki
    Retrieve Weather Parameters for: longlac,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=longlac
    Retrieve Weather Parameters for: neiafu,to
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=neiafu
    Retrieve Weather Parameters for: molokovo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=molokovo
    Retrieve Weather Parameters for: tiksi,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tiksi
    Retrieve Weather Parameters for: kruisfontein,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kruisfontein
    Retrieve Weather Parameters for: dinsor,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dinsor
    Retrieve Weather Parameters for: daru,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=daru
    Retrieve Weather Parameters for: minab,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=minab
    Retrieve Weather Parameters for: ormara,pk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ormara
    Retrieve Weather Parameters for: grand baie,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=grand%20baie
    Retrieve Weather Parameters for: santiago,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=santiago
    Retrieve Weather Parameters for: elesbao veloso,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=elesbao%20veloso
    Retrieve Weather Parameters for: dekoa,cf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dekoa
    Retrieve Weather Parameters for: garowe,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=garowe
    Retrieve Weather Parameters for: tuatapere,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tuatapere
    Retrieve Weather Parameters for: saint-georges,gf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-georges
    Retrieve Weather Parameters for: dikson,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dikson
    Retrieve Weather Parameters for: tautira,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tautira
    Retrieve Weather Parameters for: lufilufi,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lufilufi
    Retrieve Weather Parameters for: bambanglipuro,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bambanglipuro
    Retrieve Weather Parameters for: mitsamiouli,km
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mitsamiouli
    Retrieve Weather Parameters for: mutsamudu,km
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mutsamudu
    Retrieve Weather Parameters for: douentza,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=douentza
    Retrieve Weather Parameters for: chernyshevskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chernyshevskiy
    Retrieve Weather Parameters for: maldonado,uy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maldonado
    Retrieve Weather Parameters for: bulqize,al
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bulqize
    Retrieve Weather Parameters for: mahebourg,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mahebourg
    Retrieve Weather Parameters for: aksarka,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aksarka
    Retrieve Weather Parameters for: portland,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=portland
    Retrieve Weather Parameters for: mar del plata,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mar%20del%20plata
    Retrieve Weather Parameters for: pelotas,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pelotas
    Retrieve Weather Parameters for: katsuura,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=katsuura
    Retrieve Weather Parameters for: oktyabrskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oktyabrskiy
    Retrieve Weather Parameters for: oregon city,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oregon%20city
    Retrieve Weather Parameters for: sur,om
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sur
    Retrieve Weather Parameters for: san-pedro,ci
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san-pedro
    Retrieve Weather Parameters for: naze,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=naze
    Retrieve Weather Parameters for: nuuk,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nuuk
    Retrieve Weather Parameters for: clyde river,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=clyde%20river
    Retrieve Weather Parameters for: fountain hills,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fountain%20hills
    Retrieve Weather Parameters for: marcona,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marcona
    Retrieve Weather Parameters for: bursol,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bursol
    Retrieve Weather Parameters for: port-cartier,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port-cartier
    Retrieve Weather Parameters for: pauini,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pauini
    Retrieve Weather Parameters for: nara,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nara
    Retrieve Weather Parameters for: rocha,uy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rocha
    Retrieve Weather Parameters for: saint george,bm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint%20george
    Retrieve Weather Parameters for: abu kamal,sy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abu%20kamal
    Retrieve Weather Parameters for: mayumba,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mayumba
    Retrieve Weather Parameters for: vikhorevka,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vikhorevka
    Retrieve Weather Parameters for: katangli,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=katangli
    Retrieve Weather Parameters for: alofi,nu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alofi
    Retrieve Weather Parameters for: cockburn town,tc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cockburn%20town
    Retrieve Weather Parameters for: udachnyy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=udachnyy
    Retrieve Weather Parameters for: salina,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=salina
    Retrieve Weather Parameters for: victoria,sc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=victoria
    Retrieve Weather Parameters for: resistencia,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=resistencia
    Retrieve Weather Parameters for: moiyabana,bw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=moiyabana
    Retrieve Weather Parameters for: georgiyevka,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=georgiyevka
    Retrieve Weather Parameters for: puerto leguizamo,co
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puerto%20leguizamo
    Retrieve Weather Parameters for: hambantota,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hambantota
    Retrieve Weather Parameters for: leningradskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=leningradskiy
    Retrieve Weather Parameters for: husavik,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=husavik
    Retrieve Weather Parameters for: vao,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vao
    Retrieve Weather Parameters for: ixtapa,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ixtapa
    Retrieve Weather Parameters for: illoqqortoormiut,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=illoqqortoormiut
    Retrieve Weather Parameters for: byron bay,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=byron%20bay
    Retrieve Weather Parameters for: praia da vitoria,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=praia%20da%20vitoria
    Retrieve Weather Parameters for: lobatse,bw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lobatse
    Retrieve Weather Parameters for: port alfred,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20alfred
    Retrieve Weather Parameters for: lanzhou,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lanzhou
    Retrieve Weather Parameters for: kodiak,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kodiak
    Retrieve Weather Parameters for: senanga,zm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=senanga
    Retrieve Weather Parameters for: san jeronimo,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20jeronimo
    Retrieve Weather Parameters for: lata,sb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lata
    Retrieve Weather Parameters for: elban,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=elban
    Retrieve Weather Parameters for: petit goave,ht
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=petit%20goave
    Retrieve Weather Parameters for: bluff,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bluff
    Retrieve Weather Parameters for: ukiah,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ukiah
    Retrieve Weather Parameters for: kenai,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kenai
    Retrieve Weather Parameters for: umea,se
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=umea
    Retrieve Weather Parameters for: jambusar,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jambusar
    Retrieve Weather Parameters for: masingbi,sl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=masingbi
    Retrieve Weather Parameters for: half moon bay,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=half%20moon%20bay
    Retrieve Weather Parameters for: bambous virieux,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bambous%20virieux
    Retrieve Weather Parameters for: el tocuyo,ve
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=el%20tocuyo
    Retrieve Weather Parameters for: codrington,ag
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=codrington
    Retrieve Weather Parameters for: kishi,ng
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kishi
    Retrieve Weather Parameters for: severo-kurilsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=severo-kurilsk
    Retrieve Weather Parameters for: xining,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=xining
    Retrieve Weather Parameters for: cherskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cherskiy
    Retrieve Weather Parameters for: shizunai,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shizunai
    Retrieve Weather Parameters for: berlevag,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=berlevag
    Retrieve Weather Parameters for: litovko,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=litovko
    Retrieve Weather Parameters for: basco,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=basco
    Retrieve Weather Parameters for: ormond beach,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ormond%20beach
    Retrieve Weather Parameters for: aklavik,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aklavik
    Retrieve Weather Parameters for: divnoye,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=divnoye
    Retrieve Weather Parameters for: williston,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=williston
    Retrieve Weather Parameters for: qaanaaq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qaanaaq
    Retrieve Weather Parameters for: adelaide,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=adelaide
    Retrieve Weather Parameters for: tasiilaq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tasiilaq
    Retrieve Weather Parameters for: saleaula,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saleaula
    Retrieve Weather Parameters for: naryan-mar,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=naryan-mar
    Retrieve Weather Parameters for: muhos,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=muhos
    Retrieve Weather Parameters for: nome,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nome
    Retrieve Weather Parameters for: sudogda,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sudogda
    Retrieve Weather Parameters for: kimbe,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kimbe
    Retrieve Weather Parameters for: morant bay,jm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=morant%20bay
    Retrieve Weather Parameters for: klaksvik,fo
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=klaksvik
    Retrieve Weather Parameters for: gobabis,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gobabis
    Retrieve Weather Parameters for: los llanos de aridane,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=los%20llanos%20de%20aridane
    Retrieve Weather Parameters for: santa rosa,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=santa%20rosa
    Retrieve Weather Parameters for: krechevitsy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=krechevitsy
    Retrieve Weather Parameters for: labuhan,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=labuhan
    Retrieve Weather Parameters for: lavrentiya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lavrentiya
    Retrieve Weather Parameters for: satitoa,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=satitoa
    Retrieve Weather Parameters for: homer,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=homer
    Retrieve Weather Parameters for: peterlee,gb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=peterlee
    Retrieve Weather Parameters for: albany,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=albany
    Retrieve Weather Parameters for: anchorage,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=anchorage
    Retrieve Weather Parameters for: bintulu,my
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bintulu
    Retrieve Weather Parameters for: verkhnyaya toyma,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=verkhnyaya%20toyma
    Retrieve Weather Parameters for: zambezi,zm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zambezi
    Retrieve Weather Parameters for: hermanus,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hermanus
    Retrieve Weather Parameters for: sentyabrskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sentyabrskiy
    Retrieve Weather Parameters for: kyabe,td
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kyabe
    Retrieve Weather Parameters for: mandan,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mandan
    Retrieve Weather Parameters for: damara,cf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=damara
    Retrieve Weather Parameters for: wyszkow,pl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=wyszkow
    Retrieve Weather Parameters for: la ronge,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=la%20ronge
    Retrieve Weather Parameters for: georgetown,sh
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=georgetown
    Retrieve Weather Parameters for: maltahohe,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maltahohe
    Retrieve Weather Parameters for: yongchang,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yongchang
    Retrieve Weather Parameters for: namatanai,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=namatanai
    Retrieve Weather Parameters for: fukue,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fukue
    Retrieve Weather Parameters for: ribeira grande,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ribeira%20grande
    Retrieve Weather Parameters for: fare,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fare
    Retrieve Weather Parameters for: dobryanka,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dobryanka
    Retrieve Weather Parameters for: longyearbyen,sj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=longyearbyen
    Retrieve Weather Parameters for: haapiti,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=haapiti
    Retrieve Weather Parameters for: karratha,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=karratha
    Retrieve Weather Parameters for: margate,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=margate
    Retrieve Weather Parameters for: madang,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=madang
    Retrieve Weather Parameters for: olafsvik,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=olafsvik
    Retrieve Weather Parameters for: tambul,sd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tambul
    Retrieve Weather Parameters for: hobart,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hobart
    Retrieve Weather Parameters for: price,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=price
    Retrieve Weather Parameters for: rampura,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rampura
    Retrieve Weather Parameters for: zhuhai,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zhuhai
    Retrieve Weather Parameters for: key west,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=key%20west
    Retrieve Weather Parameters for: narsaq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=narsaq
    Retrieve Weather Parameters for: mednogorskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mednogorskiy
    Retrieve Weather Parameters for: lumeje,ao
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lumeje
    Retrieve Weather Parameters for: nalut,ly
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nalut
    Retrieve Weather Parameters for: norman wells,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=norman%20wells
    Retrieve Weather Parameters for: sao filipe,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sao%20filipe
    Retrieve Weather Parameters for: ullapool,gb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ullapool
    Retrieve Weather Parameters for: port hedland,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20hedland
    Retrieve Weather Parameters for: biak,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=biak
    Retrieve Weather Parameters for: kathmandu,np
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kathmandu
    Retrieve Weather Parameters for: progreso,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=progreso
    Retrieve Weather Parameters for: bilibino,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bilibino
    Retrieve Weather Parameters for: borlange,se
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=borlange
    Retrieve Weather Parameters for: sola,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sola
    Retrieve Weather Parameters for: bandarbeyla,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bandarbeyla
    Retrieve Weather Parameters for: adrar,dz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=adrar
    Retrieve Weather Parameters for: port-gentil,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port-gentil
    Retrieve Weather Parameters for: port hardy,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20hardy
    Retrieve Weather Parameters for: batemans bay,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=batemans%20bay
    Retrieve Weather Parameters for: laguna,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=laguna
    Retrieve Weather Parameters for: srednekolymsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=srednekolymsk
    Retrieve Weather Parameters for: podosinovets,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=podosinovets
    Retrieve Weather Parameters for: qandala,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qandala
    Retrieve Weather Parameters for: saskylakh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saskylakh
    Retrieve Weather Parameters for: maputo,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maputo
    Retrieve Weather Parameters for: taolanaro,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taolanaro
    Retrieve Weather Parameters for: noyabrsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=noyabrsk
    Retrieve Weather Parameters for: yithion,gr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yithion
    Retrieve Weather Parameters for: dangtu,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dangtu
    Retrieve Weather Parameters for: tura,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tura
    Retrieve Weather Parameters for: harper,lr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=harper
    Retrieve Weather Parameters for: touros,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=touros
    Retrieve Weather Parameters for: abhar,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abhar
    Retrieve Weather Parameters for: angoram,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=angoram
    Retrieve Weather Parameters for: oksfjord,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oksfjord
    Retrieve Weather Parameters for: kaitangata,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaitangata
    Retrieve Weather Parameters for: melfort,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=melfort
    Retrieve Weather Parameters for: pumiao,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pumiao
    Retrieve Weather Parameters for: lodja,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lodja
    Retrieve Weather Parameters for: bargal,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bargal
    Retrieve Weather Parameters for: inhambane,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=inhambane
    Retrieve Weather Parameters for: kadoma,zw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kadoma
    Retrieve Weather Parameters for: hofn,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hofn
    Retrieve Weather Parameters for: atar,mr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=atar
    Retrieve Weather Parameters for: sabang,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sabang
    Retrieve Weather Parameters for: matagami,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=matagami
    Retrieve Weather Parameters for: alpoyeca,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alpoyeca
    Retrieve Weather Parameters for: oni,ge
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oni
    Retrieve Weather Parameters for: sao joao da barra,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sao%20joao%20da%20barra
    Retrieve Weather Parameters for: umm kaddadah,sd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=umm%20kaddadah
    Retrieve Weather Parameters for: shingu,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shingu
    Retrieve Weather Parameters for: isangel,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=isangel
    Retrieve Weather Parameters for: mananjary,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mananjary
    Retrieve Weather Parameters for: beruwala,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beruwala
    Retrieve Weather Parameters for: coos bay,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coos%20bay
    Retrieve Weather Parameters for: tarko-sale,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tarko-sale
    Retrieve Weather Parameters for: faanui,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=faanui
    Retrieve Weather Parameters for: timra,se
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=timra
    Retrieve Weather Parameters for: jiddah,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jiddah
    Retrieve Weather Parameters for: slave lake,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=slave%20lake
    Retrieve Weather Parameters for: terrace,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=terrace
    Retrieve Weather Parameters for: pointe-noire,gp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pointe-noire
    Retrieve Weather Parameters for: samalaeulu,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=samalaeulu
    Retrieve Weather Parameters for: ossora,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ossora
    Retrieve Weather Parameters for: puerto ayora,ec
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puerto%20ayora
    Retrieve Weather Parameters for: anito,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=anito
    Retrieve Weather Parameters for: barentsburg,sj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barentsburg
    Retrieve Weather Parameters for: umm lajj,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=umm%20lajj
    Retrieve Weather Parameters for: yanchukan,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yanchukan
    Retrieve Weather Parameters for: siuna,ni
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=siuna
    Retrieve Weather Parameters for: punta arenas,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=punta%20arenas
    Retrieve Weather Parameters for: abeche,td
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abeche
    Retrieve Weather Parameters for: doha,kw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=doha
    Retrieve Weather Parameters for: najran,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=najran
    Retrieve Weather Parameters for: lebu,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lebu
    Retrieve Weather Parameters for: abu dhabi,ae
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abu%20dhabi
    Retrieve Weather Parameters for: cuamba,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cuamba
    Retrieve Weather Parameters for: tres marias,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tres%20marias
    Retrieve Weather Parameters for: opuwo,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=opuwo
    Retrieve Weather Parameters for: timbiras,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=timbiras
    Retrieve Weather Parameters for: vila,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vila
    Retrieve Weather Parameters for: tezu,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tezu
    Retrieve Weather Parameters for: sisimiut,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sisimiut
    Retrieve Weather Parameters for: ostrovnoy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ostrovnoy
    Retrieve Weather Parameters for: beloha,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beloha
    Retrieve Weather Parameters for: maragogi,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maragogi
    Retrieve Weather Parameters for: vallenar,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vallenar
    Retrieve Weather Parameters for: mushie,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mushie
    Retrieve Weather Parameters for: santa luzia,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=santa%20luzia
    Retrieve Weather Parameters for: avera,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=avera
    Retrieve Weather Parameters for: fairview,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fairview
    Retrieve Weather Parameters for: rabo de peixe,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rabo%20de%20peixe
    Retrieve Weather Parameters for: nishihara,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nishihara
    Retrieve Weather Parameters for: ketchikan,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ketchikan
    Retrieve Weather Parameters for: porto novo,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=porto%20novo
    Retrieve Weather Parameters for: waingapu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=waingapu
    Retrieve Weather Parameters for: hanko,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hanko
    Retrieve Weather Parameters for: sechura,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sechura
    Retrieve Weather Parameters for: jacareacanga,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jacareacanga
    Retrieve Weather Parameters for: destin,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=destin
    Retrieve Weather Parameters for: haines junction,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=haines%20junction
    Retrieve Weather Parameters for: nogliki,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nogliki
    Retrieve Weather Parameters for: ancud,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ancud
    Retrieve Weather Parameters for: natal,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=natal
    Retrieve Weather Parameters for: kuche,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kuche
    Retrieve Weather Parameters for: haibowan,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=haibowan
    Retrieve Weather Parameters for: hovd,mn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hovd
    Retrieve Weather Parameters for: caravelas,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=caravelas
    Retrieve Weather Parameters for: mingshui,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mingshui
    Retrieve Weather Parameters for: rosetta,eg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rosetta
    Retrieve Weather Parameters for: padang,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=padang
    Retrieve Weather Parameters for: arlit,ne
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=arlit
    Retrieve Weather Parameters for: kilcormac,ie
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kilcormac
    Retrieve Weather Parameters for: villazon,bo
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=villazon
    Retrieve Weather Parameters for: busselton,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=busselton
    Retrieve Weather Parameters for: swarzedz,pl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=swarzedz
    Retrieve Weather Parameters for: redmond,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=redmond
    Retrieve Weather Parameters for: khorixas,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khorixas
    Retrieve Weather Parameters for: kutum,sd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kutum
    Retrieve Weather Parameters for: dolores,uy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dolores
    Retrieve Weather Parameters for: kavieng,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kavieng
    Retrieve Weather Parameters for: mocambique,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mocambique
    Retrieve Weather Parameters for: mataura,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mataura
    Retrieve Weather Parameters for: pangnirtung,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pangnirtung
    Retrieve Weather Parameters for: zorritos,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zorritos
    Retrieve Weather Parameters for: bengkulu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bengkulu
    Retrieve Weather Parameters for: kanchanaburi,th
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kanchanaburi
    Retrieve Weather Parameters for: quesnel,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=quesnel
    Retrieve Weather Parameters for: ahipara,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ahipara
    Retrieve Weather Parameters for: mehamn,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mehamn
    Retrieve Weather Parameters for: mount pleasant,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mount%20pleasant
    Retrieve Weather Parameters for: bowen,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bowen
    Retrieve Weather Parameters for: hede,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hede
    Retrieve Weather Parameters for: nenjiang,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nenjiang
    Retrieve Weather Parameters for: castro,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=castro
    Retrieve Weather Parameters for: marsh harbour,bs
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marsh%20harbour
    Retrieve Weather Parameters for: bagdarin,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bagdarin
    Retrieve Weather Parameters for: qaqortoq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qaqortoq
    Retrieve Weather Parameters for: seoni malwa,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=seoni%20malwa
    Retrieve Weather Parameters for: westport,ie
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=westport
    Retrieve Weather Parameters for: takoradi,gh
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=takoradi
    Retrieve Weather Parameters for: dwarka,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dwarka
    Retrieve Weather Parameters for: makakilo city,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=makakilo%20city
    Retrieve Weather Parameters for: dombarovskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dombarovskiy



```python
#Exception Handling
# What should I do if I can't retrieve information ....Drop na's cities.
city_coordinates_df2 = city_coordinates_df.dropna()

initial_df_sz= city_coordinates_df.shape[0]
final_df_sz= city_coordinates_df2.shape[0]

if initial_df_sz > final_df_sz:
    print("Oops, we couldn't retrieve the weather parameters for (%s) cities" %(initial_df_sz - final_df_sz))
    print("Your new DataFrame has the weather information for (%s) unique cities"%(final_df_sz))
    print('The DataFrame has been saved as WeatherPy2.csv')
    city_coordinates_df2.to_csv("WeatherPy2.csv")
else:
    print("We succesfully retrieve the weather information for all the random cities sample you requested")
    print('The DataFrame has been saved as WeatherPy.csv')
    city_coordinates_df2.to_csv("WeatherPy.csv")
```

    Oops, we couldn't retrieve the weather parameters for (53) cities
    Your new DataFrame has the weather information for (447) unique cities
    The DataFrame has been saved as WeatherPy2.csv



```python
#city_coordinates_df2
```


```python
print('----------1. Temperature vs. Latitude Scatterplot----------')
# Temperature vs Latitude 
city_coordinates_df2.plot(kind="scatter",x="Latitude",y="Temperature",s=35, marker = 'o', color = 'red', grid=True)
plt.suptitle('Temperature (F) vs. Latitude')
plt.title('Total cities plotted = %s'%(final_df_sz))
plt.ylim(city_coordinates_df2['Temperature'].min() - 10, 10 + city_coordinates_df2['Temperature'].max())
plt.xlim(-90, 90)
plt.axvline(0, color='gray',alpha=0.4)
plt.savefig("Temperature vs. Latitude.png")
plt.show()
```

    ----------1. Temperature vs. Latitude Scatterplot----------



![png](output_13_1.png)



```python
print('----------2. Humidity vs. Latitude Scatterplot----------')
# Temperature vs Latitude 
city_coordinates_df2.plot(kind="scatter",x="Latitude",y="Humidity",s=35, marker = 'o', color = 'gold', grid=True)
plt.suptitle('Humidity vs. Latitude')
plt.title('Total cities plotted = %s'%(final_df_sz))
plt.ylim(city_coordinates_df2['Humidity'].min() - 5, 5 + city_coordinates_df2['Humidity'].max())
plt.xlim(-90, 90)
plt.axvline(0, color='gray',alpha=0.4)
plt.savefig("Humidity vs. Latitude.png")
plt.show()
```

    ----------2. Humidity vs. Latitude Scatterplot----------



![png](output_14_1.png)



```python
print('----------3. Cloudiness vs. Latitude Scatterplot----------')
# Temperature vs Latitude 
city_coordinates_df2.plot(kind="scatter",x="Latitude",y="Cloudiness",s=50, marker = 'o', color = 'blue', grid=True)
plt.suptitle('Cloudiness (mph) vs. Latitude')
plt.title('Total cities plotted = %s'%(final_df_sz))
plt.ylim(city_coordinates_df2['Cloudiness'].min() - 10, 10 + city_coordinates_df2['Cloudiness'].max())
plt.xlim(-90, 90)
plt.axvline(0, color='gray',alpha=0.4)
plt.savefig("Cloudiness vs. Latitude.png")
plt.show()
```

    ----------3. Cloudiness vs. Latitude Scatterplot----------



![png](output_15_1.png)



```python
print('----------4. Wind Speed vs. Latitude Scatterplot----------')
# Temperature vs Latitude 
city_coordinates_df2.plot(kind="scatter",x="Latitude",y="Wind Speed",s=35, marker = 'o', color = 'green', grid=True)
plt.suptitle('Wind Speed (mph) vs. Latitude')
plt.title('Total cities plotted = %s'%(final_df_sz))
plt.ylim(0, 10 + city_coordinates_df2['Wind Speed'].max())
plt.xlim(-90, 90)
plt.axvline(0, color='gray',alpha=0.4)
plt.savefig("Wind Speed vs. Latitude.png")
plt.show()
```

    ----------4. Wind Speed vs. Latitude Scatterplot----------



![png](output_16_1.png)



```python
print('Observable Trends')
print('1.The temperature increases as coordinates get closer to the equator. The cities around the equator have the highest temperatures')
max_wind = city_coordinates_df2.loc[city_coordinates_df2['Wind Speed'] == city_coordinates_df2['Wind Speed'].max()]
max_wind['City']
max_wind['Country Code']
print('2.The wind speed for most of the cities is under 10 mph. The median is %smph. There is a possible outlier with a wind speed of %smph in %s'%(city_coordinates_df2['Wind Speed'].median(),city_coordinates_df2['Wind Speed'].max(),'Pahrump in the US'))
print('3. The clouds seem pretty disperse, whithout a visible correlation with the latitude.')

```

    Observable Trends
    1.The temperature increases as coordinates get closer to the equator. The cities around the equator have the highest temperatures
    2.The wind speed for most of the cities is under 10 mph. The median is 6.22mph. There is a possible outlier with a wind speed of 39.15mph in Pahrump in the US
    3. The clouds seem pretty disperse, whithout a visible correlation with the latitude.

