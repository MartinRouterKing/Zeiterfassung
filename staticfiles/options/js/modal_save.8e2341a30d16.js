function ajax_save(){
    var form = $('#modal_form');
    url = $('#modal_form').attr('action');

   $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function (data) {
                var newHTML = data;
                $('#modal_content_id').html(newHTML);
                }
    });
}
