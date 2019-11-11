public class StatFunc {
    //Private access specifier limits access to Class instance.
    private String sName = ""; 
    private int iID = 0;
    private String sEmail = "";
    protected static int iEmpCount = 0;

    // Constructor for a Class
    public StatFunc(String sName, int iID, String sEmail) {
        this.sName = sName;
        this.iID = iID;
        this.sEmail = sEmail;
        Node.iEmpCount += 1;
        StatFunc.funcname();
    }

    public String getsEmail() {
        return sEmail;
    }

    public void setsEmail(String sEmail) {
        this.sEmail = sEmail;
    }

    public int getiID() {
        return iID;
    }

    public void setiID(int iID) {
        this.iID = iID;
    }

    public String getsName() {
        return sName;
    }

    public void setsName(String sName) {
        this.sName = sName;
    }

    public static void funcname(){
        System.out.println("This is node class");
    }

}