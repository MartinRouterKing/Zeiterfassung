
  function saveMyData(event){
    $.ajax({
          type: 'POST',
          url: 'post/',
          data: {
                action: 'save',
                id: event.id,
                title: event.title,
                type: event.type,
                start: event.start.toString(),
                end:   event.end.toString(),
                note: event.note,
                save: event.save,
                csrfmiddlewaretoken: csrf_token
          },
    });
    }