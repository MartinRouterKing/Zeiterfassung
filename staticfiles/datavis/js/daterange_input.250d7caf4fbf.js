
$('.input-daterange input').each(function() {
    $(this).datepicker({
        format: "mm.yyyy",
        startView: "months",
        minViewMode: "months",
        autoclose: true,
        }).on('changeDate', function(e) {
            var start_date = document.getElementById("start_date").value;
            console.log(start_date);
            $.ajax({
                url: 'load_bar_cat/',
                data: {
                  'selectedDate': start_date
                },
                success: function (data) {
                  $("#canvas-container").html(data);
                },
            });
        });
    });


