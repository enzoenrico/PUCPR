const express = require("express");
const app = express();
const port = 3000;

const mongoose = require("mongoose");
const uri =
  "mongodb+srv://admin:admin@clientescluster.mrixscb.mongodb.net/SmartCity?retryWrites=true&w=majority";

try {
  mongoose.connect(uri);
} catch (erroMongoose) {
  console.error(erroMongoose);
}

//Formatação de Datas para envio no servidor
let today = new Date();
let yyyy = today.getFullYear();
let mm = today.getMonth() + 1;
let dd = today.getDate();

if (dd < 10) dd = "0" + dd;
if (mm < 10) mm = "0" + mm;

const formattedToday = dd + "/" + mm + "/" + yyyy;

const insertSchema = mongoose.Schema({
  servoX: String,
  servoY: String,
  sendingDate: String,
});

const insertPattern = mongoose.model("ServoData", insertSchema);

app.use(express.json());

let data = [];

app.post("/api", (req, res) => {
  console.log('Request recebida')
  data.push(req.body);
  let sendData = new insertPattern({
    servoX: req.body.servoX,
    servoY: req.body.servoY,
    ldr: req.body.ldrData,
    sendingDate: formattedToday,
  });
  try {
    //enviar dados para o servidor 
    sendData.save().then(() => console.log("[!]OK"));
    res.status(200)
    console.log(sendData);
  } catch (erroServer) {
    res.status(500);
  }
});
app.get("/api", (req, res) => {
  console.log(`[+]Conexão de: ${req.ip}`);
  res.json(data);
});

app.listen(port, () => console.log(`gaming on port ${port}`));
