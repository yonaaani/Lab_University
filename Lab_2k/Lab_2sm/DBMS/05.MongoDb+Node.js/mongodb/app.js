const express = require("express");
const MongoClient = require("mongodb").MongoClient;
const objectId = require("mongodb").ObjectId;
     
const app = express();
const jsonParser = express.json();
   
const mongoClient = new MongoClient("mongodb://127.0.0.1:27017/");
  
app.use(express.static(`${__dirname}/public`));
  
(async () => {
     try {
        await mongoClient.connect();
        app.locals.collection = mongoClient.db("travelagency").collection("clients");
        app.locals.collection1 = mongoClient.db("travelagency").collection("routes");
        app.locals.collection2 = mongoClient.db("travelagency").collection("vouchers");
        app.listen(3000);
        console.log("Сервер чекає підключення...");
    }catch(err) {
        return console.log(err);
    } 
})();
  
//Клієнти
app.get("/api/clients", async(req, res) => {
          
    const collection = req.app.locals.collection;
    try{
        const clients = await collection.find({}).toArray();
        res.send(clients);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }  
});
app.get("/api/clients/:id", async(req, res) => {
          
    const collection = req.app.locals.collection;
    try{
        const id = new objectId(req.params.id);
        const client = await collection.findOne({_id: id});
        if(client) res.send(client);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.post("/api/clients", jsonParser, async(req, res)=> {
         
    if(!req.body) return res.sendStatus(400);
         
    const clientSurname = req.body.surname;
    const clientName = req.body.name;
    const clientAddress = req.body.address;
    const clientPhone = req.body.phone;
    const client = {surname: clientSurname, name: clientName, address: clientAddress, phone: clientPhone};
         
    const collection = req.app.locals.collection;
      
    try{
        await collection.insertOne(client);
        res.send(client);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
      
app.delete("/api/clients/:id", async(req, res)=>{
          
    const collection = req.app.locals.collection;
    try{
        const id = new objectId(req.params.id);
        const result = await collection.findOneAndDelete({_id: id});
        const client = result.value;
        if(client) res.send(client);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.put("/api/clients", jsonParser, async(req, res)=>{
          
    if(!req.body) return res.sendStatus(400);
    const clientSurname = req.body.surname;
    const clientName = req.body.name;
    const clientAddress = req.body.address;
    const clientPhone = req.body.phone;
         
    const collection = req.app.locals.collection;
    try{
        const id = new objectId(req.body.id);
        const result = await collection.findOneAndUpdate({_id: id}, { $set: {surname: clientSurname, name: clientName, address: clientAddress, phone: clientPhone}},
         {returnDocument: "after" });
 
        const client = result.value;
        if(client) res.send(client);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});



///////////////////////////////////////////////////////////////////////////////////////////


//Маршрути
app.get("/api/routes", async(req, res) => {
          
    const collection1 = req.app.locals.collection1;
    try{
        const routes = await collection1.find({}).toArray();
        res.send(routes);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }  
});
app.get("/api/routes/:id", async(req, res) => {
          
    const collection1 = req.app.locals.collection1;
    try{
        const id = new objectId(req.params.id);
        const route = await collection1.findOne({_id: id});
        if(route) res.send(route);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.post("/api/routes", jsonParser, async(req, res)=> {
         
    if(!req.body) return res.sendStatus(400);
         
    const clientId = req.body.client_id;
    const routeDate = req.body.date;
    const routeCount = req.body.count;
    const routeDiscount = req.body.discount;
    const route = {client_id: clientId, date: routeDate, count: routeCount, discount: routeDiscount};
         
    const collection1 = req.app.locals.collection1;
      
    try{
        await collection1.insertOne(route);
        res.send(route);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
      
app.delete("/api/routes/:id", async(req, res)=>{
          
    const collection1 = req.app.locals.collection1;
    try{
        const id = new objectId(req.params.id);
        const result = await collection1.findOneAndDelete({_id: id});
        const route = result.value;
        if(route) res.send(route);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.put("/api/routes", jsonParser, async(req, res)=>{
          
    if(!req.body) return res.sendStatus(400);
    const clientId = req.body.client_id;
    const routeDate = req.body.date;
    const routeCount = req.body.count;
    const routeDiscount = req.body.discount;
         
    const collection1 = req.app.locals.collection1;
    try{
        const id = new objectId(req.body.id);
        const result = await collection1.findOneAndUpdate({_id: id}, { $set: {client_id: clientId, date: routeDate, count: routeCount, discount: routeDiscount}},
         {returnDocument: "after" });
 
        const route = result.value;
        if(route) res.send(route);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});


/////////////////////////////////////////////////////////////////////////////////////////


//Путівки
app.get("/api/vouchers", async(req, res) => {
          
    const collection2 = req.app.locals.collection2;
    try{
        const vouchers = await collection2.find({}).toArray();
        res.send(vouchers);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }  
});
app.get("/api/vouchers/:id", async(req, res) => {
          
    const collection2 = req.app.locals.collection2;
    try{
        const id = new objectId(req.params.id);
        const voucher = await collection2.findOne({_id: id});
        if(voucher) res.send(voucher);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.post("/api/vouchers", jsonParser, async(req, res)=> {
         
    if(!req.body) return res.sendStatus(400);
         
    const routerId = req.body.routers_id;
    const voucherCountry = req.body.country;
    const voucherClimate = req.body.climate;
    const voucherDuration = req.body.duration;
    const voucherHotel = req.body.hotel;
    const voucherPrice = req.body.price;
    const voucher = {routers_id: routerId, country: voucherCountry, climate: voucherClimate, duration: voucherDuration, hotel: voucherHotel, price: voucherPrice};
         
    const collection2 = req.app.locals.collection2;
      
    try{
        await collection2.insertOne(voucher);
        res.send(voucher);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
      
app.delete("/api/vouchers/:id", async(req, res)=>{
          
    const collection2 = req.app.locals.collection2;
    try{
        const id = new objectId(req.params.id);
        const result = await collection2.findOneAndDelete({_id: id});
        const voucher = result.value;
        if(voucher) res.send(voucher);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});
     
app.put("/api/vouchers", jsonParser, async(req, res)=>{
          
    if(!req.body) return res.sendStatus(400);
    const routerId = req.body.routers_id;
    const voucherCountry = req.body.country;
    const voucherClimate = req.body.climate;
    const voucherDuration = req.body.duration;
    const voucherHotel = req.body.hotel;
    const voucherPrice = req.body.price;
         
    const collection2 = req.app.locals.collection2;
    try{
        const id = new objectId(req.body.id);
        const result = await collection2.findOneAndUpdate({_id: id}, { $set: {routers_id: routerId, country: voucherCountry, climate: voucherClimate, duration: voucherDuration, hotel: voucherHotel, price: voucherPrice}},
         {returnDocument: "after" });
 
        const voucher = result.value;
        if(voucher) res.send(voucher);
        else res.sendStatus(404);
    }
    catch(err){
        console.log(err);
        res.sendStatus(500);
    }
});


   
// прослушиваем прерывание работы программы (ctrl-c)
process.on("SIGINT", async() => {
      
    await mongoClient.close();
    console.log("Приложение завершило работу");
    process.exit();
});