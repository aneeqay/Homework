import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    private Calculator calculator;

    @Before
    public void before(){
        calculator = new Calculator();
    }

    @Test
    public void canAdd(){
        assertEquals(3, calculator.add(1, 2));
    }

    @Test
    public void canSubtract(){
        assertEquals(10, calculator.subtract(20, 10));
    }

    @Test
    public void canMultiply(){
        assertEquals(20, calculator.multiply(4, 5));
    }

    @Test
    public void canDivide(){
        assertEquals(1.00, calculator.divide(10.99, 10.99), 0.0);
    }


}
