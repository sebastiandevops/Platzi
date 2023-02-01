package demo;

public class Driver extends Account {
    public Driver(String name, String document,
    String email, String password) {
        super(name, document, email, password);
    }
    void printDataDriver(){
        System.out.println("Driver document: " + document
        + " Driver name: " + name + " email: " + email +
        " Password: " + password);
    }
}
