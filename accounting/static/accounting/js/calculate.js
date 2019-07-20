   function calculate() {
      var inner = '<i  id="load_icon" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="font-size:18px; color:#f8f9fa;"></i>'
      load_icon = document.getElementById('sub_button');
      load_icon.innerHTML = inner;
      var cat_selected = $('#cat_select').val();
      var wie_selected = $('#wie_select').val();
      var obj_selected = $('#obj_select').val();
      var userId = $('#user_select').val();
      var start_date = document.getElementById("start_date").value;
      var end_date = document.getElementById("end_date").value;

      $.ajax({
        type: "POST",
        url: "table/",
        data:{
            csrfmiddlewaretoken: csrf_token,
            'ca': cat_selected,
            'wie': wie_selected,
            'obj': obj_selected,
            'user': userId,
            'start_date': start_date,
            'end_date': end_date
            },
            success: function (data) {
            load_icon.innerHTML = 'Berechnen';
          $("#id_table").html(data);
          $("#download_id").attr("hidden",false);
          gen_pie();
        }
        });
};
