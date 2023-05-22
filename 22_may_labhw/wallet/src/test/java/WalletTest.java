import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class WalletTest {

    private Wallet wallet;
    private ArrayList<IChargeable> cards;
    private ArrayList<Double> transactions;
    private CreditCard amex;
    private DebitCard hsbc;
    private GiftCard next;

    @Before
    public void before(){
        transactions = new ArrayList<>();
        next = new GiftCard(50);
        hsbc = new DebitCard(1100, 425, 200, transactions, 1001, 1675);
        amex = new CreditCard(2345, 565, 677, transactions, 1000);
        cards = new ArrayList<>();
        wallet = new Wallet(cards);
        wallet.addCard(next);
        wallet.addCard(hsbc);
        wallet.addCard(amex);
    }

    @Test
    public void canSelectCard(){
        assertEquals(next, wallet.getCard(0));
    }

    @Test
    public void canPay(){
        wallet.pay(0, 10);
        wallet.pay(1, 10);
        wallet.pay(2, 10);
        assertEquals(40, next.getBalance(), 0.0);
        assertEquals(10, hsbc.getTransaction(0), 0.0);
        assertEquals((1000 - (1.05*10)), amex.getCredit(), 0.0);

    }
}
