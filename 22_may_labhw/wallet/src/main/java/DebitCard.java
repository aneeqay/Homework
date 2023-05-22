import java.util.ArrayList;

public class DebitCard extends PaymentCard implements IChargeable{

    private int accNumber;
    private int sortCode;

    public DebitCard(int cardNumber, int expDate, int secNumber, ArrayList<Double> transactions, int accNumber, int sortCode){
        super(cardNumber, expDate, secNumber, transactions);
        this.accNumber = accNumber;
        this.sortCode = sortCode;
    }

    public int getAccNumber() {
        return this.accNumber;
    }

    public int getSortCode() {
        return this.sortCode;
    }

    public void charge(double purchaseAmount){
        getTransactions().add(purchaseAmount);
    }
}
