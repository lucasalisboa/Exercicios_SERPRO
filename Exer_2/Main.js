let Order = require('./Order.js');

novo_pedido = new Order(2.5,4);
conta = novo_pedido.total();
console.log(conta)