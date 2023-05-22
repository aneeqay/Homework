import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class CreditCardTest {

    private CreditCard amexcc;
    private ArrayList<Double> transactions;

    @Before
    public void setUp(){
        transactions = new ArrayList<>();
        amexcc = new CreditCard(1000, 1020, 633, transactions, 10000);
    }

    @Test
    public void canGetCredit(){
        assertEquals(10000, amexcc.getCredit(), 0.0);
    }

    @Test
    public void canMakePurchase(){
        amexcc.charge(1000);
        assertEquals(8950, amexcc.getCredit(), 0.0);
    }

}
