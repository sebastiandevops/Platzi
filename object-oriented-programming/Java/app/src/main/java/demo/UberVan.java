package demo;
import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatMaterial;

    public UberVan(String license, Account driver,
        Map<String, Map<String, Integer>> typeCarAccepted,
        ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }
}
