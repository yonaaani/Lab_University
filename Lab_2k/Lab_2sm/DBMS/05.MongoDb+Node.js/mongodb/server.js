const express = require('express');
const { connectToDb, getDb } = require('./db');


const PORT = 3000;

const app = express();
const jsonParser = express.json();


let db;

connectToDb((err) => {
    if(!err) {
        app.listen(PORT,(err)=> {
            err ? console.log(err) : console.log(`Listening port ${PORT}`);
        });
        db = getDb();
    } else {
        console.log(`DB connection error: ${err}`);
    }
});

app.use(express.static(`${__dirname}/public`));
  
/*(async () => {
     try {
        await mongoClient.connect();
        app.locals.collection = mongoClient.db("travelagency").collection("clients");
        app.listen(3000);
        console.log("Сервер ожидает подключения...");
    }catch(err) {
        return console.log(err);
    } 
})();*/

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
         
    const clientSurName = req.body.surname;
    const clientName = req.body.name;
    const clientAddress = req.body.address;
    const clientPhone = req.body.phone;
    const client = {surname: clientSurName, name: clientName, address: clientAddress, phone: clientPhone};
         
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
    const clientSurName = req.body.surname;
    const clientName = req.body.name;
    const clientAddress = req.body.address;
    const clientPhone = req.body.phone;
         
    const collection = req.app.locals.collection;
    try{
        const id = new objectId(req.body.id);
        const result = await collection.findOneAndUpdate({_id: id}, { $set: {surname: clientSurName, name: clientName, address: clientAddress, phone: clientPhone}},
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
   
// прослушиваем прерывание работы программы (ctrl-c)
process.on("SIGINT", async() => {
      
    await mongoClient.close();
    console.log("Приложение завершило работу");
    process.exit();
});
