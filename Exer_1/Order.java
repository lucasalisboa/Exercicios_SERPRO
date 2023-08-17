import java.util.ArrayList;
import java.util.Date;

public class Order {
    private Date moment;
    private OrderStatus status;
    private ArrayList <OrderItem> itens;
    
    public Order(OrderStatus status){
        moment = new Date();
        this.status = status;
        this.itens = new ArrayList<OrderItem>();
    }

    public void addItem(OrderItem item){
        itens.add(0, item);
    }

    public void removeItem(OrderItem item){
        itens.remove(item);
    }

    public Double Total(){
        Double total = 0.0;
        System.out.println("Data:"+moment);
        System.out.println("Status:"+status);
        System.out.println("----");
        for (OrderItem orderItem : itens) {
            total += orderItem.subTotal();
            System.out.println("----");
        }
        return total;
    }
}
