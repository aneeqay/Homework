import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class GiftCardTest {

    private GiftCard asos;

    @Before
    public void before(){
        asos = new GiftCard(100);
    }

    @Test
    public void canMakePurchase(){
        asos.charge(10);
        assertEquals(90, asos.getBalance());
    }

}
