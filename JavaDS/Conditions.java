import java.util.Scanner;
public class Conditions{
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
        
    }
}