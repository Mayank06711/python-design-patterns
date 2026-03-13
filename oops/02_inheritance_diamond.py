"""
Practice 2: Inheritance + Diamond Problem

Build a food delivery restaurant hierarchy:
1. Restaurant (base) — has name, accept_order() returns "Order accepted by {name}"
2. VegRestaurant(Restaurant) — has menu_type() returns "Veg", prepare() returns "Cooking veg: {item}"
3. NonVegRestaurant(Restaurant) — has menu_type() returns "Non-veg", prepare() returns "Grilling non-veg: {item}"
4. FusionRestaurant(VegRestaurant, NonVegRestaurant) — Diamond!
   - menu_type() returns "Both veg & non-veg"
   - prepare() should call BOTH parent prepare methods and combine them

After building, answer these questions by filling in the prints at the bottom.
"""


class Restaurant:
    def __init__(self, name: str):
        self._name = name
    def accept_order(self):
        return f"Order accepted by {self._name}"

class VegRestaurant(Restaurant):
    def __init__(self, name:str):
        super().__init__(name)

    def menu_type(self):
        return "Veg"

    def prepare(self, item: str):
        return f"Cooking veg: {item}"




class NonVegRestaurant(Restaurant):
    def __init__(self, name:str):
        super().__init__(name)
    def menu_type(self):
        return "Non-veg"
    def prepare(self, item:str):
        return f"Grilling non-veg: {item}"


class FusionRestaurant(VegRestaurant, NonVegRestaurant):
    def __init__(self, name:str):
        super().__init__(name)

    def menu_type(self):
        return "Both veg & non-veg"
    
    def prepare(self, item:str):
        #When you have multiple inheritance and need to call both parents, super() can't do it — it only follows one path. 
        # veg_res = super().prepare(item) # this will call veg res prepare as its next in mro (method resolution order) which goes from class to its common anchestior follow left to right so look like-> Fushion -> veg ->non-veg->res->obj
        # non_veg_res = super().prepare(item) # this is same as above so we never called non-veg one
        
        #Soltuon one: Call methods directly on class
        veg_res = VegRestaurant.prepare(self, item)
        non_veg_res = NonVegRestaurant.prepare(self, item) # here self means this fusion obj

        return veg_res + "&" + non_veg_res

# ============ TEST CASES (DO NOT MODIFY) ============

if __name__ == "__main__":
    # Test 1: Basic inheritance
    veg = VegRestaurant("Green Kitchen")
    assert veg.accept_order() == "Order accepted by Green Kitchen"
    print("Test 1 PASS: VegRestaurant inherits accept_order()")

    # Test 2: Method specific to child
    assert veg.menu_type() == "Veg"
    print("Test 2 PASS: VegRestaurant.menu_type() works")

    nonveg = NonVegRestaurant("Meat House")
    assert nonveg.menu_type() == "Non-veg"
    print("Test 3 PASS: NonVegRestaurant.menu_type() works")

    # Test 4: Diamond — FusionRestaurant
    fusion = FusionRestaurant("Fusion Bites")
    assert fusion.accept_order() == "Order accepted by Fusion Bites"
    print("Test 4 PASS: FusionRestaurant inherits accept_order()")

    assert fusion.menu_type() == "Both veg & non-veg"
    print("Test 5 PASS: FusionRestaurant.menu_type() overrides correctly")

    # Test 6: MRO check
    mro_names = [cls.__name__ for cls in FusionRestaurant.__mro__]
    print(f"\nTest 6: MRO = {mro_names}")
    assert mro_names == ["FusionRestaurant", "VegRestaurant", "NonVegRestaurant", "Restaurant", "object"]
    print("Test 6 PASS: MRO is correct")

    # Test 7: Fusion prepare calls both parents
    result = fusion.prepare("Biryani")
    assert "veg" in result.lower() and "non-veg" in result.lower(), \
        f"Expected both veg and non-veg in result, got: {result}"
    print(f"Test 7 PASS: fusion.prepare('Biryani') = {result}")

    print(f"\nAll tests passed!")
