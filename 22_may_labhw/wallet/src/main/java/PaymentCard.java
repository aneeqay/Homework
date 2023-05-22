import java.util.ArrayList;

public abstract class PaymentCard implements IChargeable{

    private int cardNumber;
    private int expDate;
    private int secNumber;
    private ArrayList<Double> transactions;

    public PaymentCard(int cardNumber, int expDate, int secNumber, ArrayList<Double> transactions){
        this.cardNumber = cardNumber;
        this.expDate = expDate;
        this.secNumber = secNumber;
        this.transactions = transactions;
    }

    public int getCardNumber() {
        return this.cardNumber;
    }

    public int getExpDate() {
        return this.expDate;
    }

    public int getSecNumber() {
        return this.secNumber;
    }

    public ArrayList<Double> getTransactions() {
        return this.transactions;
    }

    public void charge(double purchaseAmount){}

    public Double getTransaction(int index){
        return getTransactions().get(index);
    }
}
