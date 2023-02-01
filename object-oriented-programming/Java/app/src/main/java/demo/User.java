package demo;

public class User extends Account {
    public User(String name, String document,
    String email, String password) {
        super(name, document, email, password);
    }
    void printDataUser(){
        System.out.println("User document: " + document
        + " User name: " + name + " email: " + email +
        " Password: " + password);
    }
}
