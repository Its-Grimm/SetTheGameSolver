import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

//Tyler Patenaude (300338859)
class tester {

    @Test
    void testToString(){
        Cards c = new Cards('p', 'd', '2', 'f');
        assertEquals("p d 2 f", c.toString());
    }

    @Test
    void testGetAttributes(){
        Cards attrTest = new Cards('p', 'd', '2', 'f');
        assertEquals('p', attrTest.getColor());
        assertEquals('d', attrTest.getShape());
        assertEquals('2', attrTest.getNum());
        assertEquals('f', attrTest.getFill());
    }

    @Test 
    void testSolve1(){
        //Answers.png
        char[][] quickInputCards = {
            {'g', 'o', '2', 'f'}, 
            {'f', 'd', '1', 'g'}, //Swapped g and f
            {'r', 'd', '1', 'f'},
            {'g', 's', '1', 'e'},
            {'p', 's', '3', 'f'},
            {'g', 's', '3', 'e'},
            {'l', '1', 'o', 'g'}, //Swapped 1 and o, g and l
            {'r', 'd', '1', 'e'},
            {'1', 'f', 'g', 's'}, //Swapped g and 1, s and f
            {'p', 'o', '1', 'e'},
            {'g', 'o', '2', 'l'},
            {'p', 'o', '2', 'e'}
        };
        Cards[] cardArr = new Cards[quickInputCards.length];
        for (int i=0; i<quickInputCards.length; i++){
            char[] charArr = SetTheGameSolver.validateCardProperties(quickInputCards[i]); //Validator verifies each card has proper attributes, then sorts them back into order (g o 2 f)
            cardArr[i] = new Cards(charArr[0], charArr[1], charArr[2], charArr[3]); //Adds them to the card array
        }
    
        assertEquals('g', cardArr[3].getColor());
        assertEquals('f', cardArr[4].getFill());

        //Run the solver on the quickInputCards
        String output = SetTheGameSolver.solve(cardArr);
        String realOutput = "g o 2 f-r d 1 f-p s 3 f ||| AT 1:3:5\n"  +
                            "g d 1 f-g s 1 e-g o 1 l ||| AT 2:4:7\n"  + 
                            "g d 1 f-g s 3 e-g o 2 l ||| AT 2:6:11\n" +
                            "g s 1 e-r d 1 e-p o 1 e ||| AT 4:8:10\n" +
                            "p s 3 f-r d 1 e-g o 2 l ||| AT 5:8:11\n" + 
                            "g s 3 e-r d 1 e-p o 2 e ||| AT 6:8:12\n" ;

        assertEquals(realOutput , output);
    }

}