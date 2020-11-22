var PromiseFtp = require("promise-ftp");

let host = "ftp.datasus.gov.br";
let user = "";
let password = "";

var ftp = new PromiseFtp();
ftp
  .connect({ host: host, user: user, password: password })
  .then(function (serverMessage) {
    console.log("Server message: " + serverMessage);
    return ftp.list("/CIHA/downloads/CIHA01");
  })
  .then(function (list) {
    console.log("Directory listing:");
    console.dir(list);
    return ftp.end();
  });