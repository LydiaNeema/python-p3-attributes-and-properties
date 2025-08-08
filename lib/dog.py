class Dog:
    approved_breeds = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name=None, breed=None):
        if name is not None:
            self.name = name  # Will trigger setter
        if breed is not None:
            self.breed = breed  # Will trigger setter

    # name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
