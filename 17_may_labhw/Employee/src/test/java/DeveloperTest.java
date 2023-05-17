import org.junit.Before;
import org.junit.Test;
import staff.techStaff.Developer;

import static org.junit.Assert.assertEquals;

public class DeveloperTest {

    Developer sarah;

    @Before
    public void before(){
        sarah = new Developer("Sarah", 5678, 60000.99);
    }

    @Test
    public void hasName(){
        assertEquals("Sarah", sarah.getName());
    }

    @Test
    public void hasNINumber(){
        assertEquals(5678, sarah.getNINumber());
    }

    @Test
    public void hasSalary(){
        assertEquals(60000.99, sarah.getSalary(), 0.0);
    }

    @Test
    public void canRaiseSalary(){
        sarah.raiseSalary(9999.01);
        assertEquals(70000.00, sarah.getSalary(), 0.0);
    }

    @Test
    public void canPayBonus(){
        assertEquals((60000.99*0.01), sarah.payBonus(), 0.0);
    }
}
