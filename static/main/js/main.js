  

  $(document).ready(function() {
  $(".show-hide-btn").click(function() {
    var id = $(this).data("id");
    $("#half-" + id).toggle();//hide/show..
    $("#full-" + id).toggle();
  })
})

