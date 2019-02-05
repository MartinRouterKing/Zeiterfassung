
              Chart.defaults.global.defaultFontColor = 'white';

var BarChart =  new Chart(document.getElementById("bar-chart_cat"), {
                type: 'bar',

                data: {
                labels: ['Typ'],
                datasets: bar_chart_data
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: { position: 'bottom' },
                },
            });

            var resizeId;
        $(window).resize(function() {
            clearTimeout(resizeId);
            resizeId = setTimeout(afterResizing, 100);
        });


        function afterResizing(){
            var canvasheight=document.getElementById("bar-chart_cat").height;
            if(canvasheight <=250)
            {
                window.BarChart.options.legend.display=false;
            }
            else
            {
                window.BarChart.options.legend.display=true;
            }
            window.BarChart.update();
        }
