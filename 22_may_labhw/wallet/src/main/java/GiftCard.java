public class GiftCard implements IChargeable{

    private double balance;

    public GiftCard(double balance){
        this.balance = balance;
    }

    public double getBalance() {
        return this.balance;
    }

    @Override
    public void charge(double paymentAmount) {
        this.balance -= paymentAmount;
    }
}
