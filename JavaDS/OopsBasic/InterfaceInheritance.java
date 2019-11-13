public interface InterfaceInheritance extends InterfaceNode{

    //
    public void process2();
    public void display2();
    default void fun1(){
        System.out.println("This is a default function in Java 8");
        
    }
}