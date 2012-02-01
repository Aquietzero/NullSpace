$ ->
  sidebar = $('#sidebar')
  width = sidebar.width()

  sidebar.css
    'margin-left' : -width + 30 + 'px'

  sidebar.hover
    -> sidebar.animate
      'margin-left' : 0
    ,
    -> sidebar.animate
      'margin-left' : -width + 30 + 'px'
