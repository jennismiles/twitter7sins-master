import couchdb
import json

couch = couchdb.Server('http://admin:admin@103.6.254.57:5984')

vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne']
nsw_area = ['Newcastle', 'Sydney', 'Wollongong']
qld_area = ['Brisbane', 'Townsville', 'Cairns']
all_areas = vic_area + nsw_area + qld_area
search_word = ['envy', 'envious', 'jealous', 'I desire', 'I want', 'I wish']

db = couch['tweets_data']

# Collect hashtags that appear more than once in each area
area_hashtags = {}
for item in db.view('area_general/hashtag_area', group=True, group_level=2):
    if item.value > 1:
        area = item.key[1]
        if area in area_hashtags.keys():
            area_hashtags[area].append(item.key[0])
        else:
            area_hashtags[area] = [item.key[0]]

for row in area_hashtags.items():
    print(row)

out = json.dumps(area_hashtags)
f = open('/home/ubuntu/web/json_output/content and timeline/hashtags appeared more than once (separated by areas).json', 'w')
f.write(out)
f.close()


# Collect hashtags that appear more than once for all areas
allAreas_hashtags = {}
for item in db.view('area_general/hashtag_area', group=True, group_level=1):
    if item.value > 1:
        hashtag = item.key[0]
        allAreas_hashtags[hashtag] = item.value

sorted_allAreas_hashtags = sorted(allAreas_hashtags.items(), key=lambda kv: kv[1], reverse=True)

for row in sorted_allAreas_hashtags:
    print(row)

out = json.dumps(sorted_allAreas_hashtags)
f = open('/home/ubuntu/web/json_output/content and timeline/hashtags appeared more than once (all areas).json', 'w')
f.write(out)
f.close()


# Count the number of Tweets in a time range
num_Tweets_time = {}
num_Tweets_time['Average of all areas'] = {}
for area in all_areas:
    num_Tweets_time[area] = {}

for item in db.view('area_general/timeline_area', group=True, group_level=2):
    area = item.key[1]
    time = item.key[0]
    if area is not None and time is not None:
        count = item.value
        num_Tweets_time[area][time] = count


for element in db.view('area_general/timeline_area', group=True, group_level=1):
    time = element.key[0]
    count = element.value
    num_Tweets_time['Average of all areas'][time] = round(count/len(all_areas))

for row in num_Tweets_time.items():
    print(row)

out = json.dumps(num_Tweets_time)
f = open('/home/ubuntu/web/json_output/content and timeline/number of tweets in time ranges of a day.json', 'w')
f.write(out)
f.close()

