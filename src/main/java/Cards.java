//Tyler Patenaude (300338859)
//This is a class for each card. There will be a 2dim array for holding each card on a "board" like in the actual game
public class Cards {
    //Each card will have each of these elements
    private char color;
    private char shape;
    private char num;
    private char fill;

    public Cards(char color, char shape, char num, char fill){
        this.color=color;
        this.shape=shape;
        this.num=num;
        this.fill=fill;
    }

    //Getters/Setters
    public char getColor() {
        return this.color;
    }
    public void setColor(char color) {
        this.color = color;
    }

    public char getShape() {
    	return this.shape;
    }
    public void setShape(char shape) {
    	this.shape = shape;
    }

    public char getNum() {
    	return this.num;
    }
    public void setNum(char num) {
    	this.num = num;
    }

    public char getFill() {
    	return this.fill;
    }
    public void setFill(char fill) {
    	this.fill = fill;
    } 

    @Override
    public String toString(){
        // return "Color: "  + color +
        //        " Shape: " + shape +
        //        " Num: "   + num   +
        //        " Fill: "  + fill; 
        return color + " " + shape + " " + num + " " + fill;
    }

    // ***** Taken from https://www.infoworld.com/article/3305792/comparing-java-objects-with-equals-and-hashcode.html, in the "Comparing objects with equals()" section
    //Used for finding duplicates 
    @Override
    public boolean equals(Object cardObj){
        if (this == cardObj){
            return true;
        }
        if (cardObj == null || getClass() != cardObj.getClass()){
            return false;
        }

        Cards otherCard = (Cards) cardObj;
        return this.color == otherCard.color &&
               this.shape == otherCard.shape &&
               this.num   == otherCard.num   &&
               this.fill  == otherCard.fill;
    }
}
