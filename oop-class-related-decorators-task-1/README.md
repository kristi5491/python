### Class-Related Decorators. Task 1
***
#### Description

You need to create abstract class `Vehicle`. Classes `Car`, `Motorcycle`, `Truck`, `Bus` are inherited from `Vehicle` 
and already implemented. 

Class `Vehicle` accepts the following parameters:

- `brand_name` -> str (e.g. Honda)
- `year_of_issue` -> int (e.g. 2020)
- `base_price` -> int (e.g. 1_000_000)
- `mileage` -> int (e.g. 10_000)

The following methods should be implemented:

- `vehicle_type` - returns str - type of the vehicle in the following pattern *brand_name + name of the class*.
  For example: *Toyota Car*, *Suzuki Motorcycle*;
- `is_motorcycle` return boolean value depends on the amount of wheels (2 wheels -> motorcycle, so method should return *True*);
- `purchase_price` - returns the price of the vehicle: (`base_price - 0.1 * mileage`). If the result price is less than 100_000, 
method should return 100_000.

Put the following decorators where necessary and if it is necessary:

`abstractmethod`, `classmethod`, `staticmethod`, `property` and other decorators.

#### Example


    >>> vehicles = (
        Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
        Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
        Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
        Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
    )
    
    >>> for vehicle in vehicles:
            print(
                f"Vehicle type={vehicle.vehicle_type()}\n"
                f"Is motorcycle={vehicle.is_motorcycle()}\n"
                f"Purchase price={vehicle.purchase_price}\n"
            )
    

    Vehicle type=Toyota Car
    Is motorcycle=False
    Purchase price=985000.0
    
    Vehicle type=Suzuki Motorcycle
    Is motorcycle=True
    Purchase price=796500.0
    
    Vehicle type=Scania Truck
    Is motorcycle=False
    Purchase price=14915000.0
    
    Vehicle type=MAN Bus
    Is motorcycle=False
    Purchase price=9905000.0

