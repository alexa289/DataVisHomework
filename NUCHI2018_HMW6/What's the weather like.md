

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
city= citipy.nearest_city(latitude[0],longitude[0])
#city
city.city_name
```




    'vaini'




```python
city.country_code
```




    'to'




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
    print(city_names[x].city_name)
    city_list.append(city)

country_list = []
for y in range(0,max_coord):
    country = city_names[y].country_code
    print(city_names[y].country_code)
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

    vaini
    yellowknife
    hithadhoo
    marsa matruh
    basco
    cherskiy
    beruwala
    butaritari
    qaanaaq
    new norfolk
    kavaratti
    busselton
    pangnirtung
    rodbyhavn
    pangnirtung
    hobart
    hovd
    shimoda
    kaitangata
    chuy
    rikitea
    albany
    ruatoria
    torbay
    sitka
    tiksi
    atar
    puri
    poum
    vao
    mataura
    barrow
    avera
    barrow
    airai
    iqaluit
    sheridan
    grand river south east
    rikitea
    broome
    axim
    san carlos de bariloche
    ushuaia
    mys shmidta
    coquimbo
    mataura
    rikitea
    dong hoi
    rikitea
    busselton
    norman wells
    faanui
    verkhnevilyuysk
    cape town
    bereda
    busselton
    new norfolk
    saint george
    bonthe
    rikitea
    taolanaro
    ouadda
    el dorado
    hobart
    ribeira grande
    rikitea
    shangrao
    upernavik
    sioux lookout
    chokurdakh
    jamestown
    chuy
    punta arenas
    tiksi
    gorno-chuyskiy
    east london
    belushya guba
    geraldton
    kodiak
    dikson
    arraial do cabo
    vaini
    busselton
    amderma
    tura
    tuktoyaktuk
    rantauprapat
    samarai
    saleaula
    kapaa
    komsomolskiy
    shenjiamen
    new norfolk
    busselton
    castro
    yellowknife
    rikitea
    ushuaia
    taolanaro
    orlik
    hobart
    mahebourg
    zhuhai
    amparafaravola
    illoqqortoormiut
    anadyr
    punta arenas
    sorland
    belushya guba
    severo-kurilsk
    albany
    kribi
    sao joao da barra
    komsomolskiy
    kushiro
    norman wells
    north bend
    tuatapere
    emerald
    bambous virieux
    albany
    esperance
    san cristobal
    clyde river
    gazojak
    pouebo
    torbay
    ushuaia
    karamea
    montepuez
    damaturu
    puerto ayora
    yulara
    yar-sale
    olinda
    bredasdorp
    poso
    hauge
    phan rang
    rikitea
    cayenne
    mataura
    ribeira grande
    hobart
    yellowknife
    tiksi
    hobart
    torbay
    albany
    herten
    rikitea
    punta arenas
    mataura
    marzuq
    richards bay
    mar del plata
    coihaique
    narsaq
    tumannyy
    upernavik
    rikitea
    mahajanga
    vila franca do campo
    ribeira grande
    lompoc
    vaini
    bar harbor
    east london
    korla
    beringovskiy
    belushya guba
    hobart
    san quintin
    punta arenas
    hilo
    saskylakh
    tornio
    barrow
    mataura
    safita
    ushuaia
    busselton
    puerto ayora
    marawi
    olafsvik
    kudahuvadhoo
    boa vista
    hilo
    atuona
    sorland
    karamea
    barrow
    vaini
    saskylakh
    ushuaia
    bredasdorp
    nanortalik
    victoria
    hermanus
    cabo san lucas
    guanica
    rikitea
    namibe
    busselton
    carnarvon
    norman wells
    naze
    petropavlovsk-kamchatskiy
    half moon bay
    busselton
    georgetown
    qaanaaq
    arkhangelsk
    jamestown
    jamestown
    constitucion
    yar-sale
    labuan
    castro
    mazagao
    bluff
    new norfolk
    atuona
    komsomolets
    codrington
    narsaq
    saleaula
    tabou
    cayenne
    seoul
    ushuaia
    tiksi
    mys shmidta
    cherskiy
    muros
    nikolskoye
    dakar
    chapais
    saint-philippe
    busselton
    bluff
    oranjemund
    punta umbria
    luena
    laguna
    vilhena
    tchaourou
    avarua
    bambous virieux
    cidreira
    tubruq
    nyurba
    basco
    lima
    mount darwin
    bambous virieux
    garowe
    jalu
    taolanaro
    victoria
    hermanus
    bluff
    deming
    cherskiy
    hermanus
    new norfolk
    puerto ayora
    tiksi
    belushya guba
    antofagasta
    guerrero negro
    ledenice
    taolanaro
    mar del plata
    souillac
    elda
    salinas
    florence
    oistins
    nacala
    douentza
    yellowknife
    cabo san lucas
    bambanglipuro
    mataura
    georgetown
    voh
    svetlogorsk
    bambous virieux
    bethel
    georgetown
    rikitea
    khatanga
    saint-philippe
    vanavara
    bathsheba
    mataura
    barentsburg
    punta arenas
    puerto ayora
    vao
    inta
    nikolskoye
    albany
    tanout
    albany
    rikitea
    barentsburg
    new norfolk
    tsihombe
    aquiraz
    tual
    port alfred
    north platte
    havre-saint-pierre
    dikson
    port alfred
    castro
    busselton
    hobart
    belushya guba
    provideniya
    saint george
    mataura
    ushuaia
    cape town
    port alfred
    khash
    rikitea
    albany
    ponta do sol
    adolfo ruiz cortines
    mokhsogollokh
    hilo
    east london
    hermanus
    ushuaia
    ushuaia
    ushuaia
    busselton
    belushya guba
    kodiak
    burhaniye
    avarua
    punta arenas
    vaitupu
    butaritari
    tsihombe
    rikitea
    saint-francois
    sioux lookout
    avera
    gouyave
    vaitupu
    cockburn town
    mayo
    sorland
    rikitea
    dongning
    pokhara
    coffs harbour
    utiroa
    hobart
    mjolby
    kang
    caravelas
    mae sai
    kaeo
    puerto del rosario
    krutikha
    ushuaia
    arraial do cabo
    tasiilaq
    hobart
    chapais
    georgetown
    mataura
    hobart
    raudeberg
    vaini
    vila velha
    alvorada
    beira
    mahebourg
    flinders
    djambala
    richards bay
    punta arenas
    vestmannaeyjar
    norman wells
    guerrero negro
    samusu
    puerto ayora
    nantucket
    hithadhoo
    lavrentiya
    kabare
    gongzhuling
    illoqqortoormiut
    mount isa
    barreiras
    busselton
    mar del plata
    sao joao da barra
    new norfolk
    busselton
    toliary
    katsuura
    vardo
    lowestoft
    bluff
    yellowknife
    torbay
    kaitangata
    port-gentil
    rungata
    yellowknife
    vestmannaeyjar
    muros
    katsuura
    kapaa
    kodiak
    busselton
    mataura
    yulara
    tongliao
    kenai
    umzimvubu
    qaanaaq
    constitucion
    bluff
    clyde river
    punta arenas
    longlac
    qaanaaq
    belyy yar
    guerrero negro
    punta arenas
    pacific grove
    rikitea
    gornopravdinsk
    avarua
    geraldton
    westport
    norman wells
    luderitz
    dikson
    salinopolis
    victoria
    punta arenas
    sassandra
    westport
    port elizabeth
    saint anthony
    punta arenas
    taolanaro
    bethel
    gushikawa
    ostrovnoy
    jamestown
    ilulissat
    khatanga
    cidreira
    punta arenas
    esperance
    srednekolymsk
    illoqqortoormiut
    savannah bight
    antalaha
    provideniya
    castro
    novomalorossiyskaya
    grindavik
    punta arenas
    rikitea
    port alfred
    punta arenas
    bengkulu
    busselton
    albany
    saint-philippe
    mys shmidta
    qaanaaq
    codrington
    cape town
    xucheng
    bestobe
    hamilton
    punta arenas
    chuguyevka
    mataura
    saint-philippe
    olinda
    porto novo
    taolanaro
    vaini
    rikitea
    harper
    avarua
    belushya guba
    rungata
    pemangkat
    punta arenas
    butaritari
    puerto ayora
    georgetown
    kodinsk
    bluff
    dikson
    carnarvon
    birecik
    yaan
    agde
    jamestown
    busselton
    lagoa
    atuona
    tucumcari
    cherskiy
    illoqqortoormiut
    pochutla
    geraldton
    biu
    tuktoyaktuk
    jamestown
    fallon
    lompoc
    jamestown
    carutapera
    jamestown
    kirakira
    port elizabeth
    avarua
    alice town
    busselton
    rikitea
    dicabisagan
    georgetown
    lolua
    tervel
    hithadhoo
    pasighat
    castro
    mataura
    rikitea
    busselton
    moba
    sokolo
    kimberley
    vaini
    busselton
    albany
    qaanaaq
    palu
    pospelikha
    chuy
    dikson
    hilo
    ponta do sol
    atuona
    samusu
    bengkulu
    vaini
    tura
    komsomolskiy
    bluff
    khatanga
    nikolskoye
    mackay
    mishelevka
    tuktoyaktuk
    rikitea
    uribia
    geraldton
    new norfolk
    alta gracia
    lalsot
    ribeira grande
    jamestown
    port alfred
    conakry
    mbengwi
    knyaze-volkonskoye
    ushuaia
    oss
    exeter
    viedma
    mosquera
    punta arenas
    tiksi
    ancud
    bengkulu
    kloulklubed
    port alfred
    amga
    cape town
    louisbourg
    hermanus
    lorengau
    rapallo
    acapulco
    bukama
    huarmey
    hofn
    saleaula
    busselton
    trelew
    kapaa
    tambun
    cidreira
    boyolangu
    mataura
    sinnamary
    cabra
    port alfred
    port elizabeth
    punta arenas
    rikitea
    atar
    biak
    watertown
    det udom
    hilo
    taolanaro
    elizabeth city
    beidao
    ilulissat
    nanortalik
    leningradskiy
    kruisfontein
    east london
    mataura
    saleaula
    rikitea
    bluff
    albany
    port hardy
    galle
    neuquen
    busselton
    taolanaro
    albany
    ushuaia
    vardo
    taoudenni
    ghugus
    saint-augustin
    punta arenas
    cape town
    caapucu
    ribeira grande
    barentsburg
    avarua
    januaria
    avarua
    rikitea
    jibuti
    plainview
    chumikan
    jiroft
    chute-aux-outardes
    hithadhoo
    saskylakh
    gornopravdinsk
    bredasdorp
    tuktoyaktuk
    longyearbyen
    saint george
    kavieng
    mar del plata
    rawson
    bluff
    cape town
    pasni
    bluff
    tuktoyaktuk
    provideniya
    octeville
    saint-gaudens
    nikolskoye
    albany
    kapaa
    torbay
    khatanga
    altinopolis
    hobart
    ushuaia
    rundu
    ushuaia
    ponta do sol
    aklavik
    gwadar
    albany
    butaritari
    butaritari
    meadow lake
    nizhneyansk
    hithadhoo
    kudahuvadhoo
    kodiak
    antofagasta
    tombouctou
    cape town
    busselton
    xingyi
    tanout
    barrow
    hilo
    thunder bay
    tumannyy
    mataura
    albany
    taolanaro
    hermanus
    saleaula
    cape town
    cabo san lucas
    nizhnevartovsk
    dikson
    hailar
    mount gambier
    kapaa
    mataura
    provideniya
    mataura
    new norfolk
    avarua
    west bay
    waipawa
    port alfred
    poitiers
    naze
    walvis bay
    albany
    illoqqortoormiut
    sorong
    barentsburg
    emerald
    sapa
    port moresby
    tchibanga
    souillac
    rikitea
    namatanai
    hobart
    najran
    illoqqortoormiut
    hamilton
    karmana
    syriam
    mar del plata
    pemangkat
    upernavik
    saldanha
    belushya guba
    sentyabrskiy
    vestmannaeyjar
    saint-joseph
    ohara
    bilibino
    vaini
    puerto ayora
    les cayes
    ushuaia
    port alfred
    yarensk
    louisbourg
    amderma
    vicuna
    saint-philippe
    taolanaro
    vaini
    plettenberg bay
    ilulissat
    tilsonburg
    victoria
    margate
    kodiak
    barrow
    mataura
    vyazemskiy
    andra
    port alfred
    mataura
    vostok
    coahuayana
    vaini
    mar del plata
    thompson
    mahebourg
    kargasok
    hithadhoo
    port alfred
    awjilah
    bredasdorp
    vaini
    torbay
    albany
    mataura
    tiksi
    sarkand
    jamestown
    esperance
    buraydah
    kaitangata
    carnarvon
    butterworth
    mataura
    esperance
    albany
    provideniya
    clyde river
    port alfred
    mayo
    atuona
    illoqqortoormiut
    mataura
    mar del plata
    torbay
    cidreira
    piacabucu
    sarkand
    cherskiy
    kapaa
    mataura
    sedelnikovo
    portage
    aasiaat
    along
    rikitea
    samusu
    kaya
    nargana
    pevek
    sakakah
    aykhal
    tucuman
    ribeira grande
    banff
    mehamn
    alofi
    mandiana
    gafargaon
    assiniboia
    new norfolk
    atuona
    vaini
    victoria
    ngawen
    boulder city
    vaini
    belushya guba
    alofi
    chuy
    ciudad bolivar
    guerrero negro
    butaritari
    yurgamysh
    ushuaia
    hithadhoo
    margate
    tiksi
    arraial do cabo
    vaini
    kapaa
    mar del plata
    kununurra
    jamestown
    grand river south east
    san bartolome de tirajana
    norman wells
    rikitea
    astipalaia
    esperance
    torbay
    male
    bluff
    taolanaro
    labuhan
    bethel
    zhanakorgan
    bethel
    bluff
    petaling jaya
    faanui
    mercedes
    attawapiskat
    taolanaro
    punta arenas
    ushuaia
    hambantota
    provideniya
    kloulklubed
    georgiyevka
    nikolskoye
    hilo
    port elizabeth
    avarua
    daru
    san rafael
    obera
    pisco
    pacific grove
    port elizabeth
    bengkulu
    port alfred
    bredasdorp
    birao
    vaini
    sola
    vaitupu
    la vega
    itarema
    saint george
    barrow
    ushuaia
    amderma
    arraial do cabo
    horana
    puerto ayora
    ushuaia
    cidreira
    tsihombe
    barentsburg
    busselton
    saint-philippe
    punta arenas
    corumba
    meiganga
    saint anthony
    khatanga
    margate
    kahului
    deputatskiy
    bengkulu
    vaini
    new norfolk
    kamenskoye
    isangel
    sentyabrskiy
    albany
    saskylakh
    busselton
    mareeba
    sun valley
    boysun
    yulara
    hobart
    mayahi
    albany
    krasnaya polyana
    nogales
    abha
    narsaq
    kaitangata
    maniitsoq
    linxia
    rikitea
    katsina
    fort nelson
    mataura
    pisco
    viedma
    himora
    rikitea
    korla
    east london
    hobart
    jamestown
    zaigrayevo
    isangel
    puerto plata
    karakendzha
    chicama
    kamenskoye
    mataura
    qaanaaq
    nikolskoye
    cabo san lucas
    bredasdorp
    ushuaia
    hermanus
    punta arenas
    saint-philippe
    hermanus
    eskasem
    taolanaro
    alenquer
    bonthe
    avarua
    buraydah
    iqaluit
    busselton
    busselton
    codrington
    saint-augustin
    cape town
    thompson
    clyde river
    quebo
    cape town
    guerrero negro
    zhangjiakou
    atuona
    puerto ayora
    tasiilaq
    turukhansk
    paita
    riyadh
    samalaeulu
    qasigiannguit
    saskylakh
    ambulu
    busselton
    kushima
    omboue
    chokurdakh
    esperance
    taolanaro
    fort nelson
    umzimvubu
    albany
    mataura
    letlhakane
    saint-prosper
    chuy
    chabahar
    mataura
    ignalina
    poum
    port alfred
    vaini
    redlands
    punta arenas
    peniche
    samusu
    letlhakane
    alofi
    shahgarh
    hilo
    katangli
    puerto ayora
    sitka
    barrow
    lebu
    albany
    takapau
    tiksi
    hervey bay
    puerto ayora
    new norfolk
    punta arenas
    sur
    chuy
    beloha
    port-gentil
    nouadhibou
    maghama
    punta arenas
    olafsvik
    cape town
    albany
    cape town
    tigil
    bluff
    port alfred
    taolanaro
    cape town
    porto murtinho
    dikson
    barentsburg
    beihai
    vaini
    port-gentil
    atasu
    saint-philippe
    anadyr
    saskylakh
    punta arenas
    mahebourg
    hobart
    rikitea
    ushuaia
    ushuaia
    hearst
    barrow
    tamiahua
    arraial do cabo
    sur
    jipijapa
    parrita
    castro
    hithadhoo
    mataura
    chitral
    rikitea
    ilulissat
    khani
    coihaique
    anton lizardo
    rikitea
    gornopravdinsk
    asau
    butaritari
    khatanga
    sorong
    tasiilaq
    sao paulo de olivenca
    cabo san lucas
    saint-philippe
    klaksvik
    punta arenas
    khatanga
    albany
    tuktoyaktuk
    vaini
    palmer
    dikson
    vaini
    chokurdakh
    carnarvon
    rikitea
    santiago
    bluff
    mancio lima
    victoria
    barrow
    mahebourg
    castro
    puerto ayora
    mataura
    punta arenas
    praia
    albany
    hermanus
    butaritari
    busselton
    lakes entrance
    tuktoyaktuk
    clyde river
    taoudenni
    bengkulu
    dikson
    thomaston
    barrow
    ushuaia
    nikolskoye
    lhokseumawe
    windhoek
    saint-philippe
    busselton
    hays
    qiongshan
    bambous virieux
    mataura
    rudsar
    ixtapa
    sobolevo
    atuona
    powassan
    taolanaro
    hailun
    ushuaia
    tabiauea
    udomlya
    tuktoyaktuk
    urumqi
    hermanus
    salamanca
    kaspiyskiy
    pevek
    mataura
    port blair
    ushuaia
    joaquim gomes
    victoria
    ushuaia
    asau
    ponta do sol
    taolanaro
    shirgaon
    vaitupu
    kavieng
    oriximina
    khandyga
    port elizabeth
    georgetown
    albany
    tupik
    kapaa
    omboue
    cururupu
    hamilton
    taolanaro
    karatau
    hilo
    quatre cocos
    seoul
    yanahuanca
    albany
    kruisfontein
    eyrarbakki
    punta arenas
    liwale
    avarua
    nizhneyansk
    laguna
    arraial do cabo
    saint-philippe
    hobart
    kaitangata
    illoqqortoormiut
    deputatskiy
    saint george
    taolanaro
    laguna
    fayaoue
    busselton
    jamestown
    catamarca
    plettenberg bay
    mar del plata
    barrow
    albany
    hilo
    carnarvon
    marcona
    atuona
    tsihombe
    victoria
    ushuaia
    qaanaaq
    kapaa
    kajaani
    qaanaaq
    nikolskoye
    bluff
    new norfolk
    tuktoyaktuk
    punta arenas
    vaini
    atuona
    hilo
    albany
    nanortalik
    caravelas
    chagda
    cape town
    birjand
    mataura
    vanimo
    ushuaia
    vestmannaeyjar
    storforshei
    bandarbeyla
    mys shmidta
    severo-kurilsk
    atuona
    cape town
    punta arenas
    flinders
    hermanus
    port elizabeth
    clyde river
    baiima
    provideniya
    umzimvubu
    araouane
    myanaung
    guerrero negro
    hilo
    aykhal
    khatanga
    hermanus
    tabou
    fortuna
    albany
    cuamba
    ayan
    grand-santi
    punta arenas
    hithadhoo
    rikitea
    ushuaia
    maldonado
    punta arenas
    puerto ayora
    kapaa
    tuktoyaktuk
    padang
    hithadhoo
    sao filipe
    mataura
    albany
    mataura
    acapulco
    lagoa
    albany
    atuona
    becerril
    yellowknife
    nabire
    coihaique
    arraial do cabo
    yellowknife
    charters towers
    cape town
    meadow lake
    kapaa
    avarua
    kytmanovo
    vila franca do campo
    atuona
    laguna
    awjilah
    illoqqortoormiut
    belushya guba
    hermanus
    araxa
    tuktoyaktuk
    kahului
    butaritari
    ushuaia
    east london
    rodrigues alves
    ntoum
    maragogi
    bluff
    panalingaan
    puerto ayora
    marystown
    victoria
    dikson
    carnarvon
    mataura
    hermanus
    longyearbyen
    rikitea
    barrow
    dunedin
    kodiak
    chuy
    hobart
    mataura
    kunashak
    rikitea
    butaritari
    nieuw amsterdam
    tiksi
    jamestown
    taolanaro
    comodoro rivadavia
    bluff
    mbacke
    ushuaia
    palabuhanratu
    qaanaaq
    geresk
    mataura
    tyukhtet
    bam
    richards bay
    ushuaia
    nikolskoye
    jamestown
    punta arenas
    ust-kamchatsk
    ushuaia
    clyde river
    tiksi
    grindavik
    ushuaia
    omboue
    port hardy
    ushuaia
    tsihombe
    tasiilaq
    ribeira grande
    teguldet
    kapaa
    jamestown
    souillac
    ahipara
    cay
    atuona
    belushya guba
    vaini
    sturgis
    rikitea
    ushuaia
    punta arenas
    khorramshahr
    hobart
    xuddur
    yar-sale
    evensk
    ponta do sol
    sitka
    ofunato
    sitka
    port alfred
    busselton
    bereda
    rikitea
    tuktoyaktuk
    busselton
    aklavik
    cape town
    vestmannaeyjar
    hettstedt
    marsabit
    lompoc
    san marcos de colon
    quatre cocos
    alta floresta
    felidhoo
    kapaa
    punta arenas
    pangnirtung
    samusu
    cape town
    butaritari
    qaanaaq
    hilo
    riberalta
    ribeira grande
    punta arenas
    albany
    atuona
    cape town
    bluff
    ushuaia
    namatanai
    isangel
    jamestown
    port alfred
    georgetown
    rikitea
    chokurdakh
    acapulco
    bandundu
    mar del plata
    mataura
    barrow
    cape town
    castro
    hobart
    rikitea
    victoria
    thompson
    kapaa
    puerto ayora
    port elizabeth
    serik
    mataura
    saint-philippe
    mataura
    punta arenas
    nikolskoye
    kisaran
    yar-sale
    amderma
    rikitea
    sentyabrskiy
    bud
    belushya guba
    hermanus
    ambon
    port antonio
    mataura
    henties bay
    ebano
    busselton
    ushuaia
    rikitea
    hermanus
    thompson
    srem
    port alfred
    tumannyy
    cape town
    kismayo
    ushuaia
    verkhniy baskunchak
    ancud
    bengkulu
    palana
    hermanus
    albany
    khatanga
    tiksi
    bolton
    torbay
    pevek
    mecca
    chuy
    guerrero negro
    cape town
    meulaboh
    severo-yeniseyskiy
    to
    ca
    mv
    eg
    ph
    ru
    lk
    ki
    gl
    au
    in
    au
    ca
    dk
    ca
    au
    mn
    jp
    nz
    uy
    pf
    au
    nz
    ca
    us
    ru
    mr
    in
    nc
    nc
    pf
    us
    pf
    us
    pw
    ca
    us
    mu
    pf
    au
    gh
    ar
    ar
    ru
    cl
    pf
    pf
    vn
    pf
    au
    ca
    pf
    ru
    za
    so
    au
    au
    bm
    sl
    pf
    mg
    cf
    co
    au
    pt
    pf
    cn
    gl
    ca
    ru
    sh
    uy
    cl
    ru
    ru
    za
    ru
    au
    us
    ru
    br
    to
    au
    ru
    ru
    ca
    id
    pg
    ws
    us
    ru
    cn
    au
    au
    cl
    ca
    pf
    ar
    mg
    ru
    au
    mu
    cn
    mg
    gl
    ru
    cl
    no
    ru
    ru
    au
    cm
    br
    ru
    jp
    ca
    us
    nz
    au
    mu
    au
    au
    ec
    ca
    tm
    nc
    ca
    ar
    nz
    mz
    ng
    ec
    au
    ru
    br
    za
    id
    no
    vn
    pf
    gf
    pf
    pt
    au
    ca
    ru
    au
    ca
    au
    de
    pf
    cl
    pf
    ly
    za
    ar
    cl
    gl
    ru
    gl
    pf
    mg
    pt
    pt
    us
    to
    us
    za
    cn
    ru
    ru
    au
    mx
    cl
    us
    ru
    fi
    us
    pf
    sy
    ar
    au
    ec
    sd
    is
    mv
    br
    us
    pf
    no
    nz
    us
    to
    ru
    ar
    za
    gl
    sc
    za
    mx
    us
    pf
    ao
    au
    au
    ca
    jp
    ru
    us
    au
    sh
    gl
    ru
    sh
    sh
    mx
    ru
    my
    cl
    br
    nz
    au
    pf
    kz
    ag
    gl
    ws
    ci
    gf
    kr
    ar
    ru
    ru
    ru
    es
    ru
    sn
    ca
    re
    au
    nz
    na
    es
    ao
    br
    br
    bj
    ck
    mu
    br
    ly
    ru
    ph
    pe
    zw
    mu
    so
    ly
    mg
    sc
    za
    nz
    us
    ru
    za
    au
    ec
    ru
    ru
    cl
    mx
    cz
    mg
    ar
    mu
    es
    us
    us
    bb
    mz
    ml
    ca
    mx
    id
    pf
    sh
    nc
    ru
    mu
    us
    sh
    pf
    ru
    re
    ru
    bb
    pf
    sj
    cl
    ec
    nc
    ru
    ru
    au
    ne
    au
    pf
    sj
    au
    mg
    br
    id
    za
    us
    ca
    ru
    za
    cl
    au
    au
    ru
    ru
    bm
    pf
    ar
    za
    za
    ir
    pf
    au
    cv
    mx
    ru
    us
    za
    za
    ar
    ar
    ar
    au
    ru
    us
    tr
    ck
    cl
    wf
    ki
    mg
    pf
    gp
    ca
    pf
    gd
    wf
    tc
    ca
    no
    pf
    cn
    np
    au
    ki
    au
    se
    bw
    br
    th
    nz
    es
    ru
    ar
    br
    gl
    au
    ca
    sh
    pf
    au
    no
    to
    br
    br
    mz
    mu
    au
    cg
    za
    cl
    is
    ca
    mx
    ws
    ec
    us
    mv
    ru
    cd
    cn
    gl
    au
    br
    au
    ar
    br
    au
    au
    mg
    jp
    no
    gb
    nz
    ca
    ca
    nz
    ga
    ki
    ca
    is
    es
    jp
    us
    us
    au
    pf
    au
    cn
    us
    za
    gl
    mx
    nz
    ca
    cl
    ca
    gl
    ru
    mx
    cl
    us
    pf
    ru
    ck
    au
    nz
    ca
    na
    ru
    br
    sc
    cl
    ci
    nz
    za
    ca
    cl
    mg
    us
    jp
    ru
    sh
    gl
    ru
    br
    cl
    au
    ru
    gl
    hn
    mg
    ru
    cl
    ru
    is
    cl
    pf
    za
    cl
    id
    au
    au
    re
    ru
    gl
    ag
    za
    cn
    kz
    us
    cl
    ru
    pf
    re
    br
    cv
    mg
    to
    pf
    lr
    ck
    ru
    ki
    id
    cl
    ki
    ec
    sh
    ru
    nz
    ru
    au
    tr
    cn
    fr
    sh
    au
    pt
    pf
    us
    ru
    gl
    mx
    au
    ng
    ca
    sh
    us
    us
    sh
    br
    sh
    sb
    za
    ck
    bs
    au
    pf
    ph
    sh
    tv
    bg
    mv
    in
    cl
    pf
    pf
    au
    cd
    ml
    ca
    to
    au
    au
    gl
    id
    ru
    uy
    ru
    us
    cv
    pf
    ws
    id
    to
    ru
    ru
    nz
    ru
    ru
    au
    ru
    ca
    pf
    co
    au
    au
    ar
    in
    pt
    sh
    za
    gn
    cm
    ru
    ar
    nl
    gb
    ar
    co
    cl
    ru
    cl
    id
    pw
    za
    ru
    za
    ca
    za
    pg
    it
    mx
    cd
    pe
    is
    ws
    au
    ar
    us
    id
    br
    id
    pf
    gf
    ph
    za
    za
    cl
    pf
    mr
    id
    us
    th
    us
    mg
    us
    cn
    gl
    gl
    ru
    za
    za
    pf
    ws
    pf
    nz
    au
    ca
    lk
    ar
    au
    mg
    au
    ar
    no
    ml
    in
    ca
    cl
    za
    py
    pt
    sj
    ck
    br
    ck
    pf
    dj
    us
    ru
    ir
    ca
    mv
    ru
    ru
    za
    ca
    sj
    bm
    pg
    ar
    ar
    nz
    za
    pk
    nz
    ca
    ru
    fr
    fr
    ru
    au
    us
    ca
    ru
    br
    au
    ar
    na
    ar
    cv
    ca
    pk
    au
    ki
    ki
    ca
    ru
    mv
    mv
    us
    cl
    ml
    za
    au
    cn
    ne
    us
    us
    ca
    ru
    pf
    au
    mg
    za
    ws
    za
    mx
    ru
    ru
    cn
    au
    us
    pf
    ru
    pf
    au
    ck
    ky
    nz
    za
    fr
    jp
    na
    au
    gl
    id
    sj
    au
    ph
    pg
    ga
    mu
    pf
    pg
    au
    sa
    gl
    bm
    uz
    mm
    ar
    id
    gl
    za
    ru
    ru
    is
    re
    jp
    ru
    to
    ec
    ht
    ar
    za
    ru
    ca
    ru
    cl
    re
    mg
    to
    za
    gl
    ca
    sc
    za
    us
    us
    pf
    ru
    ru
    za
    pf
    ru
    mx
    to
    ar
    ca
    mu
    ru
    mv
    za
    ly
    za
    to
    ca
    au
    pf
    ru
    kz
    sh
    au
    sa
    nz
    au
    za
    pf
    au
    au
    ru
    ca
    za
    ca
    pf
    gl
    pf
    ar
    ca
    br
    br
    kz
    ru
    us
    pf
    ru
    us
    gl
    in
    pf
    ws
    bf
    pa
    ru
    sa
    ru
    ar
    pt
    ca
    no
    nu
    gn
    bd
    ca
    au
    pf
    to
    sc
    id
    us
    to
    ru
    nu
    uy
    ve
    mx
    ki
    ru
    ar
    mv
    za
    ru
    br
    to
    us
    ar
    au
    sh
    mu
    es
    ca
    pf
    gr
    au
    ca
    mv
    nz
    mg
    id
    us
    kz
    us
    nz
    my
    pf
    ar
    ca
    mg
    cl
    ar
    lk
    ru
    pw
    kz
    ru
    us
    za
    ck
    pg
    ar
    ar
    pe
    us
    za
    id
    za
    za
    cf
    to
    vu
    wf
    do
    br
    bm
    us
    ar
    ru
    br
    lk
    ec
    ar
    br
    mg
    sj
    au
    re
    cl
    br
    cm
    ca
    ru
    za
    us
    ru
    id
    to
    au
    ru
    vu
    ru
    au
    ru
    au
    au
    us
    uz
    au
    au
    ne
    au
    ru
    us
    sa
    gl
    nz
    gl
    cn
    pf
    ng
    ca
    pf
    pe
    ar
    et
    pf
    cn
    za
    au
    sh
    ru
    vu
    do
    tj
    pe
    ru
    pf
    gl
    ru
    mx
    za
    ar
    za
    cl
    re
    za
    af
    mg
    br
    sl
    ck
    sa
    ca
    au
    au
    ag
    ca
    za
    ca
    ca
    gw
    za
    mx
    cn
    pf
    ec
    gl
    ru
    pe
    sa
    ws
    gl
    ru
    id
    au
    jp
    ga
    ru
    au
    mg
    ca
    za
    au
    pf
    bw
    ca
    uy
    ir
    pf
    lt
    nc
    za
    to
    us
    cl
    pt
    ws
    bw
    nu
    in
    us
    ru
    ec
    us
    us
    cl
    au
    nz
    ru
    au
    ec
    au
    cl
    om
    uy
    mg
    ga
    mr
    mr
    cl
    is
    za
    au
    za
    ru
    nz
    za
    mg
    za
    br
    ru
    sj
    cn
    to
    ga
    kz
    re
    ru
    ru
    cl
    mu
    au
    pf
    ar
    ar
    ca
    us
    mx
    br
    om
    ec
    cr
    cl
    mv
    pf
    pk
    pf
    gl
    ru
    cl
    mx
    pf
    ru
    tv
    ki
    ru
    id
    gl
    br
    mx
    re
    fo
    cl
    ru
    au
    ca
    to
    us
    ru
    to
    ru
    au
    pf
    br
    nz
    br
    sc
    us
    mu
    cl
    ec
    pf
    cl
    cv
    au
    za
    ki
    au
    au
    ca
    ca
    ml
    id
    ru
    us
    us
    ar
    ru
    id
    na
    re
    au
    us
    cn
    mu
    pf
    ir
    mx
    ru
    pf
    ca
    mg
    cn
    ar
    ki
    ru
    ca
    cn
    za
    cl
    ru
    ru
    pf
    in
    ar
    br
    sc
    ar
    tv
    cv
    mg
    in
    wf
    pg
    br
    ru
    za
    gy
    au
    ru
    us
    ga
    br
    bm
    mg
    kz
    us
    mu
    kr
    pe
    au
    za
    is
    cl
    tz
    ck
    ru
    br
    br
    re
    au
    nz
    gl
    ru
    bm
    mg
    br
    nc
    au
    sh
    ar
    za
    ar
    us
    au
    us
    au
    pe
    pf
    mg
    sc
    ar
    gl
    us
    fi
    gl
    ru
    nz
    au
    ca
    cl
    to
    pf
    us
    au
    gl
    br
    ru
    za
    ir
    pf
    pg
    ar
    is
    no
    so
    ru
    ru
    pf
    za
    cl
    au
    za
    za
    ca
    sl
    ru
    za
    ml
    mm
    mx
    us
    ru
    ru
    za
    ci
    us
    au
    mz
    ru
    gf
    cl
    mv
    pf
    ar
    uy
    cl
    ec
    us
    ca
    id
    mv
    cv
    pf
    au
    pf
    mx
    pt
    au
    pf
    co
    ca
    id
    cl
    br
    ca
    au
    za
    ca
    us
    ck
    ru
    pt
    pf
    br
    ly
    gl
    ru
    za
    br
    ca
    us
    ki
    ar
    za
    br
    ga
    br
    nz
    ph
    ec
    ca
    sc
    ru
    au
    pf
    za
    sj
    pf
    us
    nz
    us
    uy
    au
    pf
    ru
    pf
    ki
    sr
    ru
    sh
    mg
    ar
    nz
    sn
    ar
    id
    gl
    af
    pf
    ru
    ir
    za
    ar
    ru
    sh
    cl
    ru
    ar
    ca
    ru
    is
    ar
    ga
    ca
    ar
    mg
    gl
    pt
    ru
    us
    sh
    mu
    nz
    tr
    pf
    ru
    to
    us
    pf
    ar
    cl
    ir
    au
    so
    ru
    ru
    pt
    us
    jp
    us
    za
    au
    so
    pf
    ca
    au
    ca
    za
    is
    de
    ke
    us
    hn
    mu
    br
    mv
    us
    cl
    ca
    ws
    za
    ki
    gl
    us
    bo
    pt
    cl
    au
    pf
    za
    nz
    ar
    pg
    vu
    sh
    za
    sh
    pf
    ru
    mx
    cd
    ar
    pf
    us
    za
    cl
    au
    pf
    sc
    ca
    us
    ec
    za
    tr
    pf
    re
    pf
    cl
    ru
    id
    ru
    ru
    pf
    ru
    no
    ru
    za
    id
    jm
    pf
    na
    mx
    au
    ar
    pf
    za
    ca
    pl
    za
    ru
    za
    so
    ar
    ru
    cl
    id
    ru
    za
    au
    ru
    ru
    ca
    ca
    ru
    sa
    uy
    mx
    za
    id
    ru



![png](output_7_1.png)



```python
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


