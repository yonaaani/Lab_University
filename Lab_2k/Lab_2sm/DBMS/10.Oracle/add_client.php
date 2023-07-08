<?php
	// Підключення до бази даних
	$conn = oci_connect('SYS', 'ivanka04', 'localhost/1521');

	// Вставка нового запису у таблицю "Клієнти"
	$sql = "INSERT INTO clients (id, surname, firstname, address, phone) VALUES (:id, :surname, :firstname, :address, :phone)";
	$stmt = oci_parse($conn, $sql);
	$id = time();
	$surname = $_POST['surname'];
	$firstname = $_POST['firstname'];
	$address = $_POST['address'];
	$phone = $_POST['phone'];
	oci_bind_by_name($stmt, ':id', $id);
	oci_bind_by_name($stmt, ':surname', $surname);
	oci_bind_by_name($stmt, ':firstname', $firstname);
	oci_bind_by_name($stmt, ':address', $address);
	oci_bind_by_name($stmt, ':phone', $phone);
	oci_execute($stmt);

	// Вибірка всіх записів з таблиці "Клієнти"
	$sql = "SELECT * FROM clients";
	$stmt = oci_parse($conn, $sql);
	oci_execute($stmt);

	// Відображення результатів запиту у вигляді HTML-таблиці
	echo "<table border='1'>";
	echo "<tr><th>ID</th><th>Прізвище</th><th>Ім'я</th><th>Адреса</th><th>Телефон</th></tr>";
	while ($row = oci_fetch_array($stmt, OCI_ASSOC)) {
		echo "<tr>";
		echo "<td>".$row['ID']."</td>";
		echo "<td>".$row['SURNAME']."</td>";
		echo "<td>".$row['FIRSTNAME']."</td>";
		echo "<td>".$row['ADDRESS']."</td>";
		echo "<td>".$row['PHONE']."</td>";
		echo "</tr>";
	}
	echo "</table>";

	// Закриття з'єднання з базою даних
	oci_close($conn);
?>
