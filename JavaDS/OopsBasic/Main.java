

public class Main{

    public static void main(String[] args){
        
        Node nNode = new Node("ram",798,"ram@outlook.com");
        System.out.println(nNode.getsName());
        System.out.println(nNode.getiID());
        System.out.println(nNode.getsEmail());
        Node nNode2 = new Node("hari",798,"hari@outlook.com");
        System.out.println(nNode2.getsName());
        System.out.println(nNode2.getiID());
        System.out.println(nNode2.getsEmail());

        //All three prints are same below, gives the same result. Since the variable is static to class
        //Memory allocated in Static section
        System.out.println(Node.iEmpCount);
        System.out.println(nNode2.iEmpCount);
        System.out.println(nNode.iEmpCount);

        //Inheritance of Java. 
        //Even inherited the Static values increments.
        Nodev2 nNodev2 = new Nodev2("ram",798,"ram@outlook.com","Rama krishna","Chinthamsetty");
        nNodev2.speak();
        System.out.println(Node.iEmpCount);

        Node3 nNode3 = new Node3("ram",798,"ram@outlook.com","Rama krishna","Chinthamsetty","Eurofins","PSE");
        nNode3.display();
        //calling static function - No need to create an instance of class
        StatFunc.funcname(); //Stored in Static section of Java.

        //Calling Enums in Java
        // Enums are constants 
        Level lvl = Level.LOW;
        System.out.println(lvl);

        
    }
}