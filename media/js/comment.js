(function() {

  $(function() {
    $('.leaveComment').css({
      'display': 'none'
    });
    return $('.leaveCommentButton').bind('click', function() {
      return $(this).next('.leaveComment').slideToggle();
    });
  });

}).call(this);
