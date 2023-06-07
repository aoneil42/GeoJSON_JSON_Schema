import json

esrisdjson = input("Esri Service Definition JSON file: ")
geojsonschema = "geojsonschema.json"
projecttitle = input("Project title: ")
projectdesc = input("Project description: ")
outputjson = projecttitle+"_JSONSchema.json"

typedict = {"esriFieldTypeOID":"integer",
            "esriFieldTypeString":"string",
            "esriFieldTypeInteger":"number",
            "esriFieldTypeSmallInteger":"number",
            "esriFieldTypeSingle":"number",
            "esriFieldTypeDouble":"number",
            "esriFieldTypeDate":"string",
            "typeIdField":"string"}

def loadjsonfields(file):
    with open(file) as f:
        srcjson = json.load(f)
        fields = srcjson['fields']
        #print(fields)
    return fields

def payload(j):
    pload = {}
    for field in j:
        ftype = field.get('type', "string")
        flen = field.get('length', "")
        if flen == "":
            pload[field['name']] = {"type": ftype}
        else:
            pload[field['name']] = {"type" : ftype,"maxLength" : flen}
    for sub in pload:
        if pload[sub]['type'] in typedict:
            pload[sub]['type'] = typedict[pload[sub]['type']]
    return pload

def insertpayload(j, p):
    with open(j) as f:
        jsonsch = json.load(f)
        jsonsch['title'] = prjecttitle
        jsonshc['description'] = projectdesc
        jsonsch['definitions']['feature']['properties']['properties']['oneOf'][0]['properties'] = p
    return jsonsch

originschema = loadjsonfields(esrisdjson)
fieldpayload = payload(originschema)
results = json.dumps(insertpayload(geojsonschema, fieldpayload), indent=4)

with open(outputjson, "w") as outfile:
    outfile.write(results)
