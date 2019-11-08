import java.util.Scanner;

public class DSCollections {

    public static void main(String[] args){
        //Declaring Array of 10 strings. As lists in Python. Defining data types is important here
        String[] newArr = new String[10]; //Initializing with Null data by default
        newArr[0] = "String1";
        newArr[1] = "String2";
        newArr[2] = "String3";
        newArr[3] = "String4";
        System.out.println(newArr);
        //simple for loop
        for (int i=0;i< newArr.length;i++){
            System.out.println(newArr[i]); 
        }//for loop end
        // For each loop - It will print all the elements
        for (String element:newArr){
            if (element!= null) //filtering data without null
            {
                System.out.println(element); 
            }
           
        }
        Integer[] intArr = new Integer[10];
        intArr[1] = 100;
        intArr[2] = 300;
        //simple for loop
        for (int i=0;i< intArr.length;i++){
            System.out.println(intArr[i]); 
        }//for loop end
    }
}