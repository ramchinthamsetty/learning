/*
- Inheritance of Node class to Nodev2 class
- Super method to initialize the constructor of Node class
- Cannot access Private variables from Super Class. Make them public or accessible through API.
*/
public class Nodev2 extends Node {
    private String sLastName = "";
    private String sFirst = "";
    
    //Constructor initialization for Inherited class
    public Nodev2(String sName, int iID, String sEmail, String sLastName, String sFirst){
        super(sName, iID, sEmail); // to load Constructor from Super Class Node
        this.sLastName = sLastName; //Initialize additional parameters that are extended
        this.sFirst = sFirst; //Initialize additional parameters that are extended
    }
    /*
    Function to print all values
    */
    public void speak(){
        System.out.println(this.getsName()+" "+this.getiID()+" "+this.getsEmail()+" "+this.sFirst+" "+this.sLastName);

    }//speak() function
}//Nodev2