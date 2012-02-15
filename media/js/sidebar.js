(function() {

  $(function() {
    var hide, sidebar, sidebarButton, toggleHide, width;
    sidebar = $('#sidebar');
    width = sidebar.width();
    sidebar.css({
      'margin-right': -width + 30 + 'px'
    });
    $('#fixedbar a img').hover((function() {
      return $(this).animate({
        'opacity': 1
      }, 'slow');
    }), (function() {
      return $(this).animate({
        'opacity': 0
      }, 'slow');
    }));
    hide = true;
    toggleHide = function() {
      if (hide) {
        hide = false;
        return sidebar.animate({
          'margin-right': 0
        });
      } else {
        hide = true;
        return sidebar.animate({
          'margin-right': -width + 30 + 'px'
        });
      }
    };
    sidebarButton = $('#sidebarButton');
    return sidebarButton.bind('click', toggleHide);
  });

}).call(this);
