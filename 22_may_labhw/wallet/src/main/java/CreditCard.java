import java.util.ArrayList;

public class CreditCard extends PaymentCard{

    private double credit;

    public CreditCard(int cardNumber, int expDate, int secNumber, ArrayList<Double> transactions, double credit){
        super(cardNumber, expDate, secNumber, transactions);
        this.credit = credit;
    }

    public double getCredit() {
        return this.credit;
    }

    public void charge(double purchaseAmount){
        getTransactions().add(purchaseAmount);
        double purchasePlusInterest = purchaseAmount * 1.05;
        this.credit -= purchasePlusInterest;
    }

}
