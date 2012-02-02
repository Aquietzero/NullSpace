$ ->
  sidebar = $('#sidebar')
  width = sidebar.width()

  sidebar.css
    'margin-right' : -width + 30 + 'px'

  sidebar.hover (-> $(this).animate
      'margin-right' : 0
    ), (-> $(this).animate
      'margin-right' : -width + 30 + 'px'
    )
