function initializePieChart(){
    data = {
        datasets: [{
            data: [0, 0, 0, 0, 0, 0, 0],
            backgroundColor: ["#a6a6a6", "#b3c6ff", "#1a1aff", "#99ff99","#00ff00","#00b300"]
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
            'Nothing',
            'iPhone',
            'Android Smartphone',
            'Ventilator (1)',
            'Ventilator (2)',
            'Ventilator (3)',
        ]
    };
    var alternating_data = [
        [10,20,30],
        [20,20,20]
    ];
    var ctx = document.getElementById('pieChart').getContext('2d');
    return myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            title: {
            display: true,
            text: 'Prediction'
            }}
    });
}

function initializePlotChart(){

    var data = {
		datasets : [
		  {
                pointColor : "#00ff00",
                pointStrokeColor : "#fff",
                data : [0,0,0,0,0,0,0,0,0,0],
                label: "Power Consumption in Watt Hours",
                borderColor: "#4dff4d",
                backgroundColor: "rgba(128, 255, 128, 0.4)",
                pointBackgroundColor: "#00ff00"
			}
		],
      labels: ["1", "2", "3", "4","5", "6","7", "8", "9", "10"]
  };

  // Not sure why the scaleOverride isn't working...
      var optionsNoAnimation = {
        animation : false,
          scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    min: 0,
                    max: 40
                }
            }]
          },
        title: {
            display: true,
            text: 'Current Power Consumption'
        }
      };

      //Get the context of the canvas element we want to select
      var ctx = document.getElementById("plotChart").getContext("2d");
      return myPlotChart = new Chart(ctx, {
          type: 'line',
          data: data,
          options: optionsNoAnimation
      });
}

function initializeBarChart() {
    var data2 = {
      labels: ["iPhone", "Android (SP)", "Ventilator"],
      datasets: [
        {
          backgroundColor: ["#b3c6ff", "#1a1aff","#00b300"],
          data: [250,300,400]
        }
      ]
    } ;
    var options2 = {
      legend: { display: false },
      title: {
        display: true,
        text: 'Total Power Consumption in Watt Hours'
      },
      scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true,
                    min: 0
                }
            }]
          }
    };
    var ctx = document.getElementById("barChart").getContext("2d");
    return myBarChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: data2,
        options: options2
    });
}
