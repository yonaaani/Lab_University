const express = require("express");
const bodyParser = require("body-parser");
const hbs = require('hbs');
const pg = require("pg");
 
const app = express();
const urlencodedParser = bodyParser.urlencoded({extended: false});
 
const pool = new pg.Pool({
  host: "localhost",
  user: "postgres",
  database: "travelagency",
  password: "ivanka04",
  port: 5432,
});
 
app.set("view engine", "hbs");


// отримання списку користувачів
app.get("/", function(req, res){
    pool.query("SELECT * FROM clients", function(err, data) {
      if(err) return console.log(err);
      res.render("index", {
          clients: data.rows
      });
    });
});
// повертаємо форму для додавання даних
app.get("/create", function(req, res){
    res.render("create.hbs");
});
// отримуємо одержані дані та надсилаємо в БД
app.post("/create", urlencodedParser, function (req, res) {
         
    if(!req.body) return res.sendStatus(400);
    const surname = req.body.surname;
    const firstname = req.body.firstname;
    const address = req.body.address;
    const phone = req.body.phone;
    pool.query("INSERT INTO clients (surname, firstname, address, phone) VALUES ($1,$2,$3,$4)", [surname, firstname, address, phone], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/");
    });
});
 
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
app.get("/edit/:id", function(req, res){
  const id = req.params.id;
  pool.query("SELECT * FROM clients WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit.hbs", {
        client: data.rows[0]
    });
  });
});
// отримуємо відредаговані дані і надсилаємо в БД
app.post("/edit", urlencodedParser, function (req, res) {
         
  if(!req.body) return res.sendStatus(400);
  const id = req.body.id;
  const surname = req.body.surname;
  const firstname = req.body.firstname;
  const address = req.body.address;
  const phone = req.body.phone;
  
   
  pool.query("UPDATE clients SET surname=$1, firstname=$2, address=$3, phone=$4 WHERE id=$5", [surname, firstname, address, phone, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});
 
// отримуємо id потрібного користувача і видаляємо з БД
app.post("/delete/:id", function(req, res){
          
  const id = req.params.id;
  pool.query("DELETE FROM clients WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// отримання списку користувачів
app.get("/1", function(req, res){
    pool.query("SELECT * FROM routes", function(err, data) {
      if(err) return console.log(err);
      res.render("index1.hbs", {
         routes: data.rows
      });
    });
  });
// повертаємо форму для додавання даних
  app.get("/create1", function(req, res){
    res.render("create1.hbs");
  });
// отримуємо одержані дані та надсилаємо в БД
  app.post("/create1", urlencodedParser, function (req, res) {
         
    if(!req.body) return res.sendStatus(400);
    const clientid = req.body.clientid;
    const routedate = req.body.routedate;
    const count = req.body.count;
    const discount = req.body.discount;
    pool.query("INSERT INTO routes (clientid, routedate, count, discount) VALUES ($1,$2,$3,$4)", [clientid, routedate, count, discount], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/1");
    });
  });
  
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
  app.get("/edit1/:id", function(req, res){
  const id = req.params.id;
  pool.query("SELECT * FROM routes WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit1.hbs", {
        route: data.rows[0]
    });
  });
  });
// отримуємо відредаговані дані і надсилаємо в БД
  app.post("/edit1", urlencodedParser, function (req, res) {
         
  if(!req.body) return res.sendStatus(400);
  const clientid = req.body.clientid;
  const routedate = req.body.routedate;
  const count = req.body.count;
  const discount = req.body.discount;
  const id = req.body.id;
   
  pool.query("UPDATE routes SET clientid=$1, routedate=$2, count=$3, discount=$4 WHERE id=$5", [clientid, routedate, count, discount, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/1");
  });
  });
  
// отримуємо id потрібного користувача і видаляємо з БД
  app.post("/delete1/:id", function(req, res){
          
  const id = req.params.id;
  pool.query("DELETE FROM routes WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/1");
  });
  });
  
  
  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
  
  // отримання списку користувачів
  app.get("/2", function(req, res){
    pool.query("SELECT * FROM vouchers", function(err, data) {
      if(err) return console.log(err);
      res.render("index2.hbs", {
        vouchers: data.rows
      });
    });
  });
 // повертаємо форму для додавання даних
  app.get("/create2", function(req, res){
    res.render("create2.hbs");
  });
// отримуємо одержані дані та надсилаємо в БД
  app.post("/create2", urlencodedParser, function (req, res) {
         
    if(!req.body) return res.sendStatus(400);
    const routesid = req.body.routesid;
    const country = req.body.country;
    const climate = req.body.climate;
    const duration = req.body.duration;
    const hotel = req.body.hotel;
    const price = req.body.price;
    pool.query("INSERT INTO vouchers (routesid, country, climate, duration, hotel, price) VALUES ($1,$2,$3,$4,$5,$6)", [routesid, country, climate, duration, hotel, price], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/2");
    });
  });
  
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
  app.get("/edit2/:id", function(req, res){
  const id = req.params.id;
  pool.query("SELECT * FROM vouchers WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit2.hbs", {
      voucher: data.rows[0]
    });
  });
  });
// отримуємо відредаговані дані і надсилаємо в БД
  app.post("/edit2", urlencodedParser, function (req, res) {
         
  if(!req.body) return res.sendStatus(400);
  const routesid = req.body.routesid;
  const country = req.body.country;
  const climate = req.body.climate;
  const duration = req.body.duration;
  const hotel = req.body.hotel;
  const price = req.body.price;
  const id = req.body.id;
   
  pool.query("UPDATE vouchers SET routesid=$1, country=$2, climate=$3, duration=$4, hotel=$5, price=$6 WHERE id=$7", [routesid, country, climate, duration, hotel, price, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/2");
  });
  });
  
// отримуємо id потрібного користувача і видаляємо з БД
  app.post("/delete2/:id", function(req, res){
          
  const id = req.params.id;
  pool.query("DELETE FROM vouchers WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/2");
  });
  });

/*Запит виконує оновлення поля "price" в таблиці "vouchers" відповідно до тривалості, 
яку отримано з даних запиту. У разі, якщо тривалість дорівнює 2 тижням, метод зменшує ціну на 5%. 
Якщо тривалість більше 2, метод зменшує ціну на 5% у степені, що дорівнює тривалості мінус 1. 
Якщо тривалість менше або дорівнює 1, ціна не змінюється. */
  app.post("/updatePrice2", urlencodedParser, function (req, res) {
    if (!req.body) return res.sendStatus(400);
    const duration = req.body.duration;
    pool.query(`
        UPDATE vouchers SET price = 
        CASE 
            WHEN duration = 2 THEN price * 0.95
            WHEN duration > 2 THEN price * POWER(0.95, duration - 1)
            ELSE price
        END
        WHERE duration = $1`, [duration], function (err, data) {
            if (err) return console.log(err);
            res.redirect("/2");
        });
});

  

 
app.listen(3000, function(){
  console.log("Сервер ожидает подключения...");
});