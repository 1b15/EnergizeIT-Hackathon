function setupSockets() {
    var socket = io();
    socket.on('giveData', function (message) {
        console.log(JSON.parse(message));
        var res = JSON.parse(message);
        updateCharts(res['lastTen'], res['probabilities']);
    });
    setInterval(function() { socket.emit('giveData')}, 1000);

    function updateCharts(data1,data2) {

        myPlotChart.data.datasets[0].data = data1;
        myPieChart.data.datasets[0].data = data2;
        //myBarChart.data.datasets[0].data = data3;
        console.log(data1);
        console.log(data2);
        myPlotChart.update();
        myPieChart.update();
        //myBarChart.update();
    }
}