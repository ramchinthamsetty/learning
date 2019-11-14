import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.lang.Error;
import java.util.Arrays;
import java.util.stream.Stream;

public class BufferReaderTest {

    public static void main(String[] args) {
        String sRow;
        System.out.println("Working Directory = " + System.getProperty("user.dir"));
        // Open Buffer reader to process CSV file
        // FileReader fFile = new FileReader("TechCrunchcontinentalUSA.csv");
        // System.out.println(fFile.toString());
        File fFile = new File("C:/Users/n74z/Documents/Personal/Programming/LearningBasics/JavaDS/simpledata.csv");
        System.out.println(fFile.exists());
        try { //try catch block is required for BufferReaders
            BufferedReader bRead = new BufferedReader(new FileReader(fFile));
            // Read line by line of CSV file
            while ((sRow = bRead.readLine()) != null) {
                String[] saText = sRow.split(",");
                System.out.println(sRow);
                //
                Arrays.stream(saText)
                .filter(x -> x.startsWith("w")) //including lamda expressions
                .forEach(System.out::println);
                // System.out.println(value);
            }
            bRead.close();
        } catch (Exception e) {
            System.out.println(e);
        }

    }
}