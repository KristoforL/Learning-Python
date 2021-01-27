import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'Data_Visualization/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_data = all_eq_data['features']
print(len(all_eq_data))

mags,lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

#Map the earthquake
#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Hot',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
    },
}]
my_layout = Layout(title = 'Global Earthquakes')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')























