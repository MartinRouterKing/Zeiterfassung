       function  favorite_change(){
        console.log("click");
      var categoriesId = $('id_categories').val();                         // get the selected country ID from the HTML input
      var checkBox = document.getElementById("id-of-input");
      $.ajax({                                                  // initialize an AJAX request
        url: 'load_elements/',                                  // set the url of the request (= localhost:8000/hr/ajax/element/)
        data: {
          'categories': categoriesId,                            // add the country id to the GET parameters
          'checked': checkBox.checked
        },
        success: function (data) {                              // `data` is the return of the `load_element` view function
          console.log(data);
          $("#id_element").html(data)

         $('#id_element .fc-event').each(function() {
            var colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6',, '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6',];
            var color = colors[categoriesId];
            $(this).css({"border-left": "5px solid #20749b"});

                                                    // store data so the calendar knows to render an event upon drop
           $(this).data('event', {
            title: $.trim($(this).text()),                      // use the element's text as the event title
            type: categoriesId,
            stick: true,                      // maintain when user navigates (see docs on the renderEvent method)
            duration: '01:00:00'              // will set the duration during drag of event
            });

        $('#id_element .fc-event').draggable({
        helper: 'clone',
        zIndex: 999,
        revert: true,      // will cause the event to go back to its
        revertDuration: 0  //  original position after the drag
        });

        });
        }
      });
   };