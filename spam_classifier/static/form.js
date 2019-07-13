$(document).ready(function() {

	$('form').on('submit', function(event) {
		$.ajax({
			data : {
				messaje : $('#comments').val()
			},
			type : 'POST',
			url : '/spampr'
		})
		.done(function(data) {
			
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				
			}
			else {
				$('#successAlert').text(data.correct).show();
				$('#errorAlert').hide();

			}

		});

		event.preventDefault();

	});

});