$ ->
  months = $('.archieve .month')
  for month in months
    $(month)
      .bind('click', ->
        $(this)
          .find('.postTitles')
          .slideToggle()
      )
