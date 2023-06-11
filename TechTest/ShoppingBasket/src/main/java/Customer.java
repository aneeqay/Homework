public class Customer {

    private boolean loyaltyCard;

    public Customer(boolean loyaltyCard) {
        this.loyaltyCard = loyaltyCard;
    }

    public boolean isLoyaltyCard() {
        return this.loyaltyCard;
    }

    public void setLoyaltyCard(boolean loyaltyCard) {
        this.loyaltyCard = loyaltyCard;
    }
}
