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
app.get("/routes", function(req, res){
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
      res.redirect("/routes");
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
    res.redirect("/routes");
  });
  });
  
  // получаем id удаляемого пользователя и удаляем его из бд
  app.post("/delete1/:id", function(req, res){
          
  const id = req.params.id;
  pool.query("DELETE FROM routes WHERE id=?", [id], function(err, data) {
    if(err) return console.log(err);
    res.redirect("/");
  });
  });

  module.exports = router;