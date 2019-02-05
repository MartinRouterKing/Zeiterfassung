
   $('input[name=options]').change(function(){
   var selectedOption = $("input:radio[name=options]:checked").val();
   var tempScrollTop = $(window).scrollTop();

   $.ajax({
        url: 'load_canvas/',
        data: {
          'selectedOption': selectedOption
        },
        success: function (data) {
          $("#toggle_chart").html(data);

            Chart.defaults.global.defaultFontColor = 'white';
            new Chart(document.getElementById(selectedOption + "-chart"), {
                type: selectedOption + '',

                data: {
                labels: ['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'],

                datasets: [{
                    backgroundColor: "#d43f3a",
                    data: chart_init_data,
                    label: chart_init_label,
                    borderColor: "#d43f3a",
                    fill: false,
                    },
                    ]},
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    title: {
                    display: true,
                    showTooltips: true,
                    responsive: true,
                    text: 'Arbeitszeit pro Monat (in Stunden)',
                    fontColor: "white"
                    }
                    }
            });
        $(window).scrollTop(tempScrollTop);
        }
        });
   });

