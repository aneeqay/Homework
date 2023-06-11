import org.junit.Before;
import org.junit.Test;

import java.util.HashMap;

import static org.junit.Assert.assertEquals;

public class ShoppingBasketTest {

    ShoppingBasket basket;
    Customer loyalCustomer;
    Customer fickleCustomer;
    Item tomato;
    Item potato;
    HashMap<Item, Integer> items;

    @Before
    public void setUp(){
        tomato = new Item("tomato", 0.6, false);
        potato = new Item("potato", 0.5, true);
        items = new HashMap<>();
        basket = new ShoppingBasket(items);
        basket.addItem(tomato, 1);
        loyalCustomer = new Customer(true);
        fickleCustomer = new Customer(false);
    }

    @Test
    public void canAddToBasket(){
        basket.addItem(tomato,2);
        int actual = basket.getItems().get(tomato);
        assertEquals(3, actual);
    }

    @Test
    public void canRemoveFromBasket(){
        basket.addItem(tomato, 1);
        basket.removeItem(tomato, 1);
        int actual = basket.getItems().get(tomato);
        assertEquals(1, actual);
        System.out.println(basket.getTotal());
        assertEquals(0.6, basket.getTotal(), 0.0);
    }

    @Test
    public void canEmptyBasket(){
        basket.emptyBasket();
        assertEquals(0, basket.getTotal(), 0.0);
        System.out.println(basket.getItems().keySet());
    }

    @Test
    public void canGetTotal(){
        assertEquals(0.6, basket.getTotal(), 0.0);
    }

    @Test
    public void canGiveOver20Discount(){
        basket.setTotal(21);
        basket.applyDiscounts(fickleCustomer);
        assertEquals((21*0.9), basket.getTotal(), 0.0);
    }

    @Test
    public void cannotGiveOver20Discount(){
        basket.applyDiscounts(fickleCustomer);
        assertEquals(0.6, basket.getTotal(), 0.0);
    }

    @Test
    public void canGiveLoyaltyDiscount(){
        basket.applyDiscounts(loyalCustomer);
        assertEquals((0.6*0.98), basket.getTotal(), 0.0);
    }

    @Test
    public void cannotGiveLoyaltyDiscount(){
        basket.applyDiscounts(fickleCustomer);
        assertEquals(0.6, basket.getTotal(), 0.0);
    }

    @Test
    public void canStackDiscounts(){
        basket.setTotal(30);
        basket.applyDiscounts(loyalCustomer);
        assertEquals((30*0.9*0.98), basket.getTotal(), 0.0);
    }

    @Test
    public void canApplyBogof(){
        basket.addItem(potato, 3);
        assertEquals(1.6, basket.getTotal(), 0.0);
    }

}
