import java.util.Scanner;
public class Conditions{

    private static enum Size {
        SMALL, MEDIUM, LARGE, X_LARGE
    };
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); //Define InPut Stream - read, write - system calls in C
        // String s = sc.next(); //read word by word
        String sLine = sc.nextLine(); //Read line by Line
        //Conditional Statements
        try {
            if(sLine.equals("hello")){
                System.out.println(sLine);
            }
            else if(sLine.equals("this data")){ //Comparing String
                System.out.println(sLine);
            }
            else{
              int i=  Integer.parseInt(sLine);
              System.out.println(i);
            }
        } catch (java.lang.NumberFormatException e) { //NumberFormat exception handling
            System.out.println("Number is AlphaNumeric");
            System.out.println(e);
        }
        finally{
            System.out.println("Finally here!");
        }



        //Switch case here with Enum Variables
        int size = sc.nextInt(); //Scanning Integer Values

        switch((int)size) {

            case 1   : { System.out.println("size is small");   break; }
            case 2  : { System.out.println("size is medium");  break; }
            case 3   : { System.out.println("size is large");   break; }
            case 4 : { System.out.println("size is X-large"); break; }

            default : { System.out.println("size is not small, medium, large or X-large, but was " + size); }
        }
        
    }
}