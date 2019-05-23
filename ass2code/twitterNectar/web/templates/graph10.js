var seriesJS10 = {{ series10|safe }}
Highcharts.chart('container10', {
    chart: {
        zoomType: 'xy', 
        width : 600,
        height : null,
    },
    title: {
        text: 'Income VS Normalized number of Tweets'
    },
    subtitle: {
        text: 'Born in Europe'
    },
    xAxis: [{
        categories: [
            'Ballarat',
            'Bendigo',
            'Geelong',
            'Melbourne',
            'Newcastle',
            'Sydney',
            'Wollongong',
            'Brisbane',
            'Townsville',
            'Carins',
        ],
        crosshair: true
    }],
    yAxis: [{ // Primary yAxis
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        },
        title: {
            text: 'Normalized num of Tweets',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        }
    }, { // Secondary yAxis
        title: {
            text: 'Percentage',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        labels: {
            format: '{value} %',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        opposite: true
    }],
    tooltip: {
        shared: true
    },
    legend: {
        layout: 'vertical',
        x: 150,
        verticalAlign: 'top',
        y: 70,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255,255,255,0.25)'
    },
    series: seriesJS10
});