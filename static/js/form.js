//Vincular enter con el boton siguiente
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();  // Evitar el comportamiento por defecto
      document.querySelector('input[value="Siguiente"]').click();  // Simular clic en "Siguiente"
    }
  });

    // Desactivar la validación del campo cuando se hace clic en "Volver"
    document.getElementById('volver').addEventListener('click', function() {
      document.getElementById('form').noValidate = true;
    });