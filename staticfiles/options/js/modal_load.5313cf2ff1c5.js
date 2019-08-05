$('#id_cat_choice').change( function () {
    var inner = '<i  id="load_icon" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="font-size:18px; color:#f8f9fa;"></i>'
    load_icon = document.getElementById('load_cat_select');
    load_icon.innerHTML = inner;

    var cat_choice = $('#id_cat_choice option:selected').text();

        $.ajax({
          type: 'POST',
          url: 'ajax_load_from_groups/',
          data:{
          cat_choice: cat_choice,
          csrfmiddlewaretoken: csrf_token
          },
          success: function(data){
           $('#from-group-container').html(data);
            load_icon.innerHTML = "Bitte Typ auswählen";
          }
        });

});


function add_from_group(event){

    counter = ($('#from-group-container')[0].length/4)
    counter ++;

    var cat_choice = $('#id_cat_choice')[0][$('#id_cat_choice')[0].selectedIndex].text

    $.ajax({
          type: 'POST',
          url: 'ajax_add_from_group/',
          data:{
          counter: counter,
          cat_choice: cat_choice,
          csrfmiddlewaretoken: csrf_token
          },
          success: function(data){
            $('#from-group-container').append(data).show('slow');
          }
        });

}

function del_from_group(event){
    element = $(event).parent().parent().parent().remove().hide('slow');
    element.remove()
}

function save_element(){
    var cat_choice = $('#id_cat_choice')[0][$('#id_cat_choice')[0].selectedIndex].text
    var inner = '<i  id="load_icon" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="font-size:18px; color:#f8f9fa;"></i>'
    load_icon = document.getElementById('sub_button');
    load_icon.innerHTML = inner;

    var count = $('#from-group-container')[0].length;
    var element = [];
    var wie = [];
    var obj = [];
    var calc = [];
        var group = 0;
        for (var i = 0, n = count; i < n; i++) {
            group ++;
            if (group==1){
                element.push($('#from-group-container')[0][i][$('#from-group-container')[0][i].selectedIndex].text);
            }
            else if (group==2){
                wie.push($('#from-group-container')[0][i].value);
            }
            else if (group==3){
                obj.push($('#from-group-container')[0][i].value);
            }
            else if (group==4){
                calc.push($('#from-group-container')[0][i][$('#from-group-container')[0][i].selectedIndex].text);
                group = 0;

            }
          }

         $.ajax({
          type: 'POST',
          url: 'ajax_save_element/',
          data:{
          cat_choice: cat_choice,
          element: element,
          wie: wie,
          obj: obj,
          calc: calc,
          csrfmiddlewaretoken: csrf_token
          },
          success: function(){

              var inner = '<p>Gespeichert</p><iid="load_icon" class="glyphicon glyphicon-ok" style="font-size:18px; color:#f8f9fa;"></i>'
              load_icon = document.getElementById('sub_button');
              load_icon.innerHTML = inner;

              load_icon.innerHTML = "Speichern";
          }
        });
}

function save_limit(){

    var user = $('#id_users')[0][$('#id_users')[0].selectedIndex].text
    var inner = '<i  id="load_icon" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="font-size:18px; color:#f8f9fa;"></i>'
    load_icon = document.getElementById('sub_button_limit');
    load_icon.innerHTML = inner;
    var limit = $('#sel1')[0][$('#sel1')[0].selectedIndex].text;
    console.log(user);
    console.log(limit);
    $.ajax({
      type: 'POST',
      url: 'ajax_user_limit/',
      data:{
      user_choice: user,
      limit: limit,
      csrfmiddlewaretoken: '{{csrf_token}}'
      },
      success: function(){

          var inner = '<p>Gespeichert</p><iid="load_icon" class="glyphicon glyphicon-ok" style="font-size:18px; color:#f8f9fa;"></i>'
          load_icon = document.getElementById('sub_button_limit');
          load_icon.innerHTML = inner;

          load_icon.innerHTML = "Speichern";
      }
    });

};