import csv
import couchdb

couch = couchdb.Server('http://admin:admin@103.6.254.57:5984')


# Upload census data to CouchDB
vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne']
nsw_area = ['Newcastle', 'Sydney', 'Wollongong']
qld_area = ['Brisbane', 'Townsville', 'Cairns']
all_areas = vic_area + nsw_area + qld_area

csvfile_paths = ['/home/ubuntu/web/Data/education_employment_LGA.csv', '/home/ubuntu/web/Data/people_population_LGA.csv',
                 '/home/ubuntu/web/Data/income_LGA.csv']
db_names = ['education_employment_lga', 'people_population_lga', 'income_lga']

for i in range(3):
    path = csvfile_paths[i]
    db_name = db_names[i]
    with open(path, encoding='utf-8-sig') as csvfile:
        try:
            db = couch.create(db_name)
        except:
            db = couch[db_name]  # database already created
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if row['YEAR'] == "2016":
                    Label = row['LABEL'].split()
                    if Label[0] in all_areas:  # e.g. Melbourne (C)
                        row['LABEL'] = Label[0]
                        row['_id'] = Label[0]
                        db.save(row)
                        print(row)
                    if Label[0] == "Greater" and Label[1] in all_areas:  # e.g. Greater Geelong (C)
                        row['LABEL'] = Label[1]
                        row['_id'] = Label[1]
                        db.save(row)
                        print(row)
            except:
                # ignore duplicates (doc with same id)
                continue
    print(db_name + " upload completed")





