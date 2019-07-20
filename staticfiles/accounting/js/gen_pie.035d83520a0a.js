
function gen_pie() {
    console.log("START GENPIE");
    pie_labels = [];
    pie_values = [];
    var table = document.getElementsByTagName("table")[0];
    console.log(table);
    var ges =  parseInt(table.rows[table.rows.length-1].cells[3].innerHTML);

    for (var c = 4; c< table.rows[0].cells.length; c++) {

        pie_labels.push(table.rows[0].cells[c].innerText);
        var percent = 0
        for (var i = 1; i< table.rows.length - 1; i++) {

            if (table.rows[i].cells[c].innerHTML != "—") {

                var percent = percent + Math.round(parseFloat(table.rows[i].cells[c].innerHTML *100 / ges));


            };
        };
        pie_values.push(percent);
    }


        Chart.defaults.global.defaultFontColor = 'white';
    var ctx = document.getElementById("bar-chart")
    new Chart(ctx, {
    type: 'bar',
    data: {
      labels: pie_labels,
                datasets: [
                    {
                    label: "Verteilung der Kostenträger in Prozent",
                    backgroundColor: ['#1abc9c', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6','#2ecc71',],
                    data: pie_values,
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
                                    stepSize: 5
                                }
                            }],
                        xAxes: [{
                            ticks: {
                                display: false
                            }
                        }]
                        },
                    legend: {
                         labels: {
                         boxWidth: 0,
                        }
                    },
                    tooltips: {
                        enabled: true
                        },
                },
            });

}