var seriesJS1 = {{ series1|safe }}
Highcharts.chart('container1', {
    chart: {
        /*spacingBottom: 15,
        spacingTop: 10,
        spacingLeft: 10,
        spacingRight: 300,*/
        width: 600,
        height: null,
    },

    title: {
        text: 'Num of Tweets in time range of a day'
    },
    subtitle: {
        text: 'Victoria'
    },
    xAxis: {
        categories: [
            '00:00 - 05:59',
            '06:00 - 11:59', 
            '12:00 - 17:59', 
            '18:00 - 23:59',
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of Tweets'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: seriesJS1
});