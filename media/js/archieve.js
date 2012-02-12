(function() {

  $(function() {
    var month, months, _i, _len, _results;
    months = $('.archieve .month');
    _results = [];
    for (_i = 0, _len = months.length; _i < _len; _i++) {
      month = months[_i];
      _results.push($(month).bind('click', function() {
        return $(this).find('.postTitles').slideToggle();
      }));
    }
    return _results;
  });

}).call(this);
