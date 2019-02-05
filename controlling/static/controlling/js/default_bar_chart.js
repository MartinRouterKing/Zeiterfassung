
        Chart.defaults.global.defaultFontColor = 'white';
    var ctx = document.getElementById("bar-chart")
    new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Typ"],
                datasets: [
                    {
                    label: "Kein Typ Ausgewählt",
                    backgroundColor: '#1abc9c',
                    data: [0,01],
                    },
                    ],
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                                    scales: {
                        yAxes: [{
                            display: true,
                                ticks: {
                                    min: 0,
                                    max: 10,
                                    stepSize: 2
                                }
                            }]
                        },

                    legend: { position: 'bottom' },
                    tooltips: {
                        enabled: true
                        },
                },
            });
