document.addEventListener('DOMContentLoaded', () => {
    var limit = 0;
    
    // When the crust or size dropdown changes get the correct model
    $("#whichsize, #whichcrust").change(function () {
        var size = $("#whichsize").val();
        var crust = $("#whichcrust").val();
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
                            text: item.fields['flavour'] + " $" + item.fields['price']
                        }));
                    });

                }
            }
        });
    });

    // Set the limit, number of toppings that can be checked
    $("#whichflavmodel").change(function () {
        console.log($(this).val());
        if ($(this).val() < 5) {
            limit = $(this).val() -1;
        } else {
            limit = 5;
        }
        
    });
    
    // Limit the number of toppings that can be selected based on the flavour model 
    $('input.singlecheckbox').on('change', function(evt) {
       if($(this).siblings(':checked').length >= limit) {
           this.checked = false;
       }
    });
    
    // Hide the steack and cheese sub options
    $('#sc').css({
        'display': 'none'
     });

    // Show and hide the Steak and Cheese options
    $('#whichsub').change(function() {
        var $option = $(this).find('option:selected');
        var text = $option.text();
        if (text.includes("Steak and Cheese")) {
            $('#sc').show();
        } else {
            $('#sc').hide();
        }
        
    });

});