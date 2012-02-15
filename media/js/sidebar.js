(function() {

  $(function() {
    var sidebar, width;
    sidebar = $('#sidebar');
    width = sidebar.width();
    sidebar.css({
      'margin-right': -width + 30 + 'px'
    });
    sidebar.hover((function() {
      return $(this).animate({
        'margin-right': 0
      });
    }), (function() {
      return $(this).animate({
        'margin-right': -width + 30 + 'px'
      });
    }));
    return $('a img').hover((function() {
      return $(this).animate({
        'opacity': 1
      }, 'slow');
    }), (function() {
      return $(this).animate({
        'opacity': 0
      }, 'slow');
    }));
  });

}).call(this);
