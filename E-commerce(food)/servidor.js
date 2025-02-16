const http = require('http');
const servidor = http.createServer((request, response) => {
  console.log("Servidor acessado!");
});
servidor.listen(3000);