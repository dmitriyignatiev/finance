$(document).ready(function() {
$('form').on('submit', function(){


    $.ajax({
        data:{
            name : $('#name').val()
        },
        type : 'POST',
        url : '/process'


    }).done(function(data){
        if (data.error){
           	$('#errorAlert').text(data.error).show();
			$('#successAlert').hide();

        }else{
            $('#successAlert').text(data.name).show();
			$('#errorAlert').hide();
        }

    });


    e.preventDefault();

});

})