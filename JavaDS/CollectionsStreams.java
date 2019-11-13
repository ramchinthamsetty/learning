import java.util.stream.*;

public class CollectionsStreams {

    public static void main(String[] args){

        //1. Integer Stream with range fucntion
        IntStream
			.range(1, 10)
			.forEach(System.out::print);
        System.out.println();

        //2. Integer Streams with Skip function
        IntStream
            .range(1,100) //Create a range of values
            .skip(50) //Skip the values before 50
            .forEach(x->System.out.println(x)); //Lamda Expression in Java

        //3. Applying /Calculating Sum of values
        System.out.println(IntStream
        .range(1,10)
        .skip(5)
        .sum()); //Calculate the SUM for values after 5

        //Sort, Finding First elements
        Stream.of("")
                .sorted()
                .findFirst()
                .ifPresent(System.out::println);
    }
}