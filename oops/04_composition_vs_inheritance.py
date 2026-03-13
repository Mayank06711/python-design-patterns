"""
Practice 4: Composition vs Inheritance (is-a vs has-a)

Build a Car system using COMPOSITION (not inheritance):

1. Engine class:
   - __init__(self, horsepower)
   - start() returns "Engine ({hp}hp) started"
   - stop() returns "Engine stopped"

2. GPS class:
   - __init__(self, brand)
   - navigate(destination) returns "Navigating to {destination} via {brand}"

3. Car class (uses COMPOSITION — has-a Engine, has-a GPS):
   - __init__(self, name, engine: Engine, gps: GPS)
   - start() — starts the engine and returns "Car {name}: {engine.start()}"
   - drive(destination) — returns "{gps.navigate(destination)}"
   - stop() — stops engine and returns "Car {name}: {engine.stop()}"

The point: Car is NOT an Engine. Car is NOT a GPS. Car HAS an Engine and HAS a GPS.
"""


class Engine:
    def __init__(self, horsepower):
        self._horsepower = horsepower

    def start(self):
        return f"Engine ({self._horsepower}hp) started"
    
    def stop(self):
        return "Engine stopped"

class GPS:
    def __init__(self, brand):
        self._brand = brand
    
    def navigate(self, destination):
        return f"Navigating to {destination} via {self._brand}"


class Car:
    def __init__(self, name:str, eng: Engine, gps: GPS):
        self._name = name
        self._eng = eng
        self._gps = gps

    def start(self):
        return f"Car {self._name}: {self._eng.start()}"
    
    def drive(self, destination:str):
        return f"{self._gps.navigate(destination)}"

    def stop(self):
        return f"Car {self._name}: {self._eng.stop()}"



# ============ TEST CASES (DO NOT MODIFY) ============

if __name__ == "__main__":
    engine = Engine(150)
    gps = GPS("Google Maps")
    car = Car("Swift", engine, gps)

    # Test 1: Car starts engine
    result = car.start()
    assert result == "Car Swift: Engine (150hp) started", f"Got: {result}"
    print("Test 1 PASS: car.start() delegates to engine")

    # Test 2: Car uses GPS
    result = car.drive("Mumbai")
    assert result == "Navigating to Mumbai via Google Maps", f"Got: {result}"
    print("Test 2 PASS: car.drive() delegates to GPS")

    # Test 3: Car stops engine
    result = car.stop()
    assert result == "Car Swift: Engine stopped", f"Got: {result}"
    print("Test 3 PASS: car.stop() delegates to engine")

    # Test 4: Swap GPS at runtime (composition advantage!)
    car2 = Car("BMW", Engine(300), GPS("Apple Maps"))
    result = car2.drive("Delhi")
    assert result == "Navigating to Delhi via Apple Maps", f"Got: {result}"
    print("Test 4 PASS: different car with different GPS works")

    # Test 5: Car is NOT an Engine (no inheritance)
    assert not isinstance(car, Engine), "Car should NOT be an instance of Engine"
    assert not isinstance(car, GPS), "Car should NOT be an instance of GPS"
    print("Test 5 PASS: Car does not inherit from Engine or GPS")

    print(f"\nAll tests passed!")
    print("Key takeaway: Composition lets you swap parts (Engine, GPS) at runtime.")
    print("Inheritance would lock you into one fixed relationship.")
