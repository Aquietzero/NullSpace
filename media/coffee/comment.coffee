$ ->
  $('.leaveCommentButton').bind('click', ->
    $(this)
      .next('.leaveComment')
      .slideToggle()
  )
