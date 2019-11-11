import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class CollectionsMap{

    public static void main(String[] args){

        Map oMap = new HashMap(); //HashMap's are not synchronized. HashTables are synchronized.
        oMap.put(1,2);
        oMap.put(1,3);
        oMap.put("key","Option");
        oMap.put(3,9);
        oMap.put(4,16);
        System.out.println(oMap);

        Map tMap = new TreeMap(); // Data is sorted in order by keys.
        tMap.put(1,2);
        tMap.put(-11,3);
        //tMap.put("key","Option"); //Key should be similar data type in TreeMap
        tMap.put(3,9);
        tMap.put(-4,16);
        System.out.println(tMap);

        Map lMap = new LinkedHashMap(); //Keep things as we add elements into it.
        lMap.put("ram", "Ramya");
        lMap.put("rk", "mrsrk");
        lMap.put("a", "all");
        System.out.println(lMap);
        System.out.println(lMap.containsValue("Ramya")); //True if value exists
        System.out.println(lMap.get("ram")); //Get Key value, null if there is no value
        System.out.println(lMap.containsKey("ram")); //True if Key exists

    }//main
}