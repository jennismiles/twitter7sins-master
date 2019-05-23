import couchdb
import json
import pandas as pd

couch = couchdb.Server('http://admin:admin@103.6.254.57:5984')


vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne']
nsw_area = ['Newcastle', 'Sydney', 'Wollongong']
qld_area = ['Brisbane', 'Townsville', 'Cairns']
all_areas = vic_area + nsw_area + qld_area
search_word = ['envy', 'envious', 'jealous', 'I desire', 'I want', 'I wish']


# Create dictionary to store the number of tweets for each keyword and area
tweet_count = dict.fromkeys(all_areas)
for area in tweet_count.keys():
    tweet_count[area] = dict.fromkeys(search_word)
    for keyword in tweet_count[area].keys():
        tweet_count[area][keyword] = {"actual number of envy tweets": 0,
                                      "day range": 0,
                                      "estimated number of envy tweets per year": 0}
    tweet_count[area]["population_factor"] = 0

print("Dictionary initialised")

# Get values from couchdb - tweets_data
db_tweet = couch['tweets_data']

# Get actual number of tweets
for item in db_tweet.view('area_general/actual_num_tweets', group=True, group_level=2):
    area = item.key[0]
    keyword = item.key[1]
    count = item.value
    tweet_count[area][keyword]["actual number of envy tweets"] = count

# Get day range
for item in db_tweet.view('area_general/area_keyword_range', group=True, group_level=2):
    area = item.key[0]
    keyword = item.key[1]
    days = item.value
    tweet_count[area][keyword]["day range"] = days
    count = tweet_count[area][keyword]["actual number of envy tweets"]
    if count:
        tweet_count[area][keyword]["estimated number of envy tweets per year"] = round(count * 365 / days)

# Get population factor
db_population = couch['people_population_lga']
for item in db_population.view('area_population/population_15to64'):
    area = item.key
    factor = item.value
    tweet_count[area]["population_factor"] = factor

print("Dictionary filled in")

# Calculate the total number of tweets for each area
for item in tweet_count.items():
    area, element = item
    total = 0
    for keyword in search_word:
        total += element[keyword]["estimated number of envy tweets per year"]
    tweet_count[area]["estimated total number of envy tweets per year"] = total
    normalised_total = round(total/tweet_count[area]["population_factor"])
    tweet_count[area]["normalised total number of envy tweets per year"] = normalised_total

print("Dictionary complete")

out = json.dumps(tweet_count)
f = open('/home/ubuntu/web/json_output/scenario/number of tweets.json', 'w')
f.write(out)
f.close()

# Create general dictionary for all scenarios
num_tweet = dict.fromkeys(all_areas)
for key in num_tweet.keys():
    num_tweet[key] = {}
for area in all_areas:
    estimated_total = tweet_count[area]["estimated total number of envy tweets per year"]
    normalised_total = tweet_count[area]['normalised total number of envy tweets per year']
    num_tweet[area]["estimated total number of envy tweets per year"] = estimated_total
    num_tweet[area]['normalised total number of envy tweets per year'] = normalised_total

# Scenario 1: education level
education = dict.fromkeys(all_areas)
for key in education:
    education[key] = {}
db = couch['education_employment_lga']
rows = db.view('_all_docs', include_docs=True)
for row in rows:
    area = row['doc']['LABEL']
    if area in education.keys():
        education[area]["estimated total number of envy tweets per year"] = \
            tweet_count[area]["estimated total number of envy tweets per year"]
        education[area]['normalised total number of envy tweets per year'] = \
            tweet_count[area]['normalised total number of envy tweets per year']

        education[area]['Did not go to school (%)'] = row['doc']['Did not go to school']
        education[area]['Completed Year 9 or equivalent (%)'] = row['doc']['Completed Year 9 or equivalent ']
        education[area]['Completed Year 12 or equivalent (%)'] = row['doc']['Completed Year 12 or equivalent ']
        education[area]['Persons With Post School Qualification (%)'] = \
            row['doc']['Persons With Post School Qualification']
        education[area]['Persons with Postgraduate degree (%)'] = row['doc']['Postgraduate degree']

for item in education.items():
    print(item)

out = json.dumps(education)
f = open('/home/ubuntu/web/json_output/scenario/education level.json', 'w')
f.write(out)
f.close()
print("education level complete")

# Scenario 2: employment type
employment = dict.fromkeys(all_areas)
for key in employment:
    employment[key] = {}
