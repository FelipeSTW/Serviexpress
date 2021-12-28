// DOM elements
const buttonAdd = document.querySelector('.button-add')

// Main
buttonAdd.addEventListener('click', (e) => {
	e.preventDefault()
	createEmployee()
})

const getFormData = () => {
	const nameInput = document.querySelector('.name-input').value
	const lastnameInput = document.querySelector('.lastname-input').value
	const rutInput = document.querySelector('.rut-input').value
	const username = nameInput[0] + lastnameInput
	const email = username + '@serviexpress.cl'

	return {
		'name': nameInput,
		'last-name': lastnameInput,
		'rut': rutInput,
		'username': username,
		'email': email
	}
}

const createEmployee = async () => {
	await fetch('', {
		method: 'POST',
		body: JSON.stringify(getFormData()),
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,	
		}
	})
	.then(response => response.json())
	.then(() => {
		document.querySelector('.name-input').value = ''
		document.querySelector('.lastname-input').value = ''
		document.querySelector('.rut-input').value = ''		
	})
	.then(() => {
		location.reload()
	})
}

const editEmployee = async (employeeId) => {
	console.log(employeeId)
	await fetch('', {
		method: 'PUT',
		body: JSON.stringify({'id': employeeId}),
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,	
		}
	})
	.then(response => response.json())
	.then(data => {
		document.querySelector('.name-input').value = data['name']
		document.querySelector('.lastname-input').value = data['last-name']
		document.querySelector('.rut-input').value = data['rut']
	})
}

const deleteEmployee = async (employeeId) => {
	await fetch('', {
		method: 'DELETE',
		body: JSON.stringify({'id': employeeId}),
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,	
		}
	})
	.then(response => response.json())
	.then(() => {
		location.reload()
	})
}

// // Utils

// const clearField = (element) => {
// 	element.value = ''
// }

// const setField = (element, value) => {
// 	element.value = value
// }

// // Main
// buttonAdd.addEventListener('click', (e) => {
// 	e.preventDefault()
// 	console.log('FUNCIONA')
// })

// const createEmployee = () => {
// 	fetch('', {
// 		method: 'POST',
// 		body: JSON.stringify(employeeData),
// 		headers: {
// 			'Content-Type': 'application/json',
// 			'X-CSRFToken': csrftoken
// 		}
// 	})
// 	.then(response => response.json())
// 	.then(data => alert(data.status))
// 	// clearField(nameInput)
// 	// clearField(lastNameInput)
// 	// clearField(rutInput)
// }

// let employeeData = {
// 	'name': document.querySelector('.input-name').value,
// 	'last-name': document.querySelector('.input-lastname').value,
// 	'email': document.querySelector('.input-name').value[0] + document.querySelector('.input-lastname').value + '@serviexpress.cl',
// 	'rut': document.querySelector('.input-rut').value,
// }

// // Edit
// // buttonEdit.addEventListener('click', (e) => {
// // 	e.preventDefault()
// // 	console.log(e.target.id)
// // 	editEmployee()
// // })

// const editEmployee = (id) => {
// 	fetch('', {
// 		method: 'EDIT',
// 		body: JSON.stringify({
// 			'id': id
// 		}),
// 		headers: {
// 			'Content-Type': 'application/json',
// 			'X-CSRFToken': csrftoken
// 		}
// 	})
// 	.then(response => response.json())
// 	.then(data => console.log(data))
// 	setField(nameInput, 'NAME')
// 	setField(lastNameInput, 'LASTNAME')
// 	setField(rutInput, 'RUT')
// }