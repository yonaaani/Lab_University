function addClient() {
	var surname = document.getElementById('surname').value;
	var firstname = document.getElementById('firstname').value;
	var address = document.getElementById('address').value;
	var phone = document.getElementById('phone').value;

	// Створення запиту до сервера з використанням XMLHttpRequest
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'add_client.php', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
			// Оновлення вмісту таблиці на сторінці index.html
			document.getElementById('clients').innerHTML = xhr.responseText;
		}
	}
	xhr.send('surname=' + surname + '&firstname=' + firstname + '&address=' + address + '&phone=' + phone);
}
