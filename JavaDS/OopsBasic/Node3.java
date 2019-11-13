public class Node3 extends Nodev2{
    private String sCompany;
    private String sRole;

    public Node3(String sName,int iID, String sEmail,String sLastName,String sFirst,String sCompany,String sRole)
    {
        super(sName, iID, sEmail, sLastName, sFirst);
        this.sCompany = sCompany;
        this.sRole = sRole;
    }
    public void display(){
        this.speak();
        System.out.println(sCompany+sRole);
    }
}