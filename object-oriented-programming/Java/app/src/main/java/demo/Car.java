package demo;

public class Car {
    private Integer id;
    private String license;
    private Account driver;
    protected Integer passenger;

    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {
        if (passenger != null) {
            System.out.println("License: " + license +
            " | Driver name: " + driver.name + " | Passengers: " +
            passenger);
        }
    }

    public Integer getPassenger(){
        return passenger;
    }

    public void setPassenger(Integer passenger){
        this.passenger = passenger;
    }

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getLicense() {
		return license;
	}

	public void setLicense(String license) {
		this.license = license;
	}

	public Account getDriver() {
		return driver;
	}

	public void setDriver(Account driver) {
		this.driver = driver;
	}
}
