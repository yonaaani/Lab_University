const express = require("express");
const bodyParser = require("body-parser");
const hbs = require('hbs');
const sqlite3 = require('sqlite3').verbose();
 
const app = express();
const urlencodedParser = bodyParser.urlencoded({extended: false});
 
const db = new sqlite3.Database('C:/sqlite/travelagency.db');
 
app.set("view engine", "hbs");


// отримання списку користувачів
app.get("/", function(req, res){
    db.all("SELECT * FROM clients", function(err, data) {
      if(err) return console.log(err);
      res.render("index", {
          clients: data
      });
    });
});

// повертаємо форму для додавання даних
app.get("/create", function(req, res){
    res.render("create");
});
// отримуємо одержані дані та надсилаємо в БД
app.post("/create", urlencodedParser, function (req, res) {
         
    if(!req.body) return res.sendStatus(400);
    const surname = req.body.surname;
    const firstname = req.body.firstname;
    const address = req.body.address;
    const phone = req.body.phone;
    db.all("INSERT INTO clients (surname, firstname, address, phone) VALUES ($1,$2,$3,$4)", [surname, firstname, address, phone], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/");
    });
});
 
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
app.get("/edit/:id", function(req, res){
  const id = req.params.id;
  db.all("SELECT * FROM clients WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit", {
        client: data[0]
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
  
   
  db.all("UPDATE clients SET surname=$1, firstname=$2, address=$3, phone=$4 WHERE id=$5", [surname, firstname, address, phone, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});
 
// отримуємо id потрібного користувача і видаляємо з БД
app.post("/delete/:id", function(req, res){
          
  const id = req.params.id;
  db.all("DELETE FROM clients WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// отримання списку користувачів
app.get("/1", function(req, res){
    db.all("SELECT * FROM routes", function(err, data) {
      if(err) return console.log(err);
      res.render("index1.hbs", {
         routes: data
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
    db.all("INSERT INTO routes (clientid, routedate, count, discount) VALUES ($1,$2,$3,$4)", [clientid, routedate, count, discount], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/1");
    });
  });
  
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
  app.get("/edit1/:id", function(req, res){
  const id = req.params.id;
  db.all("SELECT * FROM routes WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit1.hbs", {
        route: data[0]
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
   
  db.all("UPDATE routes SET clientid=$1, routedate=$2, count=$3, discount=$4 WHERE id=$5", [clientid, routedate, count, discount, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/1");
  });
  });
  
// отримуємо id потрібного користувача і видаляємо з БД
  app.post("/delete1/:id", function(req, res){
          
  const id = req.params.id;
  db.all("DELETE FROM routes WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/1");
  });
  });
  
  
  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
  
  // отримання списку користувачів
  app.get("/2", function(req, res){
    db.all("SELECT * FROM vouchers", function(err, data) {
      if(err) return console.log(err);
      res.render("index2.hbs", {
        vouchers: data
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
    db.all("INSERT INTO vouchers (routesid, country, climate, duration, hotel, price) VALUES ($1,$2,$3,$4,$5,$6)", [routesid, country, climate, duration, hotel, price], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/2");
    });
  });
  
// отримуємо id користувача => отримуємо його із БД => відправляємо з форми редагування
  app.get("/edit2/:id", function(req, res){
  const id = req.params.id;
  db.all("SELECT * FROM vouchers WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit2.hbs", {
      voucher: data[0]
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
   
  db.all("UPDATE vouchers SET routesid=$1, country=$2, climate=$3, duration=$4, hotel=$5, price=$6 WHERE id=$7", [routesid, country, climate, duration, hotel, price, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/2");
  });
  });
  
// отримуємо id потрібного користувача і видаляємо з БД
  app.post("/delete2/:id", function(req, res){
          
  const id = req.params.id;
  db.all("DELETE FROM vouchers WHERE id=$1", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/2");
  });
  });

 
 
app.listen(3000, function(){
  console.log("Сервер ожидает подключения...");
});