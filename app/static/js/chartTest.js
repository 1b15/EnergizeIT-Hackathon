
var glob_chart = new ApexCharts(
            document.querySelector("#myChart"),
            options
        );

function getChart(){
    $.ajax({

        url : '/getData',
        context:document.body,
        type : 'GET',
        success : function(data) {
            buildChart(JSON.parse(data))
        },
        error : function(request,error)
            {
                alert("Request: "+JSON.stringify(request));
            }
    });
}
function generateData(count, yrange) {
            var i = 0;
            var series = [];
            while (i < count) {
                var x = 'w' + (i + 1).toString();
                var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

                series.push({
                    x: x,
                    y: y
                });
                i++;
            }
            return series;
}

function buildChart(data) {
    if (typeof glob_chart !== 'undefined') {
        glob_chart.destroy();
    }
    var options = {
            chart: {
                height: 350,
                type: 'heatmap',
            },
            dataLabels: {
                enabled: false
            },
            colors: ["#008FFB"],
            series: [{
                    name: 'Metric1',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric2',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric3',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric4',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric5',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric6',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric7',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric8',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                },
                {
                    name: 'Metric9',
                    data: generateData(18, {
                        min: 0,
                        max: 90
                    })
                }
            ],
            title: {
                text: 'HeatMap Chart (Single color)'
            },

        }

        var chart = new ApexCharts(
            document.querySelector("#myChart"),
            options
        );

        glob_chart = chart;

        chart.render();
}
