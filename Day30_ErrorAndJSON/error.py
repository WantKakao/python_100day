# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# v = a_dictionary["non_existent_key"]
# v = a_dictionary.get("non_existent_key") 로 해결 가능

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# t = text + 5

# try:
#     print(5)
#     a = [1, 2, 3]
#     print(a[3])
# except IndexError as error:
#     print(error)
# else:
#     print(3)
# finally:
#     print(2)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("You are not Human")

bmi = weight / height ** 2
print(bmi)