import org.junit.Before;
import org.junit.Test;
import staff.management.Manager;

import static org.junit.Assert.assertEquals;

public class ManagerTest {

    Manager geri;

    @Before
    public void before(){
        geri = new Manager("Geri", 1234, 70500.67, "Technology");
    }

    @Test
    public void hasName(){
        assertEquals("Geri", geri.getName());
    }

    @Test
    public void hasNINumber(){
        assertEquals(1234, geri.getNINumber());
    }

    @Test
    public void hasSalary(){
        assertEquals(70500.67, geri.getSalary(), 0.0);
    }

    @Test
    public void hasDept(){
        assertEquals("Technology", geri.getDeptName());
    }

    @Test
    public void canRaiseSalary(){
        geri.raiseSalary(499.33);
        assertEquals(71000.00, geri.getSalary(), 0.0);
    }

    @Test
    public void canPayBonus(){
        assertEquals((70500.67*0.01), geri.payBonus(), 0.0);
    }

}
