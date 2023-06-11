import java.util.HashMap;

public class ShoppingBasket {

    private HashMap<Item, Integer> items;
    private double total;

    public ShoppingBasket(HashMap<Item, Integer> items) {
        this.items = items;
        this.total = 0;
    }

    public HashMap<Item, Integer> getItems() {
        return this.items;
    }

    public void setItems(HashMap<Item, Integer> items) {
        this.items = items;
    }

    public double getTotal() {
        return this.total;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public void addItem(Item item, int quantity){
        this.items.put(item, items.getOrDefault(item, 0) + quantity);
        this.applyBogof(item, quantity);
    }

    public void applyBogof(Item item, int quantity){
        if (item.isBogof()) {
            int currentQuantity = this.items.get(item);
            int applicableForBogof = currentQuantity / 2;
            int notApplicableForBogof = currentQuantity % 2;
            this.total += (item.getPrice() * applicableForBogof);
            this.total += (item.getPrice() * notApplicableForBogof);
        } else {
         this.total += (item.getPrice() * quantity);}
    }

    public void removeItem(Item item, int quantity) {
        int currentQuantity = items.get(item);
        if (currentQuantity <= quantity) {
            items.remove(item);
        } else {
            items.put(item, currentQuantity - quantity);
        }
        if (item.isBogof()) {
            int applicableForBogof = quantity / 2;
            int notApplicableForBogof = quantity % 2;
            this.total -= (item.getPrice() * applicableForBogof);
            this.total -= (item.getPrice() * notApplicableForBogof);
        } else {
            this.total -= (item.getPrice() * quantity);
        }
    }

    public void emptyBasket(){
        this.items.clear();
        setTotal(0);
    }

    public void applyLoyaltyDiscount(Customer customer){
        if (customer.isLoyaltyCard()){
        double discount = this.total * 0.02;
        this.total -= discount;}
    }

    public void applyOver20Discount(){
        if (this.total > 20){
            this.total = this.total * 0.9;
        }
    }

    public void applyDiscounts(Customer customer){
        this.applyLoyaltyDiscount(customer);
        this.applyOver20Discount();
    }
}
