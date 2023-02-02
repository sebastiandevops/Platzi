package demo;
import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatMaterial;

    public UberBlack(String license, Account driver,
        Map<String, Map<String, Integer>> typeCarAccepted,
        ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }

    @Override
    public void setPassenger(Integer passenger) {

        if (passenger == 4) {
            super.setPassenger(passenger);
        } else {
            System.out.println("UberVan needs 4 passengers assigned");
        }
    }
}