db = couch['education_employment_lga']
rows = db.view('_all_docs', include_docs=True)
for row in rows:
    area = row['doc']['LABEL']
    if area in employment.keys():
        employment[area]["estimated total number of envy tweets per year"] = \
            tweet_count[area]["estimated total number of envy tweets per year"]
        employment[area]['normalised total number of envy tweets per year'] = \
            tweet_count[area]['normalised total number of envy tweets per year']

        employment[area]['Managers (%)'] = row['doc']['Managers']
        employment[area]['Professionals (%)'] = row['doc']['Professionals']
        employment[area]['Technicians and Trades Workers (%)'] = row['doc']['Technicians and Trades Workers']
        employment[area]['Community, Personal Service Workers (%)'] = row['doc']['Community, Personal Service Workers']
        employment[area]['Clerical, Administrative Workers (%)'] = row['doc']['Clerical, Administrative Workers']
        employment[area]['Sales Workers (%)'] = row['doc']['Sales Workers']
        employment[area]['Machinery Operators, Drivers (%)'] = row['doc']['Machinery Operators, Drivers']
        employment[area]['Labourers (%)'] = row['doc']['Labourers']
        employment[area]['Unemployment rate'] = row['doc']['Unemployment rate']

for item in employment.items():
    print(item)

out = json.dumps(employment)
f = open('/home/ubuntu/web/json_output/scenario/employment type.json', 'w')
f.write(out)
f.close()
print("employment type complete")


# Scenario 3: income
income = dict.fromkeys(all_areas)
for key in income:
    income[key] = {}
db = couch['income_lga']
rows = db.view('_all_docs', include_docs=True)
for row in rows:
    area = row['doc']['LABEL']
    if area in income.keys():
        income[area]["estimated total number of envy tweets per year"] = \
            tweet_count[area]["estimated total number of envy tweets per year"]
        income[area]['normalised total number of envy tweets per year'] = \
            tweet_count[area]['normalised total number of envy tweets per year']

        income[area]["Total income earners - median age"] = \
            row['doc']["Total income earners (excl. Government pensions and allowances) - median age"]
        income[area]["Median Total income"] = \
            row['doc']["Median Total income (excl. Government pensions)"].replace(",", "")
        income[area]["Gini coefficient"] = \
            row['doc']["Total income (excl. Government pensions and allowances) - Gini coefficient"]
        income[area]["Median equivalised total household income (weekly)"] = \
            row['doc']["Median equivalised total household income (weekly)"].replace(",", "")

for item in income.items():
    print(item)

out = json.dumps(income)
f = open('/home/ubuntu/web/json_output/scenario/income.json', 'w')
f.write(out)
f.close()
print("income complete")


# Scenario 4: background
background = dict.fromkeys(all_areas)
for key in background:
    background[key] = {}
db = couch['people_population_lga']
for item in db.view('area_population/population_background'):
    area = item.key
    value = item.value
    if area in background.keys():
        background[area]["estimated total number of envy tweets per year"] = \
            tweet_count[area]["estimated total number of envy tweets per year"]
        background[area]['normalised total number of envy tweets per year'] = \
            tweet_count[area]['normalised total number of envy tweets per year']

        background[area]["Total Born Overseas"] = round(value["total"], 1)
        background[area]["Born in Europe"] = round(value["Europe"], 1)
        background[area]["Born in Asia"] = round(value["Asia"], 1)
        background[area]["Born in Americas"] = round(value["Americas"], 1)
        background[area]["Born in Oceania, Antarctica (exc. Australia)"] = round(value["Oceania"], 1)
        background[area]["Born in North Africa, Middle East"] = round(value["Africa"], 1)


for item in background.items():
    print(item)

out = json.dumps(background)
f = open('/home/ubuntu/web/json_output/scenario/background.json', 'w')
f.write(out)
f.close()
print("background complete")

# Calculate correlations
correlations = {}

df = pd.DataFrame(education.values())
df = df.astype(float)
correlations['education'] = {}
for key in list(df.columns.values):
    if key not in ["estimated total number of envy tweets per year", "normalised total number of envy tweets per year"]:
        correlations['education'][key] = round(df['normalised total number of envy tweets per year'].corr(df[key]), 2)

df = pd.DataFrame(employment.values())
df = df.astype(float)
correlations['employment'] = {}
for key in list(df.columns.values):
    if key not in ["estimated total number of envy tweets per year", "normalised total number of envy tweets per year"]:
        correlations['employment'][key] = round(df['normalised total number of envy tweets per year'].corr(df[key]), 2)

df = pd.DataFrame(income.values())
df = df.astype(float)
correlations['income'] = {}
for key in list(df.columns.values):
    if key not in ["estimated total number of envy tweets per year", "normalised total number of envy tweets per year"]:
        correlations['income'][key] = round(df['normalised total number of envy tweets per year'].corr(df[key]), 2)

df = pd.DataFrame(background.values())
df = df.astype(float)
correlations['background'] = {}
for key in list(df.columns.values):
    if key not in ["estimated total number of envy tweets per year", "normalised total number of envy tweets per year"]:
        correlations['background'][key] = round(df['normalised total number of envy tweets per year'].corr(df[key]), 2)


for item in correlations.items():
    print(item)

out = json.dumps(correlations)
f = open('/home/ubuntu/web/json_output/scenario/correlations.json', 'w')
f.write(out)
f.close()
print("correlations complete")
