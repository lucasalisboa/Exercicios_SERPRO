public class OrderItem {
    private Integer quantity;
    private Double price;

    public OrderItem(Integer quantity, Double price){
        this.quantity = quantity;
        this.price = price;
    }

    public Double subTotal(){
        System.out.println("Qtd:"+quantity);
        System.out.println("preco:"+price);
        return quantity * price;
    }
}
