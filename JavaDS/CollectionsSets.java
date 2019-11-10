import java.util.Set;
import java.util.TreeSet;
import java.util.HashSet;
import java.util.LinkedHashSet;

//Example implementations using Sets in Java
/*
    Sets doesn't accept duplicates; Unordered, Unindexed
*/

public class CollectionsSets{

    public static void main(String[] args)
    {
        //Types of Sets - HashSet (Takes same time to search), Reduce Time Complexity.
        Set<Integer> s1 =  new HashSet<Integer>(); //Ordered Elements
        s1.add(10);
        s1.add(10);
        s1.add(9);
        s1.add(8);
        s1.add(78);
        s1.add(-8);
        System.out.println(s1);
        Set<Integer> s2 =  new TreeSet<Integer>(); //Ordered Elements
        s2.add(10);
        s2.add(10);
        s2.add(9);
        s2.add(8);
        s2.add(78);
        s2.add(-8);
        System.out.println(s2);
        System.out.println(s2.contains(0));
        Set<Integer> s3 =  new LinkedHashSet<Integer>(); // Unordered 
        s3.add(10);
        s3.add(10);
        s3.add(9);
        s3.add(8);
        s3.add(78);
        s3.add(-8);
        System.out.println(s3);
        

    }//Main Func
}