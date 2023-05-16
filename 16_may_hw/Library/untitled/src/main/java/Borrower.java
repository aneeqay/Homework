import java.util.ArrayList;

public class Borrower {
    private ArrayList<Book> collection;

    public Borrower(){
        this.collection = new ArrayList<>();
    }

    public void borrowBook(Book book){
        this.collection.add(book);
    }

    public int noOfBooks(){
        return this.collection.size();
    }
}
