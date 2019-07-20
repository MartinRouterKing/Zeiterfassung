$('#cat_select').selectpicker();
$('#wie_select').selectpicker();
$('#obj_select').selectpicker();
$('#user_select').selectpicker();

$('.input-daterange input').each(function() {
    $(this).datepicker({
        format: "mm-yyyy",
        startView: "months",
        minViewMode: "months",
        autoclose: true,
        }).on('changeDate', function(e) {
            console.log(e);

        });
    });