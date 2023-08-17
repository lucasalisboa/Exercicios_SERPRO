module.exports = class Order{
    constructor(preco, quantidade){
        this.preco = preco;
        this.quantidade = quantidade;
        this.momento = new Date();
    }
    total(){
        console.log(this.momento)
        return this.preco * this.quantidade;
    }
}