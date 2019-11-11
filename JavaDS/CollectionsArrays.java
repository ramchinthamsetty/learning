import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

public class CollectionsArrays{

    public static void main(String[] args){
        ArrayList<Integer> ar1 =  new ArrayList<Integer>(); 
        ar1.add(10);
        ar1.add(23);
        ar1.add(2);
        ar1.add(-10);
        System.out.println(ar1); 
        System.out.println(ar1.get(0)); //Indexed, Not Ordered.
        System.out.println(ar1.get(2)); //Indexed, Not Ordered.

        LinkedList<Object> l1 = new LinkedList(); //Object data type can be an Integer, Float, Integer
        l1.add(2);
        l1.add(3);
        l1.add(-1);
        l1.add(-3);
        l1.add("String");
        l1.add(3.0);
        l1.add(5.00);
        System.out.println(l1.getFirst());
        l1.addFirst(1234); //
        System.out.println(l1);

        ArrayList<Object> arobj1 = new ArrayList<Object>(); //Object can be type Integer, float, String
        arobj1.add("String");
        arobj1.add(12);
        arobj1.add(13.00);

        System.out.println(arobj1);
        
    }//Main func
}