![png](output_8_0.png)



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

    Current temperature (F) for Vaini:
    77.36



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

    Retrieve Weather Parameters for: hobart,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hobart
    Retrieve Weather Parameters for: mareeba,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mareeba
    Retrieve Weather Parameters for: samalaeulu,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=samalaeulu
    Retrieve Weather Parameters for: pemangkat,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pemangkat
    Retrieve Weather Parameters for: male,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=male
    Retrieve Weather Parameters for: marawi,sd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marawi
    Retrieve Weather Parameters for: tura,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tura
    Retrieve Weather Parameters for: saint-augustin,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-augustin
    Retrieve Weather Parameters for: tornio,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tornio
    Retrieve Weather Parameters for: mayahi,ne
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mayahi
    Retrieve Weather Parameters for: nouadhibou,mr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nouadhibou
    Retrieve Weather Parameters for: vila velha,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vila%20velha
    Retrieve Weather Parameters for: gushikawa,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gushikawa
    Retrieve Weather Parameters for: krasnaya polyana,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=krasnaya%20polyana
    Retrieve Weather Parameters for: sorland,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sorland
    Retrieve Weather Parameters for: joaquim gomes,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=joaquim%20gomes
    Retrieve Weather Parameters for: muros,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=muros
    Retrieve Weather Parameters for: marzuq,ly
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marzuq
    Retrieve Weather Parameters for: chagda,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chagda
    Retrieve Weather Parameters for: butaritari,ki
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=butaritari
    Retrieve Weather Parameters for: caravelas,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=caravelas
    Retrieve Weather Parameters for: ribeira grande,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ribeira%20grande
    Retrieve Weather Parameters for: cabo san lucas,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cabo%20san%20lucas
    Retrieve Weather Parameters for: verkhniy baskunchak,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=verkhniy%20baskunchak
    Retrieve Weather Parameters for: garowe,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=garowe
    Retrieve Weather Parameters for: puerto plata,do
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puerto%20plata
    Retrieve Weather Parameters for: carnarvon,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=carnarvon
    Retrieve Weather Parameters for: mayo,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mayo
    Retrieve Weather Parameters for: nacala,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nacala
    Retrieve Weather Parameters for: ponta do sol,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ponta%20do%20sol
    Retrieve Weather Parameters for: alenquer,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alenquer
    Retrieve Weather Parameters for: ignalina,lt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ignalina
    Retrieve Weather Parameters for: shenjiamen,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shenjiamen
    Retrieve Weather Parameters for: ruatoria,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ruatoria
    Retrieve Weather Parameters for: djambala,cg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=djambala
    Retrieve Weather Parameters for: pouebo,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pouebo
    Retrieve Weather Parameters for: sentyabrskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sentyabrskiy
    Retrieve Weather Parameters for: chitral,pk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chitral
    Retrieve Weather Parameters for: antalaha,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=antalaha
    Retrieve Weather Parameters for: peniche,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=peniche
    Retrieve Weather Parameters for: oriximina,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oriximina
    Retrieve Weather Parameters for: sarkand,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sarkand
    Retrieve Weather Parameters for: buraydah,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=buraydah
    Retrieve Weather Parameters for: jamestown,sh
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jamestown
    Retrieve Weather Parameters for: sur,om
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sur
    Retrieve Weather Parameters for: lolua,tv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lolua
    Retrieve Weather Parameters for: mount isa,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mount%20isa
    Retrieve Weather Parameters for: quebo,gw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=quebo
    Retrieve Weather Parameters for: mecca,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mecca
    Retrieve Weather Parameters for: yaan,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yaan
    Retrieve Weather Parameters for: palu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=palu
    Retrieve Weather Parameters for: punta umbria,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=punta%20umbria
    Retrieve Weather Parameters for: rundu,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rundu
    Retrieve Weather Parameters for: mandiana,gn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mandiana
    Retrieve Weather Parameters for: katsina,ng
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=katsina
    Retrieve Weather Parameters for: hauge,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hauge
    Retrieve Weather Parameters for: geraldton,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=geraldton
    Retrieve Weather Parameters for: pevek,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pevek
    Retrieve Weather Parameters for: barentsburg,sj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barentsburg
    Retrieve Weather Parameters for: coahuayana,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coahuayana
    Retrieve Weather Parameters for: burhaniye,tr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=burhaniye
    Retrieve Weather Parameters for: petropavlovsk-kamchatskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=petropavlovsk-kamchatskiy
    Retrieve Weather Parameters for: pisco,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pisco
    Retrieve Weather Parameters for: vyazemskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vyazemskiy
    Retrieve Weather Parameters for: bandarbeyla,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bandarbeyla
    Retrieve Weather Parameters for: becerril,co
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=becerril
    Retrieve Weather Parameters for: nizhnevartovsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nizhnevartovsk
    Retrieve Weather Parameters for: saint-gaudens,fr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-gaudens
    Retrieve Weather Parameters for: xuddur,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=xuddur
    Retrieve Weather Parameters for: elda,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=elda
    Retrieve Weather Parameters for: jibuti,dj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jibuti
    Retrieve Weather Parameters for: kapaa,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kapaa
    Retrieve Weather Parameters for: vilhena,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vilhena
    Retrieve Weather Parameters for: port-gentil,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port-gentil
    Retrieve Weather Parameters for: rodrigues alves,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rodrigues%20alves
    Retrieve Weather Parameters for: cururupu,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cururupu
    Retrieve Weather Parameters for: saint-prosper,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-prosper
    Retrieve Weather Parameters for: half moon bay,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=half%20moon%20bay
    Retrieve Weather Parameters for: port antonio,jm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20antonio
    Retrieve Weather Parameters for: nogales,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nogales
    Retrieve Weather Parameters for: nantucket,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nantucket
    Retrieve Weather Parameters for: savannah bight,hn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=savannah%20bight
    Retrieve Weather Parameters for: guanica,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=guanica
    Retrieve Weather Parameters for: sioux lookout,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sioux%20lookout
    Retrieve Weather Parameters for: umzimvubu,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=umzimvubu
    Retrieve Weather Parameters for: obera,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=obera
    Retrieve Weather Parameters for: eskasem,af
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=eskasem
    Retrieve Weather Parameters for: palmer,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=palmer
    Retrieve Weather Parameters for: praia,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=praia
    Retrieve Weather Parameters for: andra,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=andra
    Retrieve Weather Parameters for: havre-saint-pierre,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=havre-saint-pierre
    Retrieve Weather Parameters for: oistins,bb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oistins
    Retrieve Weather Parameters for: rapallo,it
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rapallo
    Retrieve Weather Parameters for: zhuhai,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zhuhai
    Retrieve Weather Parameters for: amparafaravola,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=amparafaravola
    Retrieve Weather Parameters for: biu,ng
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=biu
    Retrieve Weather Parameters for: marsabit,ke
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marsabit
    Retrieve Weather Parameters for: evensk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=evensk
    Retrieve Weather Parameters for: vardo,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vardo
    Retrieve Weather Parameters for: gwadar,pk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gwadar
    Retrieve Weather Parameters for: mahebourg,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mahebourg
    Retrieve Weather Parameters for: sapa,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sapa
    Retrieve Weather Parameters for: bud,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bud
    Retrieve Weather Parameters for: mae sai,th
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mae%20sai
    Retrieve Weather Parameters for: beruwala,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beruwala
    Retrieve Weather Parameters for: vao,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vao
    Retrieve Weather Parameters for: acapulco,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=acapulco
    Retrieve Weather Parameters for: mount gambier,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mount%20gambier
    Retrieve Weather Parameters for: kunashak,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kunashak
    Retrieve Weather Parameters for: tabiauea,ki
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tabiauea
    Retrieve Weather Parameters for: norman wells,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=norman%20wells
    Retrieve Weather Parameters for: windhoek,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=windhoek
    Retrieve Weather Parameters for: lakes entrance,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lakes%20entrance
    Retrieve Weather Parameters for: mancio lima,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mancio%20lima
    Retrieve Weather Parameters for: kodinsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kodinsk
    Retrieve Weather Parameters for: anadyr,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=anadyr
    Retrieve Weather Parameters for: flinders,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=flinders
    Retrieve Weather Parameters for: kisaran,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kisaran
    Retrieve Weather Parameters for: lowestoft,gb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lowestoft
    Retrieve Weather Parameters for: tchaourou,bj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tchaourou
    Retrieve Weather Parameters for: rikitea,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rikitea
    Retrieve Weather Parameters for: sheridan,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sheridan
    Retrieve Weather Parameters for: san rafael,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20rafael
    Retrieve Weather Parameters for: utiroa,ki
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=utiroa
    Retrieve Weather Parameters for: boysun,uz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=boysun
    Retrieve Weather Parameters for: aklavik,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aklavik
    Retrieve Weather Parameters for: yellowknife,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yellowknife
    Retrieve Weather Parameters for: puerto ayora,ec
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puerto%20ayora
    Retrieve Weather Parameters for: geresk,af
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=geresk
    Retrieve Weather Parameters for: karmana,uz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=karmana
    Retrieve Weather Parameters for: pochutla,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pochutla
    Retrieve Weather Parameters for: chute-aux-outardes,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chute-aux-outardes
    Retrieve Weather Parameters for: alofi,nu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alofi
    Retrieve Weather Parameters for: hervey bay,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hervey%20bay
    Retrieve Weather Parameters for: bambous virieux,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bambous%20virieux
    Retrieve Weather Parameters for: phan rang,vn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=phan%20rang
    Retrieve Weather Parameters for: agde,fr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=agde
    Retrieve Weather Parameters for: sinnamary,gf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sinnamary
    Retrieve Weather Parameters for: lagoa,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lagoa
    Retrieve Weather Parameters for: korla,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=korla
    Retrieve Weather Parameters for: georgiyevka,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=georgiyevka
    Retrieve Weather Parameters for: bar harbor,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bar%20harbor
    Retrieve Weather Parameters for: yarensk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yarensk
    Retrieve Weather Parameters for: lavrentiya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lavrentiya
    Retrieve Weather Parameters for: dikson,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dikson
    Retrieve Weather Parameters for: kaitangata,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaitangata
    Retrieve Weather Parameters for: sun valley,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sun%20valley
    Retrieve Weather Parameters for: fortuna,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fortuna
    Retrieve Weather Parameters for: sorong,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sorong
    Retrieve Weather Parameters for: mehamn,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mehamn
    Retrieve Weather Parameters for: birjand,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=birjand
    Retrieve Weather Parameters for: boyolangu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=boyolangu
    Retrieve Weather Parameters for: damaturu,ng
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=damaturu
    Retrieve Weather Parameters for: gafargaon,bd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gafargaon
    Retrieve Weather Parameters for: linxia,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=linxia
    Retrieve Weather Parameters for: khorramshahr,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khorramshahr
    Retrieve Weather Parameters for: urumqi,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=urumqi
    Retrieve Weather Parameters for: kytmanovo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kytmanovo
    Retrieve Weather Parameters for: paita,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=paita
    Retrieve Weather Parameters for: maragogi,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maragogi
    Retrieve Weather Parameters for: tchibanga,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tchibanga
    Retrieve Weather Parameters for: ebano,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ebano
    Retrieve Weather Parameters for: sobolevo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sobolevo
    Retrieve Weather Parameters for: kismayo,so
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kismayo
    Retrieve Weather Parameters for: luderitz,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=luderitz
    Retrieve Weather Parameters for: trelew,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=trelew
    Retrieve Weather Parameters for: salamanca,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=salamanca
    Retrieve Weather Parameters for: gornopravdinsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gornopravdinsk
    Retrieve Weather Parameters for: cuamba,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cuamba
    Retrieve Weather Parameters for: saint anthony,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint%20anthony
    Retrieve Weather Parameters for: deputatskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=deputatskiy
    Retrieve Weather Parameters for: grindavik,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=grindavik
    Retrieve Weather Parameters for: tucumcari,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tucumcari
    Retrieve Weather Parameters for: belushya guba,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=belushya%20guba
    Retrieve Weather Parameters for: kavaratti,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kavaratti
    Retrieve Weather Parameters for: san marcos de colon,hn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20marcos%20de%20colon
    Retrieve Weather Parameters for: mount darwin,zw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mount%20darwin
    Retrieve Weather Parameters for: nyurba,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nyurba
    Retrieve Weather Parameters for: himora,et
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=himora
    Retrieve Weather Parameters for: mahajanga,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mahajanga
    Retrieve Weather Parameters for: zhangjiakou,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zhangjiakou
    Retrieve Weather Parameters for: kruisfontein,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kruisfontein
    Retrieve Weather Parameters for: abha,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=abha
    Retrieve Weather Parameters for: kaeo,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaeo
    Retrieve Weather Parameters for: letlhakane,bw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=letlhakane
    Retrieve Weather Parameters for: tuktoyaktuk,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tuktoyaktuk
    Retrieve Weather Parameters for: hettstedt,de
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hettstedt
    Retrieve Weather Parameters for: qasigiannguit,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qasigiannguit
    Retrieve Weather Parameters for: meadow lake,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=meadow%20lake
    Retrieve Weather Parameters for: viedma,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=viedma
    Retrieve Weather Parameters for: torbay,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=torbay
    Retrieve Weather Parameters for: orlik,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=orlik
    Retrieve Weather Parameters for: vaini,to
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vaini
    Retrieve Weather Parameters for: verkhnevilyuysk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=verkhnevilyuysk
    Retrieve Weather Parameters for: vostok,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vostok
    Retrieve Weather Parameters for: taoudenni,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taoudenni
    Retrieve Weather Parameters for: octeville,fr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=octeville
    Retrieve Weather Parameters for: tiksi,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tiksi
    Retrieve Weather Parameters for: oranjemund,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oranjemund
    Retrieve Weather Parameters for: shirgaon,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shirgaon
    Retrieve Weather Parameters for: yurgamysh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yurgamysh
    Retrieve Weather Parameters for: les cayes,ht
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=les%20cayes
    Retrieve Weather Parameters for: montepuez,mz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=montepuez
    Retrieve Weather Parameters for: labuan,my
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=labuan
    Retrieve Weather Parameters for: serik,tr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=serik
    Retrieve Weather Parameters for: butterworth,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=butterworth
    Retrieve Weather Parameters for: kaspiyskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaspiyskiy
    Retrieve Weather Parameters for: isangel,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=isangel
    Retrieve Weather Parameters for: mosquera,co
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mosquera
    Retrieve Weather Parameters for: hofn,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hofn
    Retrieve Weather Parameters for: raudeberg,no
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=raudeberg
    Retrieve Weather Parameters for: hermanus,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hermanus
    Retrieve Weather Parameters for: dunedin,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dunedin
    Retrieve Weather Parameters for: waipawa,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=waipawa
    Retrieve Weather Parameters for: khash,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khash
    Retrieve Weather Parameters for: birecik,tr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=birecik
    Retrieve Weather Parameters for: araxa,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=araxa
    Retrieve Weather Parameters for: tumannyy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tumannyy
    Retrieve Weather Parameters for: tamiahua,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tamiahua
    Retrieve Weather Parameters for: banff,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=banff
    Retrieve Weather Parameters for: dong hoi,vn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dong%20hoi
    Retrieve Weather Parameters for: riberalta,bo
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=riberalta
    Retrieve Weather Parameters for: tilsonburg,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tilsonburg
    Retrieve Weather Parameters for: ambulu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ambulu
    Retrieve Weather Parameters for: sola,vu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sola
    Retrieve Weather Parameters for: eyrarbakki,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=eyrarbakki
    Retrieve Weather Parameters for: boulder city,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=boulder%20city
    Retrieve Weather Parameters for: neuquen,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=neuquen
    Retrieve Weather Parameters for: aasiaat,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aasiaat
    Retrieve Weather Parameters for: ixtapa,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ixtapa
    Retrieve Weather Parameters for: hailun,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hailun
    Retrieve Weather Parameters for: watertown,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=watertown
    Retrieve Weather Parameters for: cape town,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cape%20town
    Retrieve Weather Parameters for: exeter,gb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=exeter
    Retrieve Weather Parameters for: dongning,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dongning
    Retrieve Weather Parameters for: fallon,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fallon
    Retrieve Weather Parameters for: coffs harbour,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coffs%20harbour
    Retrieve Weather Parameters for: north platte,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=north%20platte
    Retrieve Weather Parameters for: thompson,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=thompson
    Retrieve Weather Parameters for: dicabisagan,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dicabisagan
    Retrieve Weather Parameters for: horana,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=horana
    Retrieve Weather Parameters for: udomlya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=udomlya
    Retrieve Weather Parameters for: barreiras,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barreiras
    Retrieve Weather Parameters for: mishelevka,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mishelevka
    Retrieve Weather Parameters for: ayan,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ayan
    Retrieve Weather Parameters for: ancud,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ancud
    Retrieve Weather Parameters for: walvis bay,na
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=walvis%20bay
    Retrieve Weather Parameters for: boa vista,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=boa%20vista
    Retrieve Weather Parameters for: souillac,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=souillac
    Retrieve Weather Parameters for: chabahar,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chabahar
    Retrieve Weather Parameters for: barrow,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=barrow
    Retrieve Weather Parameters for: tsihombe,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tsihombe
    Retrieve Weather Parameters for: vanavara,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vanavara
    Retrieve Weather Parameters for: astipalaia,gr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=astipalaia
    Retrieve Weather Parameters for: arraial do cabo,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=arraial%20do%20cabo
    Retrieve Weather Parameters for: saleaula,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saleaula
    Retrieve Weather Parameters for: ledenice,cz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ledenice
    Retrieve Weather Parameters for: kargasok,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kargasok
    Retrieve Weather Parameters for: hilo,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hilo
    Retrieve Weather Parameters for: poitiers,fr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=poitiers
    Retrieve Weather Parameters for: bambanglipuro,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bambanglipuro
    Retrieve Weather Parameters for: saldanha,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saldanha
    Retrieve Weather Parameters for: san carlos de bariloche,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20carlos%20de%20bariloche
    Retrieve Weather Parameters for: westport,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=westport
    Retrieve Weather Parameters for: belyy yar,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=belyy%20yar
    Retrieve Weather Parameters for: atasu,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=atasu
    Retrieve Weather Parameters for: bredasdorp,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bredasdorp
    Retrieve Weather Parameters for: west bay,ky
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=west%20bay
    Retrieve Weather Parameters for: krutikha,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=krutikha
    Retrieve Weather Parameters for: kavieng,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kavieng
    Retrieve Weather Parameters for: moba,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=moba
    Retrieve Weather Parameters for: maghama,mr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maghama
    Retrieve Weather Parameters for: el dorado,co
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=el%20dorado
    Retrieve Weather Parameters for: ntoum,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ntoum
    Retrieve Weather Parameters for: poum,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=poum
    Retrieve Weather Parameters for: takapau,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=takapau
    Retrieve Weather Parameters for: basco,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=basco
    Retrieve Weather Parameters for: longyearbyen,sj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=longyearbyen
    Retrieve Weather Parameters for: attawapiskat,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=attawapiskat
    Retrieve Weather Parameters for: axim,gh
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=axim
    Retrieve Weather Parameters for: tual,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tual
    Retrieve Weather Parameters for: yar-sale,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yar-sale
    Retrieve Weather Parameters for: mercedes,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mercedes
    Retrieve Weather Parameters for: tanout,ne
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tanout
    Retrieve Weather Parameters for: saskylakh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saskylakh
    Retrieve Weather Parameters for: cockburn town,tc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cockburn%20town
    Retrieve Weather Parameters for: sokolo,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sokolo
    Retrieve Weather Parameters for: coihaique,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=coihaique
    Retrieve Weather Parameters for: tuatapere,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tuatapere
    Retrieve Weather Parameters for: ciudad bolivar,ve
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ciudad%20bolivar
    Retrieve Weather Parameters for: port elizabeth,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20elizabeth
    Retrieve Weather Parameters for: shangrao,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shangrao
    Retrieve Weather Parameters for: sturgis,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sturgis
    Retrieve Weather Parameters for: powassan,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=powassan
    Retrieve Weather Parameters for: hamilton,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hamilton
    Retrieve Weather Parameters for: provideniya,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=provideniya
    Retrieve Weather Parameters for: det udom,th
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=det%20udom
    Retrieve Weather Parameters for: vicuna,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vicuna
    Retrieve Weather Parameters for: baiima,sl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=baiima
    Retrieve Weather Parameters for: myanaung,mm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=myanaung
    Retrieve Weather Parameters for: saint george,bm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint%20george
    Retrieve Weather Parameters for: chumikan,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chumikan
    Retrieve Weather Parameters for: rudsar,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rudsar
    Retrieve Weather Parameters for: tambun,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tambun
    Retrieve Weather Parameters for: avarua,ck
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=avarua
    Retrieve Weather Parameters for: codrington,ag
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=codrington
    Retrieve Weather Parameters for: iqaluit,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=iqaluit
    Retrieve Weather Parameters for: luena,ao
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=luena
    Retrieve Weather Parameters for: mazagao,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mazagao
    Retrieve Weather Parameters for: vestmannaeyjar,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vestmannaeyjar
    Retrieve Weather Parameters for: beloha,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beloha
    Retrieve Weather Parameters for: svetlogorsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=svetlogorsk
    Retrieve Weather Parameters for: caapucu,py
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=caapucu
    Retrieve Weather Parameters for: vanimo,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vanimo
    Retrieve Weather Parameters for: georgetown,sh
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=georgetown
    Retrieve Weather Parameters for: sao joao da barra,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sao%20joao%20da%20barra
    Retrieve Weather Parameters for: palabuhanratu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=palabuhanratu
    Retrieve Weather Parameters for: rodbyhavn,dk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rodbyhavn
    Retrieve Weather Parameters for: qaanaaq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qaanaaq
    Retrieve Weather Parameters for: lalsot,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lalsot
    Retrieve Weather Parameters for: januaria,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=januaria
    Retrieve Weather Parameters for: piacabucu,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=piacabucu
    Retrieve Weather Parameters for: tervel,bg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tervel
    Retrieve Weather Parameters for: kirakira,sb
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kirakira
    Retrieve Weather Parameters for: mataura,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mataura
    Retrieve Weather Parameters for: san quintin,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20quintin
    Retrieve Weather Parameters for: fayaoue,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=fayaoue
    Retrieve Weather Parameters for: riyadh,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=riyadh
    Retrieve Weather Parameters for: bonthe,sl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bonthe
    Retrieve Weather Parameters for: kamenskoye,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kamenskoye
    Retrieve Weather Parameters for: amderma,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=amderma
    Retrieve Weather Parameters for: tabou,ci
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tabou
    Retrieve Weather Parameters for: marcona,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=marcona
    Retrieve Weather Parameters for: port moresby,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20moresby
    Retrieve Weather Parameters for: komsomolskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=komsomolskiy
    Retrieve Weather Parameters for: mbacke,sn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mbacke
    Retrieve Weather Parameters for: arkhangelsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=arkhangelsk
    Retrieve Weather Parameters for: punta arenas,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=punta%20arenas
    Retrieve Weather Parameters for: altinopolis,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=altinopolis
    Retrieve Weather Parameters for: khandyga,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khandyga
    Retrieve Weather Parameters for: cherskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cherskiy
    Retrieve Weather Parameters for: atar,mr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=atar
    Retrieve Weather Parameters for: pospelikha,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pospelikha
    Retrieve Weather Parameters for: galle,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=galle
    Retrieve Weather Parameters for: pokhara,np
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pokhara
    Retrieve Weather Parameters for: amga,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=amga
    Retrieve Weather Parameters for: ushuaia,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ushuaia
    Retrieve Weather Parameters for: saint-philippe,re
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-philippe
    Retrieve Weather Parameters for: lima,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=lima
    Retrieve Weather Parameters for: meiganga,cm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=meiganga
    Retrieve Weather Parameters for: parrita,cr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=parrita
    Retrieve Weather Parameters for: porto murtinho,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=porto%20murtinho
    Retrieve Weather Parameters for: yulara,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yulara
    Retrieve Weather Parameters for: saint-joseph,re
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=saint-joseph
    Retrieve Weather Parameters for: emerald,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=emerald
    Retrieve Weather Parameters for: tucuman,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tucuman
    Retrieve Weather Parameters for: namatanai,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=namatanai
    Retrieve Weather Parameters for: nabire,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nabire
    Retrieve Weather Parameters for: deming,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=deming
    Retrieve Weather Parameters for: cayenne,gf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cayenne
    Retrieve Weather Parameters for: pasighat,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pasighat
    Retrieve Weather Parameters for: port blair,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=port%20blair
    Retrieve Weather Parameters for: karakendzha,tj
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=karakendzha
    Retrieve Weather Parameters for: vila franca do campo,pt
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vila%20franca%20do%20campo
    Retrieve Weather Parameters for: jiroft,ir
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jiroft
    Retrieve Weather Parameters for: klaksvik,fo
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=klaksvik
    Retrieve Weather Parameters for: katangli,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=katangli
    Retrieve Weather Parameters for: avera,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=avera
    Retrieve Weather Parameters for: shimoda,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=shimoda
    Retrieve Weather Parameters for: alice town,bs
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=alice%20town
    Retrieve Weather Parameters for: conakry,gn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=conakry
    Retrieve Weather Parameters for: faanui,pf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=faanui
    Retrieve Weather Parameters for: porto novo,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=porto%20novo
    Retrieve Weather Parameters for: redlands,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=redlands
    Retrieve Weather Parameters for: salinas,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=salinas
    Retrieve Weather Parameters for: kang,bw
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kang
    Retrieve Weather Parameters for: labuhan,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=labuhan
    Retrieve Weather Parameters for: ghugus,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ghugus
    Retrieve Weather Parameters for: voh,nc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=voh
    Retrieve Weather Parameters for: harper,lr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=harper
    Retrieve Weather Parameters for: oss,nl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=oss
    Retrieve Weather Parameters for: hailar,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hailar
    Retrieve Weather Parameters for: severo-kurilsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=severo-kurilsk
    Retrieve Weather Parameters for: qiongshan,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=qiongshan
    Retrieve Weather Parameters for: komsomolets,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=komsomolets
    Retrieve Weather Parameters for: pangnirtung,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pangnirtung
    Retrieve Weather Parameters for: zaigrayevo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zaigrayevo
    Retrieve Weather Parameters for: portage,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=portage
    Retrieve Weather Parameters for: kajaani,fi
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kajaani
    Retrieve Weather Parameters for: puerto del rosario,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puerto%20del%20rosario
    Retrieve Weather Parameters for: ambon,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ambon
    Retrieve Weather Parameters for: daru,pg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=daru
    Retrieve Weather Parameters for: samusu,ws
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=samusu
    Retrieve Weather Parameters for: mbengwi,cm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mbengwi
    Retrieve Weather Parameters for: puri,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=puri
    Retrieve Weather Parameters for: assiniboia,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=assiniboia
    Retrieve Weather Parameters for: poso,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=poso
    Retrieve Weather Parameters for: tigil,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tigil
    Retrieve Weather Parameters for: kahului,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kahului
    Retrieve Weather Parameters for: sassandra,ci
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sassandra
    Retrieve Weather Parameters for: aykhal,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aykhal
    Retrieve Weather Parameters for: birao,cf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=birao
    Retrieve Weather Parameters for: jipijapa,ec
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=jipijapa
    Retrieve Weather Parameters for: thunder bay,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=thunder%20bay
    Retrieve Weather Parameters for: chicama,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chicama
    Retrieve Weather Parameters for: dakar,sn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=dakar
    Retrieve Weather Parameters for: upernavik,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=upernavik
    Retrieve Weather Parameters for: mar del plata,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mar%20del%20plata
    Retrieve Weather Parameters for: plettenberg bay,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=plettenberg%20bay
    Retrieve Weather Parameters for: rungata,ki
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rungata
    Retrieve Weather Parameters for: nargana,pa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nargana
    Retrieve Weather Parameters for: meulaboh,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=meulaboh
    Retrieve Weather Parameters for: salinopolis,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=salinopolis
    Retrieve Weather Parameters for: florence,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=florence
    Retrieve Weather Parameters for: nizhneyansk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nizhneyansk
    Retrieve Weather Parameters for: illoqqortoormiut,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=illoqqortoormiut
    Retrieve Weather Parameters for: castro,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=castro
    Retrieve Weather Parameters for: tombouctou,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tombouctou
    Retrieve Weather Parameters for: chokurdakh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chokurdakh
    Retrieve Weather Parameters for: gazojak,tm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gazojak
    Retrieve Weather Parameters for: petaling jaya,my
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=petaling%20jaya
    Retrieve Weather Parameters for: tongliao,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tongliao
    Retrieve Weather Parameters for: plainview,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=plainview
    Retrieve Weather Parameters for: victoria,sc
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=victoria
    Retrieve Weather Parameters for: yanahuanca,pe
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=yanahuanca
    Retrieve Weather Parameters for: ahipara,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ahipara
    Retrieve Weather Parameters for: new norfolk,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=new%20norfolk
    Retrieve Weather Parameters for: rawson,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=rawson
    Retrieve Weather Parameters for: hambantota,lk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hambantota
    Retrieve Weather Parameters for: broome,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=broome
    Retrieve Weather Parameters for: araouane,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=araouane
    Retrieve Weather Parameters for: mackay,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mackay
    Retrieve Weather Parameters for: antofagasta,cl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=antofagasta
    Retrieve Weather Parameters for: gouyave,gd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gouyave
    Retrieve Weather Parameters for: catamarca,ar
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=catamarca
    Retrieve Weather Parameters for: inta,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=inta
    Retrieve Weather Parameters for: biak,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=biak
    Retrieve Weather Parameters for: charters towers,au
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=charters%20towers
    Retrieve Weather Parameters for: zhanakorgan,kz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=zhanakorgan
    Retrieve Weather Parameters for: cabra,ph
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cabra
    Retrieve Weather Parameters for: san bartolome de tirajana,es
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=san%20bartolome%20de%20tirajana
    Retrieve Weather Parameters for: grand-santi,gf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=grand-santi
    Retrieve Weather Parameters for: clyde river,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=clyde%20river
    Retrieve Weather Parameters for: quatre cocos,mu
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=quatre%20cocos
    Retrieve Weather Parameters for: ngawen,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ngawen
    Retrieve Weather Parameters for: bukama,cd
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bukama
    Retrieve Weather Parameters for: tyukhtet,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tyukhtet
    Retrieve Weather Parameters for: pacific grove,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pacific%20grove
    Retrieve Weather Parameters for: sedelnikovo,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sedelnikovo
    Retrieve Weather Parameters for: chuy,uy
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chuy
    Retrieve Weather Parameters for: anton lizardo,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=anton%20lizardo
    Retrieve Weather Parameters for: tupik,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tupik
    Retrieve Weather Parameters for: hovd,mn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hovd
    Retrieve Weather Parameters for: srem,pl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=srem
    Retrieve Weather Parameters for: sao filipe,cv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=sao%20filipe
    Retrieve Weather Parameters for: kaya,bf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kaya
    Retrieve Weather Parameters for: east london,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=east%20london
    Retrieve Weather Parameters for: richards bay,za
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=richards%20bay
    Retrieve Weather Parameters for: felidhoo,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=felidhoo
    Retrieve Weather Parameters for: kribi,cm
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kribi
    Retrieve Weather Parameters for: bengkulu,id
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bengkulu
    Retrieve Weather Parameters for: teguldet,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=teguldet
    Retrieve Weather Parameters for: asau,tv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=asau
    Retrieve Weather Parameters for: nieuw amsterdam,sr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=nieuw%20amsterdam
    Retrieve Weather Parameters for: herten,de
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=herten
    Retrieve Weather Parameters for: karamea,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=karamea
    Retrieve Weather Parameters for: ilulissat,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ilulissat
    Retrieve Weather Parameters for: pasni,pk
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=pasni
    Retrieve Weather Parameters for: constitucion,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=constitucion
    Retrieve Weather Parameters for: leningradskiy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=leningradskiy
    Retrieve Weather Parameters for: longlac,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=longlac
    Retrieve Weather Parameters for: liwale,tz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=liwale
    Retrieve Weather Parameters for: aquiraz,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=aquiraz
    Retrieve Weather Parameters for: gongzhuling,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=gongzhuling
    Retrieve Weather Parameters for: kushima,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kushima
    Retrieve Weather Parameters for: douentza,ml
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=douentza
    Retrieve Weather Parameters for: along,in
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=along
    Retrieve Weather Parameters for: ohara,jp
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ohara
    Retrieve Weather Parameters for: chapais,ca
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=chapais
    Retrieve Weather Parameters for: kodiak,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kodiak
    Retrieve Weather Parameters for: khatanga,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=khatanga
    Retrieve Weather Parameters for: bluff,nz
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bluff
    Retrieve Weather Parameters for: bethel,us
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bethel
    Retrieve Weather Parameters for: cay,tr
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=cay
    Retrieve Weather Parameters for: taolanaro,mg
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=taolanaro
    Retrieve Weather Parameters for: najran,sa
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=najran
    Retrieve Weather Parameters for: guerrero negro,mx
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=guerrero%20negro
    Retrieve Weather Parameters for: mokhsogollokh,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=mokhsogollokh
    Retrieve Weather Parameters for: olinda,br
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=olinda
    Retrieve Weather Parameters for: srednekolymsk,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=srednekolymsk
    Retrieve Weather Parameters for: bilibino,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=bilibino
    Retrieve Weather Parameters for: kudahuvadhoo,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=kudahuvadhoo
    Retrieve Weather Parameters for: omboue,ga
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=omboue
    Retrieve Weather Parameters for: maniitsoq,gl
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=maniitsoq
    Retrieve Weather Parameters for: vaitupu,wf
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=vaitupu
    Retrieve Weather Parameters for: hithadhoo,mv
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=hithadhoo
    Retrieve Weather Parameters for: ostrovnoy,ru
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=ostrovnoy
    Retrieve Weather Parameters for: olafsvik,is
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=olafsvik
    Retrieve Weather Parameters for: tubruq,ly
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=tubruq
    Retrieve Weather Parameters for: beihai,cn
    http://api.openweathermap.org/data/2.5/weather?appid=74d08b88df719aeffa06bf72b52c87d8&units=imperial&q=beihai



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

    Oops, we couldn't retrieve the weather parameters for (57) cities
    Your new DataFrame has the weather information for (443) unique cities
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



![png](output_15_1.png)



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



![png](output_16_1.png)



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



![png](output_17_1.png)



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



![png](output_18_1.png)



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
    2.The wind speed for most of the cities is under 10 mph. The median is 6.93mph. There is a possible outlier with a wind speed of 39.15mph in Pahrump in the US
    3. The clouds seem pretty disperse, whithout a visible correlation with the latitude.

