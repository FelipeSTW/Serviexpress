// DOM elemnts
const buttonReservation = document.getElementById('buttonReservation');

// Main
buttonReservation.addEventListener('click', (e) => {
  e.preventDefault()
  if(document.getElementById('fecha').value == '' || document.getElementById('hora').value == '' || document.getElementById('servicio').value == '' || document.getElementById('telefono').value == '' || document.getElementById('nombre').value == ''){
    console.log(getData())
    document.querySelector('#message').innerHTML = 'Debes completar todos los campos!'
    document.querySelector('.alert').classList.add('show')
  } else {
    makeReservation()
  }

})

const getData = () => {
  const dateInput = document.getElementById('fecha').value;
  const timeInput = document.getElementById('hora').value;
  const nameInput = document.getElementById('nombre').value;
  const phoneInput = document.getElementById('telefono').value;
  const serviceInput = document.getElementById('servicio').value; 

  return {
    'date': dateInput,
    'time': timeInput,
    'name': nameInput,
    'phone': phoneInput,
    'service': serviceInput
  }
}

const makeReservation = async () => {
  await fetch('', {
    method: 'POST',
    body: JSON.stringify(getData()),
    headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,	      
    }
  })
  .then(response => response.json())
  .then(data => {
    $('.alert').alert()
    document.querySelector('#message').innerHTML = data.msg
    document.querySelector('.alert').classList.add('show')
  })
}

const closeNotification = () => {
  document.querySelector('.alert').classList.remove('show')
}

