<meta http-equiv="Content-Type" content="text/html; charset=utf8">
<?php

// Змінні з форми

$srname = $_POST['Surname'];
$name = $_POST['Name'];
$mlname = $_POST['MiddleName'];
$ads = $_POST['Adress'];
$phone= $_POST['Phone'];

$country= $_POST['Country'];
$climate= $_POST['Climate'];
$duti= $_POST['Duration'];
$hotel= $_POST['Hotel'];
$price= $_POST['Price'];

$date= $_POST['Dateofshipment'];
$qaty= $_POST['Quantity'];
$discnt= $_POST['Discount'];


// Параметри для підключення
$db_host = "sql304.epizy.com"; // в open server саме
$db_user = "epiz_33572027"; // Логін БД
$db_password = "cH7nsDJ9pQ"; // Пароль БД
$db_base = 'epiz_33572027_lab1sskbd'; // Назва БД
$db_table1 = "Client"; // Назва таблиці БД
$db_table2 = "Routes";
$db_table3 = "Vouchers";

// Підключення до бази даних
$mysqli = new mysqli($db_host,$db_user,$db_password,$db_base);

// Якщо є помилка підключення, виводимо її і ліквідуємо підключення
if ($mysqli->connect_error) {
    die('Помилка: ('. $mysqli->connect_errno .') '. $mysqli->connect_error);
}

// Виконуємо запит для першої таблиці
$resultt = $mysqli->query("INSERT INTO ".$db_table1." (Surname,Name,MiddleName,Adress,Phone) VALUES ('$srname','$name','$mlname','$ads','$phone')");
$resultt1 = $mysqli->query("INSERT INTO ".$db_table2." (Country,Climate,Duration,Hotel,Price) VALUES ('$country','$climate','$duti','$hotel','$price')");
$resultt2 = $mysqli->query("INSERT INTO ".$db_table3." (Dateofshipment,Quantity,Discount) VALUES ('$date','$qaty','$discnt')");

// Перевіряємо виконання запиту та виводимо відповідне повідомлення
    if ($resultt == true || $resultt1 == true || resultt2 == true){
    	echo '<center>Інформація занесена в базу даних!</br><a href="index.html">Повернутись на головну</a></center>';
    
		
 		  $sql_select = "SELECT * FROM Client";
          $result2 = mysqli_query($mysqli, $sql_select);
          $row = mysqli_fetch_array($result2);
		do
		{
			printf("<p>Прізвище: " .$row['Surname'] . "</p> 
			        <p>Ім'я: " .$row['Name'] . "</p>
					<p>По батькові: " .$row['MiddleName'] . "</p>
					<p>Адреса: " .$row['Adress'] . "</p>
					<p>Телефон: " .$row['Phone'] . "</p></br>"
			);
		}
		while($row = mysqli_fetch_array($result2));
	
		$sql_select1 = "SELECT * FROM Routes";
          $result22 = mysqli_query($mysqli, $sql_select1);
          $row = mysqli_fetch_array($result22);
		do
		{
			printf("<p>Країна: " .$row['Country'] . "</p> 
			        <p>Клімат: " .$row['Climate'] . "</p>
					<p>Тривалість: " .$row['Duration'] . "</p>
					<p>Готель: " .$row['Hotel'] . "</p>
					<p>Вартсіть: " .$row['Price'] . "</p></br>"
			);
		}
		while($row = mysqli_fetch_array($result22));

		$sql_select2 = "SELECT * FROM Vouchers";
          $result222 = mysqli_query($mysqli, $sql_select2);
          $row = mysqli_fetch_array($result222);
		do
		{
			printf("<p>Дата відправлення: " .$row['Dateofshipment'] . "</p> 
			        <p>Кількість: " .$row['Quantity'] . "</p>
					<p>Знижка: " .$row['Discount'] . "</p></br>"
			);
		}
		while($row = mysqli_fetch_array($result222));

	
	}else{
    	echo 'Інформація не занесена в базу даних';
    }
	mysqli_close($mysqli);
?>
