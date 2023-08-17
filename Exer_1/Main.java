import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Order ordem = new Order(OrderStatus.DELIVERED);
        Scanner sc = new Scanner(System.in);
        int pedidos = sc.nextInt();
        for(int i = 1; i <= pedidos; i++ ){
            int q = sc.nextInt();
            Double p = sc.nextDouble();
            OrderItem novo_item = new OrderItem(q, p);
            ordem.addItem(novo_item);
        }
        double total = ordem.Total();
        System.out.println("TOTAL:"+total);
}
}