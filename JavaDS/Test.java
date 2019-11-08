import java.util.Scanner; //import packages

public class Test {
    public static void main(String[] args){
        String str1 = "Hello This is my first test;"; 
        //primitive data types
        int i = 100;
        double y = 10.00;
        char c = 'b';
        boolean bFlag = true;

        System.out.println(str1.length());
        System.out.println(i);
        System.out.println(y);
        System.out.println(c);
        System.out.println(bFlag);
        str1 = "Changing data there!";  //Changing data, Mutable
        System.out.println(str1);

        //reading inputs from User, like a scanf in C
        Scanner sc = new Scanner(System.in);
        String new1 = sc.nextLine(); //Next vs NextLine (reads complete line)
        int x = sc.nextInt(); // reading integer
        boolean bTest = sc.nextBoolean();
        System.out.println(new1);
        System.out.println(x); 
        System.out.println(bTest); 
        sc.close(); //closing the scanner
    }
    
  
}