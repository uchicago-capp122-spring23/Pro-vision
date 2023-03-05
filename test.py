import plotly.express as px 
import urllib.request, json 

# with urllib.request.urlopen("https://uchicago.box.com/shared/static/0hyrwzbja479o01f0ke99b418zvsudjr.geojson") as url:
#         chicagoMap = json.load(url)

# count = 0
# for area in chicagoMap['features']:
#     count += 1
#     print(area['properties']["pri_neigh"])
# print(count)

# {"type":"FeatureCollection","features": [{"type":"Feature","geometry":{"type":"MultiPolygon","coordinates":[[[[-87.67256900493521,41.83764109527692],[-87.67377263703384,41.83674076083116],[-87.67617990123108,41.83854142972268],[-87.6773835333297,41.83764109527692],[-87.67497626913246,41.8358404263854],[-87.67617990123108,41.83494009193964],[-87.67858716542833,41.83494009193964],[-87.67979079752695,41.83403975749388],[-87.67979079752695,41.832239088602364],[-87.67858716542833,41.831338754156604],[-87.6665508444421,41.831338754156604],[-87.66293994814623,41.83403975749388],[-87.66083359197364,41.8358404263854],[-87.65932905185036,41.83494009193964],[-87.65692178765312,41.83674076083116],[-87.65451452345587,41.83674076083116],[-87.65331089135725,41.83764109527692],[-87.65331089135725,41.83944176416844],[-87.65210725925863,41.8403420986142],[-87.64969999506138,41.8403420986142],[-87.64849636296276,41.84124243305996],[-87.64849636296276,41.844843770843],[-87.64729273086414,41.84574410528876],[-87.64488546666689,41.84574410528876],[-87.64368183456827,41.84664443973452],[-87.64368183456827,41.85024577751756],[-87.64247820246965,41.85114611196332],[-87.6400709382724,41.85114611196332],[-87.63886730617378,41.85204644640908],[-87.6400709382724,41.853171864466276],[-87.6400709382724,41.854522366134916],[-87.63886730617378,41.855647784192115],[-87.63766367407516,41.858348787529394],[-87.63646004197653,41.859249121975154],[-87.63646004197653,41.86285045975819],[-87.63886730617378,41.86465112864971],[-87.63886730617378,41.86645179754123],[-87.64127457037102,41.86825246643275],[-87.64127457037102,41.87005313532427],[-87.64247820246965,41.87095346977003],[-87.64488546666689,41.87095346977003],[-87.64608909876551,41.87185380421579],[-87.64608909876551,41.87365447310731],[-87.64488546666689,41.87455480755307],[-87.6400709382724,41.87455480755307],[-87.63886730617378,41.87545514199883],[-87.6400709382724,41.87635547644459],[-87.64488546666689,41.87635547644459],[-87.64969999506138,41.87275413866155],[-87.65090362716,41.87365447310731],[-87.65090362716,41.87545514199883],[-87.65210725925863,41.87635547644459],[-87.65451452345587,41.87635547644459],[-87.65692178765312,41.878156145336106],[-87.65932905185036,41.87635547644459],[-87.66173631604761,41.878156145336106],[-87.66414358024485,41.878156145336106],[-87.66534721234348,41.879056479781866],[-87.66534721234348,41.880857148673385],[-87.6665508444421,41.881757483119145],[-87.66775447654072,41.880857148673385],[-87.66775447654072,41.879056479781866],[-87.66895810863934,41.878156145336106],[-87.67136537283659,41.878156145336106],[-87.67377263703384,41.87635547644459],[-87.67617990123108,41.87635547644459],[-87.68099442962557,41.87275413866155],[-87.6882162222173,41.87275413866155],[-87.68941985431593,41.87185380421579],[-87.68941985431593,41.87005313532427],[-87.69062348641455,41.86915280087851],[-87.69543801480904,41.86915280087851],[-87.69664164690766,41.86825246643275],[-87.69664164690766,41.86645179754123],[-87.69423438271042,41.86465112864971],[-87.69423438271042,41.86285045975819],[-87.69664164690766,41.86104979086667],[-87.69664164690766,41.857448453083634],[-87.69904891110491,41.855647784192115],[-87.69904891110491,41.85204644640908],[-87.69784527900629,41.85114611196332],[-87.69543801480904,41.85114611196332],[-87.6930307506118,41.8493454430718],[-87.6882162222173,41.8493454430718],[-87.68701259011868,41.84844510862604],[-87.6882162222173,41.84754477418028],[-87.69062348641455,41.84754477418028],[-87.69423438271042,41.844843770843],[-87.6930307506118,41.84394343639724],[-87.68580895802006,41.84394343639724],[-87.68460532592144,41.84304310195148],[-87.68701259011868,41.84124243305996],[-87.68580895802006,41.8403420986142],[-87.68099442962557,41.8403420986142],[-87.67858716542833,41.84214276750572],[-87.67617990123108,41.84191768389428],[-87.67256900493521,41.83944176416844],[-87.67256900493521,41.83764109527692]]]]},"properties":{"search_id":"neighborhood_health_clinics", "GEOID": "1"}}]}

with urllib.request.urlopen("https://uchicago.box.com/shared/static/0p9qwi5wgdfksz1avixqkwednmsptijo.json") as url:
        isochroneMap = json.load(url)
healthClinicsCoverage = isochroneMap["neighborhood_health_clinics"]
for i, item in enumerate(healthClinicsCoverage['features']):
    item['properties']['isoID'] = str(i)
print(healthClinicsCoverage)




# import sys
# import matplotlib
# matplotlib.use('WebAgg')

# # 'GTK3Agg', 'GTK3Cairo', 'MacOSX', 'nbAgg', 'Qt4Agg', 'Qt4Cairo', 'Qt5Agg', 
# # 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 
# # 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template'
# import matplotlib.pyplot as plt
# import numpy as np

# # X axis parameter:
# xaxis = np.array([2, 8])

# # Y axis parameter:
# yaxis = np.array([4, 9])

# plt.plot(xaxis, yaxis)
# plt.show()

# plt.savefig('line.png')
# sys.stdout.flush()