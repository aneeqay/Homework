import java.util.ArrayList;

public class Library {

    private int capacity;
    private ArrayList<Book> books;

    public Library(int capacity){
        this.capacity = capacity;
        this.books = new ArrayList<>();
    }

    public int numOfBooks(){
        return this.books.size();
    }

    public void addBook(Book book){
        if (this.capacity > this.numOfBooks()){
        this.books.add(book);}
    }

    public void lendBook(Book book, Borrower borrower){
        this.books.remove(book);
        borrower.borrowBook(book);
    }


}
