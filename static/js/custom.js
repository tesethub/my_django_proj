$(document).ready(function(){
    $('.switcher').on('click', function(){
    	if ($('.ajaxed').length ==0){
	        $.ajax({
	    	    url:'/jobsfull/',
	    	    cache: false,
	    	    type: 'GET',
	    	    success: function(html){
	    		    $('.jobs_list').append(html);
	    	}
	    });
	    }
	   
	    else{
	    	$('.ajaxed').toggle();
	    	$('.switcher').html('Скрыть/показать')
	    }
    })
});