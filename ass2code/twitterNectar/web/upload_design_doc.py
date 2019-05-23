import couchdb

couch = couchdb.Server('http://admin:admin@103.6.254.57:5984')

doc1 = {
  "_id": "_design/area_population",
  "views": {
    "population_15to64": {
      "map": "function (doc) {\n  if (doc.LABEL && doc[\"Working Age Population (15-64 years)\"] && doc.Total) {total = parseFloat(doc.Total.replace(/,/g, ''))\n    working = parseFloat(doc[\"Working Age Population (15-64 years)\"])\n    var workingAgePopulation = total * working * 0.01 * 0.3 * 0.001;\n    emit(doc.LABEL, workingAgePopulation);\n  }\n}"
    },
    "population_background": {
      "map": "function (doc) {\n  total = parseFloat(doc['Total Born Overseas'])\n  Asia = parseFloat(doc['Born in South-East Asia']) + parseFloat(doc['Born in North-East Asia']) + parseFloat(doc['Born in Southern, Central Asia'])\n  Europe = parseFloat(doc['Born in North-West Europe']) + parseFloat(doc['Born in Southern & Eastern Europe'])\n  Americas = parseFloat(doc['Born in Americas'])\n  Oceania = parseFloat(doc['Born in Oceania, Antarctica (exc. Australia)'])\n  Africa = parseFloat(doc['Born in North Africa, Middle East'])\n  result = {\"total\": total, \"Asia\": Asia, \"Europe\": Europe, \"Americas\": Americas, \"Oceania\": Oceania, \"Africa\": Africa}\n  \n  emit(doc.LABEL, result)\n}"
    }
  },
  "language": "javascript"
}

db = couch['people_population_lga']
db.save(doc1)

doc2 = {
  "_id": "_design/area_general",
  "views": {
    "hashtag_area": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.place && doc.hashtag) {\n    doc.hashtag.forEach (function (element) {\n      emit([element, doc.place], 1);\n    })\n  }\n}"
    },
    "timeline_area": {
      "map": "function (doc) {\n  var time, hour, range\n  if (doc.place && doc.datetime) {\n    var time = doc.datetime.split(\" \")[1]\n    var hour = time.split(\":\")[0]\n    if (hour >= 0 && hour < 6) {\n      range = \"00:00 - 05:59\"\n    }\n    else if (hour >= 6 && hour < 12) {\n      range = \"06:00 - 11:59\"\n    }\n    else if (hour >= 12 && hour < 18) {\n      range = \"12:00 - 17:59\"\n    }\n    else if (hour >=18) {\n      range = \"18:00 - 23:59\"\n    }\n    emit([range, doc.place], 1)\n  }\n}",
      "reduce": "_sum"
    },
    "area_keyword_range": {
      "reduce": "function (keys, values, rereduce) {\n  // var days = values.forEach( function(element) {\n  //   return parseInt(element.split(\"-\")[2]);\n  // })\n  \n  // Return the maximum numeric value.\n  var min = Infinity;\n  for(var i = 0; i < values.length; i++) {\n    if (typeof values[i] == 'number') {\n      min = Math.min(values[i], min);\n    }\n  }\n  var range = 32 - min;\n  return range;\n}",
      "map": "function (doc) {\n  if (doc.place && doc.keyword && doc.datetime) {\n    var date = doc.datetime.split(\" \")[0];\n    emit([doc.place, doc.keyword], parseInt(date.split(\"-\")[2], 10));\n  }\n}"
    },
    "actual_num_tweets": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.place && doc.keyword) {\n    emit([doc.place, doc.keyword], 1);\n  }\n}"
    }
  },
  "language": "javascript"
}

db = couch['tweets_data']
db.save(doc2)
