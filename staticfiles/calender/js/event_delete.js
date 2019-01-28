  function deleteMyData(event){
    $.ajax({
          type: 'POST',
          url: 'post/',
          data: {
                action: 'delete',
                id: event.id,
                title: event.title,
                start: event.start.toString(),
                end:   event.end.toString(),
                note: event.note,
                save: event.save,
                csrfmiddlewaretoken: csrf_token
          },
    });
    }