      $('body').on('hidden.bs.modal', '.modal', function () {
        $(this).removeData('bs.modal');
        $("#modal_content_id").children().remove();;
      });
