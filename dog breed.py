class animal():
     def __init__(self,specie,breed):
          self.specie = specie
          self.breed = breed
my_animal = animal("animal","germanSheperd,pitbull")
print(f"Dog is {my_animal.specie} and have many breeds like {my_animal.breed} ")