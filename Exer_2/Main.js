const prompt = require("prompt-sync")({ sigint: true });
let Order = require('./Order.js');

var preco = prompt("Digite o preco");
var quantidade = prompt("Digite o quantidade");  

novo_pedido = new Order(preco,quantidade);
conta = novo_pedido.total();
console.log(conta)