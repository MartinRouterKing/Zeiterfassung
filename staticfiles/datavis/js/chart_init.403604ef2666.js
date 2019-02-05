
 $(document).ready(function() {
       $.ajax({
        url: 'load_canvas/',
        data: {
          'selectedOption': 'line'
        },
        success: function (data) {
          $("#toggle_chart").html(data);

          Chart.defaults.global.defaultFontColor = 'white';
            new Chart(document.getElementById("line-chart"), {
                type: 'line',
                data: {
                labels: ['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'],

                datasets: [{
                    data: chart_init_data,
                    label: chart_init_label,
                    borderColor: "#d43f3a",
                    fill: false,
                    backgroundColor: "#d43f3a",
                    },
                    ]},
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    title: {
                    showTooltips: true,
                    display: true,
                    text: 'Arbeitszeit pro Monat (in Stunden)',
                    fontColor: "white"
                    }
                }
            });

           }
       });
 });