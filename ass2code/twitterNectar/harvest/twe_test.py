from searchtweets import ResultStream, gen_rule_payload, load_credentials,collect_results
import couchdb
import time

couch = couchdb.Server('http://admin:admin@127.0.0.1:5984')
try:
    db = couch['tweets_data']
except:
    db = couch.create('tweets_data')


premium_search_args=load_credentials(filename="harvest/creds.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)


search_word=['envious','jealous','I desire','envy','I want','I wish']
Australian_city=['Melbourne', 'Sydney', 'Geelong', 'Bendigo', 'Ballart', 'NewCastle', 'Brisbane', 'Townsville', 'Carins']


for word in search_word:
    if word=='envy':
        time.sleep(90)
    keyword=word
    for search_area in Australian_city:
        query_place=':'.join(('place',search_area))
        place=search_area
        rule=gen_rule_payload(" ".join((keyword,query_place,"lang:en")),results_per_call=100)
        tweets = collect_results(rule,
                                 max_results=100,
                                 result_stream_args=premium_search_args)
        data_to_couch = []
        for i in range(len(tweets)):
            data_to_couch.append({})

        i = 0
        for t in tweets:
            data_to_couch[i]['_id'] = t.id
            data_to_couch[i]['text'] = t.all_text
            data_to_couch[i]['coordinates'] = t.geo_coordinates
            data_to_couch[i]['datetime'] = str(t.created_at_datetime)
            data_to_couch[i]['keyword'] = keyword
            data_to_couch[i]['place'] = place
            data_to_couch[i]['hashtag']=t.hashtags
            i += 1

        for js in data_to_couch:
            try:
                db.save(js)
            except:
                continue

