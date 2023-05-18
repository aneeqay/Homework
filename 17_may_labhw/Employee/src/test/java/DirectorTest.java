import org.junit.Before;
import org.junit.Test;
import staff.management.Director;

import static org.junit.Assert.assertEquals;

public class DirectorTest {

    Director keith;

    @Before
    public void before(){
        keith = new Director("Keith", 1234, 70500.67, "Technology", 5000.01);
    }

    @Test
    public void hasName(){
        assertEquals("Keith", keith.getName());
    }

    @Test
    public void hasNINumber(){
        assertEquals(1234, keith.getNINumber());
    }

    @Test
    public void hasSalary(){
        assertEquals(70500.67, keith.getSalary(), 0.0);
    }

    @Test
    public void hasDept(){
        assertEquals("Technology", keith.getDeptName());
    }

    @Test
    public void canRaiseSalary(){
        keith.raiseSalary(499.33);
        assertEquals(71000.00, keith.getSalary(), 0.0);
    }

    @Test
    public void canPayBonus(){
        assertEquals((70500.67*0.02), keith.payBonus(), 0.0);
    }

    @Test
    public void hasBudget(){
        assertEquals(5000.01, keith.getBudget(), 0.0);
    }

}