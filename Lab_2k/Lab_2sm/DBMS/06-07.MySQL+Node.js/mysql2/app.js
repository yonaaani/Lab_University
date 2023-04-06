const mysql = require("mysql2");
const express = require("express")
const hbs = require('hbs');
 
const app = express();
const urlencodedParser = express.urlencoded({extended: false});
 
const pool = mysql.createPool({
  connectionLimit: 5,
  host: "localhost",
  user: "root",
  database: "travelagency",
  password: "IvankaStashko04"
});
 
app.set("view engine", "hbs");


// получение списка пользователей
app.get("/", function(req, res){
    pool.query("SELECT * FROM clients", function(err, data) {
      if(err) return console.log(err);
      res.render("index.hbs", {
          clients: data
      });
    });
});
// возвращаем форму для добавления данных
app.get("/create", function(req, res){
    res.render("create.hbs");
});
// получаем отправленные данные и добавляем их в БД 
app.post("/create", urlencodedParser, function (req, res) {
         
    if(!req.body) return res.sendStatus(400);
    const surname = req.body.surname;
    const firstname = req.body.firstname;
    const address = req.body.address;
    const phone = req.body.phone;
    pool.query("INSERT INTO clients (surname, firstname, address, phone) VALUES (?,?,?,?)", [surname, firstname, address, phone], function(err, data) {
      if(err) return console.log(err);
      res.redirect("/");
    });
});
 
// получем id редактируемого пользователя, получаем его из бд и отправлям с формой редактирования
app.get("/edit/:id", function(req, res){
  const id = req.params.id;
  pool.query("SELECT * FROM clients WHERE id=?", [id], function(err, data) {
    if(err) return console.log(err);
     res.render("edit.hbs", {
        client: data[0]
    });
  });
});
// получаем отредактированные данные и отправляем их в БД
app.post("/edit", urlencodedParser, function (req, res) {
         
  if(!req.body) return res.sendStatus(400);
  const surname = req.body.surname;
  const firstname = req.body.firstname;
  const address = req.body.address;
  const phone = req.body.phone;
  const id = req.body.id;
   
  pool.query("UPDATE clients SET surname=?, name=?, address=?, phone=? WHERE id=?", [surname, firstname, address, phone, id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});
 
// получаем id удаляемого пользователя и удаляем его из бд
app.post("/delete/:id", function(req, res){
          
  const id = req.params.id;
  pool.query("DELETE FROM clients WHERE id=?", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// получение списка пользователей
app.get("/1", function(req, res){
  pool.query("SELECT * FROM routes", function(err, data) {
    if(err) return console.log(err);
    res.render("index1.hbs", {
       routes: data
    });
  });
});
// возвращаем форму для добавления данных
app.get("/create1", function(req, res){
  res.render("create1.hbs");
});
// получаем отправленные данные и добавляем их в БД 
app.post("/create1", urlencodedParser, function (req, res) {
       
  if(!req.body) return res.sendStatus(400);
  const clientid = req.body.clientid;
  const routedate = req.body.routedate;
  const count = req.body.count;
  const discount = req.body.discount;
  pool.query("INSERT INTO routes (clientid, routedate, count, discount) VALUES (?,?,?,?)", [clientid, routedate, count, discount], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/1");
  });
});

// получем id редактируемого пользователя, получаем его из бд и отправлям с формой редактирования
app.get("/edit1/:id", function(req, res){
const id = req.params.id;
pool.query("SELECT * FROM routes WHERE id=?", [id], function(err, data) {
  if(err) return console.log(err);
   res.render("edit1.hbs", {
      route: data[0]
  });
});
});
// получаем отредактированные данные и отправляем их в БД
app.post("/edit1", urlencodedParser, function (req, res) {
       
if(!req.body) return res.sendStatus(400);
const clientid = req.body.clientid;
const routedate = req.body.routedate;
const count = req.body.count;
const discount = req.body.discount;
const id = req.body.id;
 
pool.query("UPDATE routes SET clientid=?, routedate=?, count=?, discount=? WHERE id=?", [clientid, routedate, count, discount, id], function(err, data) {
  if(err) return console.log(err);
  res.redirect("/1");
});
});

// получаем id удаляемого пользователя и удаляем его из бд
app.post("/delete1/:id", function(req, res){
        
const id = req.params.id;
pool.query("DELETE FROM routes WHERE id=?", [id], function(err, data) {
  if(err) return console.log(err);
  res.redirect("/1");
});
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// получение списка пользователей
app.get("/2", function(req, res){
  pool.query("SELECT * FROM vouchers", function(err, data) {
    if(err) return console.log(err);
    res.render("index2.hbs", {
      vouchers: data
    });
  });
});
// возвращаем форму для добавления данных
app.get("/create2", function(req, res){
  res.render("create2.hbs");
});
// получаем отправленные данные и добавляем их в БД 
app.post("/create2", urlencodedParser, function (req, res) {
       
  if(!req.body) return res.sendStatus(400);
  const routesid = req.body.routesid;
  const country = req.body.country;
  const climate = req.body.climate;
  const duration = req.body.duration;
  const hotel = req.body.hotel;
  const price = req.body.price;
  pool.query("INSERT INTO vouchers (routesid, country, climate, duration, hotel, price) VALUES (?,?,?,?,?,?)", [routesid, country, climate, duration, hotel, price], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/2");
  });
});

// получем id редактируемого пользователя, получаем его из бд и отправлям с формой редактирования
app.get("/edit2/:id", function(req, res){
const id = req.params.id;
pool.query("SELECT * FROM vouchers WHERE id=?", [id], function(err, data) {
  if(err) return console.log(err);
   res.render("edit2.hbs", {
    voucher: data[0]
  });
});
});
// получаем отредактированные данные и отправляем их в БД
app.post("/edit2", urlencodedParser, function (req, res) {
       
if(!req.body) return res.sendStatus(400);
const routesid = req.body.routesid;
const country = req.body.country;
const climate = req.body.climate;
const duration = req.body.duration;
const hotel = req.body.hotel;
const price = req.body.price;
const id = req.body.id;
 
pool.query("UPDATE vouchers SET routesid=?, country=?, climate=?, duration=?, hotel=?, price=? WHERE id=?", [routesid, country, climate, duration, hotel, price, id], function(err, data) {
  if(err) return console.log(err);
  res.redirect("/2");
});
});

// получаем id удаляемого пользователя и удаляем его из бд
app.post("/delete2/:id", function(req, res){
        
const id = req.params.id;
pool.query("DELETE FROM vouchers WHERE id=?", [id], function(err, data) {
  if(err) return console.log(err);
  res.redirect("/2");
});
});

 
app.listen(3000, function(){
  console.log("Сервер ожидает подключения...");
});