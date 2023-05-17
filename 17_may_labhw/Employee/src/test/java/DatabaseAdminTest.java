import org.junit.Before;
import org.junit.Test;
import staff.techStaff.DatabaseAdmin;

import static org.junit.Assert.assertEquals;

public class DatabaseAdminTest {

    DatabaseAdmin claire;

    @Before
    public void before(){
        claire = new DatabaseAdmin("Sarah", 9999, 60000.99);
    }

    @Test
    public void hasName(){
        assertEquals("Sarah", claire.getName());
    }

    @Test
    public void hasNINumber(){
        assertEquals(9999, claire.getNINumber());
    }

    @Test
    public void hasSalary(){
        assertEquals(60000.99, claire.getSalary(), 0.0);
    }

    @Test
    public void canRaiseSalary(){
        claire.raiseSalary(9999.01);
        assertEquals(70000.00, claire.getSalary(), 0.0);
    }

    @Test
    public void canPayBonus(){
        assertEquals((60000.99*0.01), claire.payBonus(), 0.0);
    }
}

