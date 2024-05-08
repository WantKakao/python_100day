# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="w") as file:
#     file.write("\nKarina is so cute")

with open("my_file.txt", mode="a") as file:
    file.write("\nKarina is so cute")
    content = file.read()
    print(content)