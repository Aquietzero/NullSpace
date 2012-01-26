(function() {

  $(function() {
    return $('.leaveCommentButton').bind('click', function() {
      return $(this).next('.leaveComment').slideToggle();
    });
  });

}).call(this);
