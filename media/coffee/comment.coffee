$ ->
  $('.leaveComment').css 'display':'none'

  $('.leaveCommentButton').bind('click', ->
    $(this)
      .next('.leaveComment')
      .slideToggle()
  )
