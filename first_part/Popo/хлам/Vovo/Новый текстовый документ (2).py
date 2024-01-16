dict_new = {"alica":{"age":"brown"},
            "pusha":{"color":"white"}
            }

dog_1 = dict_new["alica"].get("color")

print(dog_1)

dog_2 = dict_new["pusha"]["color"]

print(dog_2)

dog_3 = dict_new.get("bobik")
if dog_3:
    dog_3 = dog_3.get("color")

print(dog_3)

