package demo;
import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    private Integer passenger;

    /*public UberVan(String license, Account driver,
        Map<String, Map<String, Integer>> typeCarAccepted,
        ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }*/

    public UberVan(String license, Account driver) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    @Override
    public void setPassenger(Integer passenger) {
        if (passenger == 6) {
            super.setPassenger(passenger);
        } else {
            System.out.println("Passenger must be 6");
        }
    }

    @Override
    void printDataCar() {
        super.printDataCar();
    }
}
