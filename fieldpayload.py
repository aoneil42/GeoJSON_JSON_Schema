import json

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
        jsonsch['definitions']['feature']['properties']['properties']['oneOf'][0]['properties'] = p
    return jsonsch

originschema = loadjsonfields("testesrischema.json")
fieldpayload = payload(originschema)
results = json.dumps(insertpayload("geojsonJSONSchema.json", fieldpayload), indent=4)

with open("results.json", "w") as outfile:
    outfile.write(results)
