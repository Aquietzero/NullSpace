(function() {

  $(function() {
    var sidebar, width;
    sidebar = $('#sidebar');
    width = sidebar.width();
    sidebar.css({
      'margin-right': -width + 30 + 'px'
    });
    return sidebar.hover((function() {
      return $(this).animate({
        'margin-right': 0
      });
    }), (function() {
      return $(this).animate({
        'margin-right': -width + 30 + 'px'
      });
    }));
  });

}).call(this);
