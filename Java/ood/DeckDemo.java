package ood;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DeckDemo {
    public static void main(String[] args) {
        Deck deck = new Deck();
        for(int i = 0; i < 20; i++) {
            System.out.println(deck.draw());
        }
    }
}

class Deck {
    public static final int NUM_CARDS = 52;
    private List<Card> cards = new ArrayList<>();

    public Deck() {
        for(Suit suit : Suit.values()) {
            for(int i = 1; i <= 13; i++) {
                cards.add(new Card(i, suit));
            }
        }
    }

    public void shuffle() {
        Collections.shuffle(cards);
    }

    public Card draw() {
        shuffle();
        return cards.get(0);
    }
}

class Card {
    private int faceValue;
    private Suit suit;

    public Card(int faceValue, Suit suit) {
        if (faceValue < 1 || faceValue > 13) {
            throw new IllegalArgumentException("Face value can be from 1 to 13 only");
        }
        this.faceValue = faceValue;
        this.suit = suit;
    }

    public int getFaceValue() {
        return faceValue;
    }

    public Suit getSuit() {
        return suit;
    }

    public String displayName() {
        return toString();
    }

    @Override
    public String toString() {
        return faceValueToDisplayName() + " of " + suit.getDisplayName() + "s";
    }

    private String faceValueToDisplayName() {
        switch(faceValue) {
            case 1 : return "Ace";
            case 2 : return "Two";
            case 3 : return "Three";
            case 4 : return "Four";
            case 5 : return "Five";
            case 6 : return "Six";
            case 7 : return "Seven";
            case 8 : return "Eight";
            case 9 : return "Nine";
            case 10 : return "Ten";
            case 11 : return "Jack";
            case 12 : return "Queen";
            case 13 : return "King";
            default : throw new IllegalStateException();
        }
    }
}

enum Suit {
    SPADE("Spade"), HEART("Heart"), CLUB("Club"), DIAMOND("Diamond");
    private String displayName;

    Suit(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }
}
