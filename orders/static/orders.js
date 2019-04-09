document.addEventListener('DOMContentLoaded', () => {
    var limit = 0;
    $("#whichsize, #whichcrust").change(function () {
        var size = $("#whichsize").val();
        var crust = $("#whichcrust").val();
        console.log($("#whichsize").val());
        console.log($("#whichcrust").val());
        $('input:checkbox').each(function() { this.checked = false; });
        limit=0;
        $.ajax({
            url: '/getmodel',
            data: {
                'size': size,
                'crust': crust
            },
            dataType: 'json',
            success: function (data) {
                if (data) {
                    console.log(data);
                    $("#whichflavmodel").empty();
                    $.each(data, function (i, item) {
                        $('#whichflavmodel').append($('<option>', {
                            value: item.pk,
                            text: item.fields['flavour'] + " " + item.fields['price']
                        }));
                    });

                }
            }
        });
    });

    $("#whichflavmodel").change(function () {
        console.log($(this).val());
        if ($(this).val() < 5) {
            limit = $(this).val() -1;
        } else {
            limit = 5;
        }
        
    });
    
    $('input.singlecheckbox').on('change', function(evt) {
       if($(this).siblings(':checked').length >= limit) {
           this.checked = false;
       }
    });

});