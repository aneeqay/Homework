import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class LibraryTest {

    Library aneeqasLib;
    Book inferno;
    Book peterRabbit;
    Book taste;
    Borrower arrietty;

    @Before
    public void setUp(){
        aneeqasLib = new Library(2);
        inferno = new Book("Inferno", "Dan Brown", "thriller");
        peterRabbit = new Book("The Tales of Peter Rabbit", "Beatrix Potter", "children");
        taste = new Book("Taste", "Stanley Tucci", "Memoir");
        arrietty = new Borrower();
    }

    @Test
    public void canAddBooks(){
        aneeqasLib.addBook(inferno);
        assertEquals(1, aneeqasLib.numOfBooks());
    }

    @Test
    public void cannotAddBooks(){
        aneeqasLib.addBook(inferno);
        aneeqasLib.addBook(taste);
        aneeqasLib.addBook(peterRabbit);
        assertEquals(2, aneeqasLib.numOfBooks());
    }

    @Test
    public void canLendBooks(){
        aneeqasLib.addBook(taste);
        aneeqasLib.lendBook(taste, arrietty);
        assertEquals(0, aneeqasLib.numOfBooks());
        assertEquals(1, arrietty.noOfBooks());
    }

}
