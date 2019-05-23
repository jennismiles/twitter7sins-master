import json
from flask import Flask, render_template
#from pprint import pprint

#import db
app = Flask(__name__)

percen_data = {
    'name': 'Percentage',
        'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
                'data': [],
                'tooltip': {
                'valueSuffix': ''
                }}

@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/member')
def memberpage():
    return render_template("member.html")


@app.route('/analysis')
def analysistest():
    return render_template('dataanalysis.html')

@app.route('/graph1.js')
def timeline1():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f)
        
        
        vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne','Average']
        nsw_area = ['Newcastle', 'Sydney', 'Wollongong','Average']
        qld_area = ['Brisbane', 'Townsville', 'Cairns','Average']
        
        json_series = []
        vic_series = []
        nsw_series = []
        qld_series = []
        for key,value in data.items():
            new_data = {
                'name': str(key),
                'data': []
            }
            for time,count in value.items():
                new_data['data'].append(count)
            json_series.append(new_data)
            
            if new_data["name"] in vic_area:
                vic_series.append(new_data)
            if new_data['name'] in nsw_area:
                nsw_series.append(new_data)
            if new_data["name"] in qld_area:
                qld_series.append(new_data)
    return render_template('graph1.js', series1=vic_series)

@app.route('/graph2.js')
def timeline2():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f)
        
        
        vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne','Average']
        nsw_area = ['Newcastle', 'Sydney', 'Wollongong','Average']
        qld_area = ['Brisbane', 'Townsville', 'Cairns','Average']
        
        json_series = []
        vic_series = []
        nsw_series = []
        qld_series = []
        for key,value in data.items():
            new_data = {
                'name': str(key),
                'data': []
            }
            for time,count in value.items():
                new_data['data'].append(count)
            json_series.append(new_data)
            
            if new_data["name"] in vic_area:
                vic_series.append(new_data)
            if new_data['name'] in nsw_area:
                nsw_series.append(new_data)
            if new_data["name"] in qld_area:
                qld_series.append(new_data)
    return render_template('graph2.js', series2=nsw_series)

@app.route('/graph3.js')
def timeline3():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f)
        
        
        vic_area = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne','Average']
        nsw_area = ['Newcastle', 'Sydney', 'Wollongong','Average']
        qld_area = ['Brisbane', 'Townsville', 'Cairns','Average']
        
        json_series = []
        vic_series = []
        nsw_series = []
        qld_series = []
        for key,value in data.items():
            new_data = {
                'name': str(key),
                'data': []
            }
            for time,count in value.items():
                new_data['data'].append(count)
            json_series.append(new_data)
            
            if new_data["name"] in vic_area:
                vic_series.append(new_data)
            if new_data['name'] in nsw_area:
                nsw_series.append(new_data)
            if new_data["name"] in qld_area:
                qld_series.append(new_data)
    return render_template('graph3.js', series3=qld_series)

@app.route('/graph4.js')
def edulevel9():
    with open('web/json_output/scenario/education level.json') as f:
        data = json.load(f)
    percen_data = {
            'name': 'Percentage',
            'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
            'data': [],
            'tooltip': {
            'valueSuffix': ''
            }}
    series4 = [percen_data, norm_data]
    for key,value in data.items():
        for types,count in value.items():
            if types == "Completed Year 9 or equivalent (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph4.js', series4=series4)
#
@app.route('/graph5.js')
def edulevel10():
    with open('web/json_output/scenario/education level.json') as f:
        data = json.load(f)
    percen_data = {
        'name': 'Percentage',
            'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
                'data': [],
                'tooltip': {
                'valueSuffix': ''
                }}
    series5 = [percen_data, norm_data]
    for key,value in data.items():
        for types,count in value.items():
            if types == "Persons with Postgraduate degree (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    print(series5)
    return render_template('graph5.js', series5=series5)

@app.route('/graph6.js')
def employtypelabour():
    with open('web/json_output/scenario/employment type.json') as f:
        data = json.load(f)
    percen_data = {
    'name': 'Percentage',
        'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
                'data': [],
                'tooltip': {
                'valueSuffix': ''
                }}
    series6 = [percen_data, norm_data]
    for key,value in data.items():
        for types,count in value.items():
            if types == "Labourers (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph6.js', series6=series6)
#


@app.route('/graph7.js')
def employtypeprof():
    with open('web/json_output/scenario/employment type.json') as f:
        data = json.load(f)
    percen_data = {
    'name': 'Percentage',
        'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
                'data': [],
                'tooltip': {
                'valueSuffix': ''
                }}
    series7 = [percen_data, norm_data]
    for key,value in data.items():
        for types,count in value.items():
            if types == "Professionals (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph7.js', series7=series7)





@app.route('/graph8.js')
def gini():
    norm_data = {
        'name': 'Normalized num of tweets',
            'type': 'spline',
                'data': [],
                'tooltip': {
                'valueSuffix': ''
                }}
    gini_data = {
        'name': 'Gini coefficient',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
        'valueSuffix': ' %'
        }}
    with open('web/json_output/scenario/income.json') as f:
        data = json.load(f)
    series8 = [gini_data, norm_data]
    for key,value in data.items():
        for types,count in value.items():
            if types == "Gini coefficient":
                gini_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    print (series8)
    return render_template('graph8.js', series8=series8)


@app.route('/graph9.js')
def bornasia():
    percen_data = {
    'name': 'Percentage',
        'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
    'name': 'Normalized num of tweets',
        'type': 'spline',
            'data': [],
            'tooltip': {
                'valueSuffix': ''
                }}
    with open('web/json_output/scenario/background.json') as f:
        data = json.load(f)
        series9 = [percen_data, norm_data]
        for key,value in data.items():
            for types,count in value.items():
                if types == "Born in Asia":
                    percen_data['data'].append(float(count))
                elif types == "normalised total number of envy tweets per year":
                    norm_data['data'].append(count)
    return render_template('graph9.js', series9=series9)


#
@app.route('/graph10.js')
def borneur():
    percen_data = {
    'name': 'Percentage',
        'type': 'column',
            'yAxis': 1,
            'data': [],
            'tooltip': {
            'valueSuffix': ' %'
            }}
    norm_data = {
    'name': 'Normalized num of tweets',
        'type': 'spline',
            'data': [],
            'tooltip': {
                'valueSuffix': ''
                }}
    with open('web/json_output/scenario/background.json') as f:
        data = json.load(f)
        series10 = [percen_data, norm_data]
        for key,value in data.items():
            for types,count in value.items():
                if types == "Born in Europe":
                    percen_data['data'].append(float(count))
                elif types == "normalised total number of envy tweets per year":
                    norm_data['data'].append(count)
    return render_template('graph10.js', series10=series10)




#@app.route('/index')
#def index():
#    categories = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
#
#    #chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
#    series = [
#        {
#        'name': 'John',
#        'data': [5, 3, 4, 7, 2]
#        },
#        {
#        'name': 'Jane',
#        'data': [2, 2, 3, 2, 1]
#        }
#    ]
#    #db.samplefunction()
#    #title = {"text": 'My Title'}
#    #xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
#    #yAxis = {"title": {"text": 'yAxis Label'}}
#
#    return render_template('index.html', series=series, categories=categories)
#



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=80, passthrough_errors=True)

#if __name__ == "__main__":
#    app.run(debug = True)

# , host='127.0.0.1', port=80, passthrough_errors=True
