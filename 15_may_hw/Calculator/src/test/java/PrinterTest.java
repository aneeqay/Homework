import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrinterTest {

    Printer testPrinter;

    @Before
    public void before() {
        testPrinter = new Printer(500, 1000);
    }

    @Test
    public void hasPaper(){
        assertEquals(500, testPrinter.getPaperInPrinter());
    }

    @Test
    public void hasToner(){
        assertEquals(1000, testPrinter.getToner());
    }

    @Test
    public void canPrint(){
        testPrinter.print(50, 2);
        assertEquals(400, testPrinter.getPaperInPrinter());
        assertEquals(900, testPrinter.getToner());
    }

    @Test
    public void cannotPrint(){
        testPrinter.print(500, 10);
        assertEquals(500, testPrinter.getPaperInPrinter());
        assertEquals(1000, testPrinter.getToner());
    }
}
