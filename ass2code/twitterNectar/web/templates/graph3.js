var seriesJS3 = {{ series3|safe }}
Highcharts.chart('container3', {
    chart: {
        width: 600,
        height: null,
    },

    title: {
        text: 'Num of Tweets in time range of a day'
    },
    subtitle: {
        text: 'Queensland'
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
    series: seriesJS3
});