import json

f = open('counties-10m.json')
data = json.load(f)
arcsAll = data['arcs']
countiesAll = data['objects']['counties']
want = ["36", "34", "09"]
countiesGeometry = []
# namesNY = ['Orange', 'Dutchess', 'Ulster', 'Nassau', 'Suffolk', 'Sullivan', 'Rockland', 'Putnam', 'Passaic', 'Hudson', 'Bergen', 'Westchester', 'Richmond', 'Bronx', 'New York', 'Queens', 'Kings']
namesNY = ['Orange', 'Dutchess', 'Ulster', 'Nassau', 'Sullivan', 'Rockland', 'Putnam', 'Passaic', 'Hudson', 'Bergen', 'Westchester', 'Richmond', 'Bronx', 'New York', 'Queens', 'Kings']
namesNJ = ['Middlesex', 'Monmouth', 'Ocean', 'Somerset', 'Essex', 'Union', 'Morris', 'Sussex', 'Hunterdon', 'Mercer']
namesCT = ['Fairfield', 'New Haven', 'Litchfield' ]
namesAll = namesNY + namesNJ + namesCT


for i in countiesAll['geometries']:
    newProperties = { 'idFIPS': "", 'idState': "", 'name': "" }
    newGeometry = { 'type': "Polygon", 'arcs': [], 'properties': {} }
    id = i['id'][0:2]
    name = i['properties']['name']
    if id in want and name in namesAll:
        newProperties['name'] = i['properties']['name']
        newProperties['idFIPS'] = id
        newGeometry['arcs'] = i['arcs']
        if id == '36':
            newProperties['idState'] = 'NY'
        elif id == '09':
            newProperties['idState'] = 'CT'
        elif id == '34':
            newProperties['idState'] = 'NJ'
        newGeometry['properties'] = newProperties
        countiesGeometry.append(newGeometry)
        countiesNew = { 'type': "GeometryCollection", 'geometries': countiesGeometry }
        dataNew = { 'type': "Topology", 'arcs': arcsAll, 'transform': data['transform'],'objects': { 'counties': countiesNew } }

with open("countiesTriState.json", "w") as outfile:
    json.dump(dataNew, outfile)
