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

module.exports = router;