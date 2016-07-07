$(document).ready(function(){
    $('.switcher').on('click', function(){
    	if ($('.ajaxed').length ==0){
	        $.ajax({
	    	    url:'/jobs/',
	    	    cache: false,
	    	    data: {name:'ajax'},
	    	    type: 'POST',
	    	    success: function(html){
	    		    $('.jobs_list').append(html);
	    		    $('.switcher').html('Скрыть')
	    	}
	    });
	    }
	   
	    else{
	    	$('.ajaxed').toggle();
	    	$('.switcher').html('Скрыть/показать')
	    }
    })
});