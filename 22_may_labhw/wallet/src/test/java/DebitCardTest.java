import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class DebitCardTest {

    private DebitCard boscard;
    private ArrayList<Double> transactions;

    @Before
    public void before(){
        transactions = new ArrayList<>();
        boscard = new DebitCard(200, 1022, 455, transactions, 7545, 102090);
    }

    @Test
    public void canMakePurchase(){
        boscard.charge(1000);
        assertEquals(1, boscard.getTransactions().size());
    }

}
