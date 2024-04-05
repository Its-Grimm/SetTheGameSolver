//Tyler Patenaude (300338859)

import java.util.Set;
import java.util.Scanner;
import java.util.LinkedHashSet;

public class SetTheGameSolver{
    public static void main(String[] args) {
        // read input to set up the game instance however you want
        Scanner sc = new Scanner(System.in);
    
        // //All of the cards which will be fed into the board, along with the counter to ensure 11 cards will be added 
        // //Tried to do this with array, but way easier to ensure no dupes with Sets
        // //Also swapped from regular HashSet to LinkedHashSet to maintain insertion order. Found from here: http://www.java2s.com/Tutorial/Java/0140__Collections/CreatingaSetThatRetainsOrderofInsertion.htm
        Set<Cards> allCards = new LinkedHashSet<Cards>();    
        int counter = 0;

        //While there are cards to add to the board
        while (counter < 12){
            System.out.println("Give me " + (12-counter) + " card(s) in the form of Color:(G/R/P), Shape:(D/O/S), Num:(1/2/3), Fill:(E/F/L)");
            String str = sc.nextLine().toLowerCase();
            int strLength = str.length();

            if (strLength == 4){ 
                //Splitting word into char array and running it through the validator (checks if a card is valid with no duplicate properties)
                char[] valid = validateCardProperties(str.toCharArray());

                //If it did not return empty array
                if (valid.length != 0){ 
                    //Catches duplicate cards inputted
                    Cards newCard = new Cards(valid[0], valid[1], valid[2], valid[3]);
                    Cards[] oldCards = allCards.toArray(new Cards[allCards.size()]);
                    //For every card in oldCards (toArray of allCards)
                    boolean noDupe = true;
                    for (Cards oneCard : oldCards){
                        if (oneCard.equals(newCard)){
                            System.out.println("This card already exists on the board, choose a card with different properties");
                            noDupe = false;
                            break;
                        }
                    }  
                    if (noDupe){
                        allCards.add(newCard);
                        counter++;
                    }
                }
                else{
                    System.out.println("That was not a valid card, please try again!");
                }
            }
            else{
                System.out.println("Only input a card with valid properties. Try again");
            }
        }
        String allSets = (solve(allCards.toArray(new Cards[allCards.size()])));
        ExportToFile.run(allSets);
        System.out.println(allSets);
        sc.close();
    }

    public static char[] validateCardProperties(char[] valWord){
        //Flags to catch repeated values (ggd1 would get caught)
        boolean colorFound = false;
        boolean shapeFound = false;
        boolean numFound = false;
        boolean fillFound = false;
        
        //New array to return proper order for easy manipulating: (color, shape, num, fill)
        char[] newArr = new char[valWord.length];
        for (int i=0; i<valWord.length; i++){
            if (!colorFound && valWord[i] == 'g' || valWord[i] == 'r' || valWord[i] == 'p'){
                newArr[0] = valWord[i];
                colorFound = true;
            }
            if (!shapeFound && valWord[i] == 'd' || valWord[i] == 'o' || valWord[i] == 's'){
                newArr[1] = valWord[i];
                shapeFound = true;
            }
            if (!numFound && valWord[i] == '1' || valWord[i] == '2' || valWord[i] == '3'){
                newArr[2] = valWord[i];
                numFound = true;
            }
            if (!fillFound && valWord[i] == 'e' || valWord[i] == 'f' || valWord[i] == 'l'){
                newArr[3] = valWord[i];
                fillFound = true;
            }
        } 
        //If a repeated and/or missing value was found
        if (!colorFound || !shapeFound || !numFound || !fillFound){
                return new char[0];
        }
        return newArr;
    }

    public static String solve(Cards[] cardArr) {
        System.out.println();
        
        String allSets = "";
        //Finding and adding all of the set combinations
        for (int i=0; i<cardArr.length; i++){
            for (int j=i+1; j<cardArr.length; j++){
                for (int k=j+1; k<cardArr.length; k++){
                    if (isSet(cardArr[i], cardArr[j], cardArr[k]) && i!=j && j!= k && k!=i){
                        allSets += (cardArr[i] + "-" + cardArr[j] + "-" + cardArr[k] + " ||| AT " + (i+1) + ":" + (j+1) + ":" + (k+1) +"\n");
                    }
                }
            }
        }
        System.out.println();
        return allSets; 
    }
    
    //For finding if a combination of three cards are a set
    public static boolean isSet(Cards a, Cards b, Cards c) {
        // returns true if the three cards a,b,c are a valid SET and false otherwise
        boolean colorSet=false;
        boolean shapeSet=false;
        boolean numSet=false;
        boolean fillSet=false;
        //If the attributes of each 3 cards are completely different or if they are all the exact same, then it is a set
        if ((a.getColor() != b.getColor() && b.getColor() != c.getColor() && c.getColor() != a.getColor()) || (a.getColor() == b.getColor() && b.getColor() == c.getColor())){
            colorSet=true;
        }
        if ((a.getShape() != b.getShape() && b.getShape() != c.getShape() && c.getShape() != a.getShape()) || (a.getShape() == b.getShape() && b.getShape() == c.getShape())){
            shapeSet=true;
        }
        if ((a.getNum() != b.getNum() && b.getNum() != c.getNum() && c.getNum() != a.getNum()) || (a.getNum() == b.getNum() && b.getNum() == c.getNum())) {
            numSet = true;
        }
        if ((a.getFill() != b.getFill() && b.getFill() != c.getFill() && c.getFill() != a.getFill()) || (a.getFill() == b.getFill() && b.getFill() == c.getFill())) {
            fillSet = true;
        }
        //If all bool set variables are true, then it is a set
        return (colorSet && shapeSet && numSet && fillSet);
    }
}