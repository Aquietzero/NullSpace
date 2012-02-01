(function() {

  $(function() {
    var sidebar, width;
    sidebar = $('#sidebar');
    width = sidebar.width();
    sidebar.css({
      'margin-left': -width + 30 + 'px'
    });
    return sidebar.hover(function() {
      return sidebar.animate({
        'margin-left': 0
      });
    }, function() {
      return sidebar.animate({
        'margin-left': -width + 30 + 'px'
      });
    });
  });

}).call(this);
