
            Chart.defaults.global.defaultFontColor = 'white';
            new Chart(document.getElementById("line-chart"), {
                type: 'line',
                scaleStartValue : 0,
                data: {
                labels: ['Jan-19', 'Feb-19', 'Mar-19', 'Apr-19', 'May-19', 'Jun-19', 'Jul-19', 'Aug-19', 'Sep-19', 'Oct-19', 'Nov-19', 'Dec-19'],

                datasets: [
                           {
                            data: [0,0,0,0,0,0,0,0,0,0,0,0],
                            label: "Kein Mitarbeiter Ausgewähl",
                            borderColor: "#1abc9c",
                            fill: false
                           },
                          ]
                        },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            display: true,
                                ticks: {
                                    min: 0,
                                    max: 50,
                                    stepSize: 10
                                }
                            }]
                        },
                    title: {
                    display: true,
                    text: 'Arbeitszeit pro Monat (in Stunden)',
                    fontColor: "white"
                    }
                    }
            });

