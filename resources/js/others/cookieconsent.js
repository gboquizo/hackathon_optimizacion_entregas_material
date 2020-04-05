window.addEventListener('load', () => {
  window.cookieconsent.initialise({
    palette: {
      popup: {
        background: '#000000',
        text: '#ffffff'
      },
      button: {
        background: '#472268',
        text: '#ffffff'
      }
    },
    theme: 'classic',
    content: {
      message: 'Utilizamos cookies para analizar y optimizar la navegación en nuestro sitio web. ' +
            'Si sigue navegando, consideramos que acepta su uso y nuestra política de cookies.',
      dismiss: 'CERRAR',
      link: '',
      href: ''
    }
  })
})
