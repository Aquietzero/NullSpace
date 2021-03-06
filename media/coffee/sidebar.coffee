$ ->
  sidebar = $('#sidebar')
  width = sidebar.width()

  sidebar.css
    'margin-right' : -width + 30 + 'px'

  
  #sidebar.hover (-> $(this).animate
  #    'margin-right' : 0
  #  ), (-> $(this).animate
  #    'margin-right' : -width + 30 + 'px'
  #  )

  $('#fixedbar a img').hover (-> $(this).animate
      'opacity' : 1, 'slow'
    ), (-> $(this).animate
      'opacity' : 0, 'slow'
    )

  hide = true
  toggleHide = ->
    if hide
      hide = false
      sidebar.animate
        'margin-right' : 0
    else
      hide = true
      sidebar.animate
        'margin-right' : -width + 30 + 'px'

  sidebarButton = $('#sidebarButton')
  sidebarButton.bind('click', toggleHide)
