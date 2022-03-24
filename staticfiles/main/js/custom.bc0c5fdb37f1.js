$(document).ready(function(){
  $("#loadMore").on('click',function(){
    var _currentComments=$(".product-box").length;
    var _limit=$(this).attr('data-limit');
    var _total=$(this).attr('data-total');
    // Start Ajax
    $.ajax({
      url:'/load-more-data',
      data:{
        limit:_limit,
        offset:_currentComments
      },
      dataType:'json',
      beforeSend:function(){
        $("#loadMore").attr('disabled',true);
        $(".load-more-icon").addClass('loading..');
      },
      success:function(res){
        $("#filteredProducts").append(res.data);
        $("#loadMore").attr('disabled',false);
        $(".load-more-icon").removeClass('loading');

        var _totalShowing=$(".product-box").length;
        if(_totalShowing==_total){
          $("#loadMore").remove();
        }
      }
    });
    // End
  });
});