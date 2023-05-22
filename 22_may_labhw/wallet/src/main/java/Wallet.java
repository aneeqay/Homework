import java.util.ArrayList;

public class Wallet {

    private ArrayList<IChargeable> cards;

    public Wallet(ArrayList<IChargeable> cards){
        this.cards = cards;
    }

    public ArrayList<IChargeable> getCards() {
        return this.cards;
    }

    public void addCard(IChargeable newCard){
        getCards().add(newCard);
    }

//    public IChargeable selectCard(IChargeable selectedCard) {
//        for (DebitCard card : cards) {
//            if (card == selectedCard) {
//                return card;
//            } else for (CreditCard card1 : cards) {
//                if (card1 == selectedCard) {
//                    return card1;
//                } else for (GiftCard card2 : cards) {
//                    if (card2 == selectedCard) {
//                        return card2;
//                    }
//                }
//            }
//        } return null;
//    }

    public IChargeable getCard(int index){
        return getCards().get(index);
    }

    public void pay(int index, int purchaseAmount){
        IChargeable card = getCard(index);
        card.charge(purchaseAmount);
    }

}

