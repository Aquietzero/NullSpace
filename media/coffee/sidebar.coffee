$ ->
  sidebar = $('#sidebar')
  width = sidebar.width()

  sidebar.css
    'margin-left' : -width + 35 + 'px'

  sidebar.hover (-> $(this).animate
      'margin-left':0
    ), (-> $(this).animate
      'margin-left':-width + 30 + 'px'
    )
