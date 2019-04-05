document.addEventListener('DOMContentLoaded', () => {
    $("#whichsize").change(function () {
        var size = $(this).val();
        console.log($(this).val());

        $.ajax({
            url: '/getmodel',
            data: {
                'size': size
            },
            dataType: 'json',
            success: function (data) {
                if (data) {
                    console.log(data);
                    $("#flavmodel").empty();
                    $.each(data, function (i, item) {
                        $('#flavmodel').append($('<option>', {
                            value: item.pk,
                            text: item.fields['flavour'] + item.fields['price']
                        }));
                    });

                }
            }
        });
    });
});