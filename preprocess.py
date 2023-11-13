import json

f = open('counties-10m.json')
data = json.load(f)
arcsAll = data['arcs']
countiesAll = data['objects']['counties']
want = ["36", "34", "09"]
countiesGeometry = []
namesNY = ['Orange', 'Dutchess', 'Ulster', 'Nassau', 'Suffolk', 'Sullivan', 'Rockland', 'Putnam', 'Westchester', 'Richmond', 'Bronx', 'New York', 'Queens', 'Kings']
# namesNY = ['Orange', 'Dutchess', 'Ulster', 'Nassau', 'Sullivan', 'Rockland', 'Putnam', 'Westchester', 'Richmond', 'Bronx', 'New York', 'Queens', 'Kings']
namesNJ = ['Bergen', 'Middlesex', 'Monmouth', 'Ocean', 'Somerset', 'Essex', 'Union', 'Morris', 'Sussex', 'Hunterdon', 'Mercer', 'Passaic', 'Hudson',]
namesCT = ['Fairfield', 'New Haven', 'Litchfield' ]
namesAll = namesNY + namesNJ + namesCT


for i in countiesAll['geometries']:
    newProperties = { 'idFIPS': "", 'idState': "", 'name': "" }
    newGeometry = { 'type': "Polygon", 'arcs': [], 'properties': {} }
    id = i['id'][0:2]
    name = i['properties']['name']
    # if name == "Suffolk":
    #     print(i)
    if id == '36' and name in namesNY: 
        newProperties['idState'] = 'NY'
        newProperties['name'] = i['properties']['name']
        newProperties['idFIPS'] = id
        newGeometry['arcs'] = i['arcs']
        newGeometry['properties'] = newProperties
        countiesGeometry.append(newGeometry)
    elif id == '09' and name in namesCT:
        newProperties['idState'] = 'CT'
        newProperties['name'] = i['properties']['name']
        newProperties['idFIPS'] = id
        newGeometry['arcs'] = i['arcs']
        newGeometry['properties'] = newProperties
        countiesGeometry.append(newGeometry)
    elif id == '34' and name in namesNJ:
        newProperties['idState'] = 'NJ'
        newProperties['name'] = i['properties']['name']
        newProperties['idFIPS'] = id
        newGeometry['arcs'] = i['arcs']
        newGeometry['properties'] = newProperties
        countiesGeometry.append(newGeometry)
countiesNew = { 'type': "GeometryCollection", 'geometries': countiesGeometry }
dataNew = { 'type': "Topology", 'arcs': arcsAll, 'transform': data['transform'],'objects': { 'counties': countiesNew } }
# print(dataNew)

with open("countiesTriState.json", "w") as outfile:
    json.dump(dataNew, outfile)
