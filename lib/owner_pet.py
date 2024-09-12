
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type_input):
        if pet_type_input in Pet.PET_TYPES:
            self._pet_type = pet_type_input
        else: 
            raise Exception


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [p for p in Pet.all if p.owner is self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)