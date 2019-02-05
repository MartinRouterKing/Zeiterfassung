
function selectedValue(id){
        var select1 = document.getElementById(id);
    var selected1 = [];
    for (var i = 0; i < select1.length; i++) {
        if (select1.options[i].selected) selected1.push(select1.options[i].value);
    }
    return selected1;
}

function search(){
    var inner = '<i  id="load_icon" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="font-size:18px; color:#f8f9fa;"></i>'
    load_icon = document.getElementById('sub_button');
    load_icon.innerHTML = inner;

    var search_user = selectedValue("id_user");
    var search_cat = selectedValue("cat_select");
    var start_date = document.getElementById("start_date").value;
    var end_date = document.getElementById("end_date").value;
    var switch_per = document.getElementById("switch_per").checked;
    console.log(switch_per);


    $.ajax({
            type: "POST",
            url: 'controlling/search/',
            data: {
            'search_user': search_user,
            'search_cat': search_cat,
            'start_date': start_date,
            'end_date': end_date,
            'percent': switch_per,
            csrfmiddlewaretoken: crf_token
            },
            success: function(data){
                $('#pie_container').html(data);

            }
        });

        $.ajax({
            type: "POST",
            url: 'controlling/search_line/',
            data: {
            'search_user': search_user,
            'search_cat': search_cat,
            'start_date': start_date,
            'end_date': end_date,
            'percent': switch_per,
            csrfmiddlewaretoken: crf_token
            },
            success: function(data){
                $('#line_container').html(data);
                load_icon.innerHTML = "Berechnen";

            }
        });


};

       $('#id_user').selectpicker();
       $('#cat_select').selectpicker();


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