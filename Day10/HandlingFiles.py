# Example 1 Writing data to file
# file = open("C:/DemoFile/Myfile.txt",'w')
# file.write("its my first statement...\n")
# file.write("its my second statement..\n")
# file.write("its my third statement...\n")
# file.write("its my forth statement...\n")
# file.write("its my fifth statement...\n")
#
# file.close()
# print("Programming Completed.....")

# Example 2  Read data from file

# file = open("C:/DemoFile/Myfile.txt",'r')
# print(file.read())
# file.close()

# file = open("C:/Users/Admin/Downloads/pom.txt",'r')
# print(file.read())
# file.close()


# ###Example 2  Appending data into text  file
#
# file = open("C:/DemoFile/Myfile.txt",'a')
# file.write("its my sixth statement...\n")
# file.write("its my eight statement...\n")
# file.write("its my ninth statement...\n")
#
# file.close()
# print("Program is completed")


###Example 5  Appending data into text  file

file = open("C:/DemoFile/Myfile.txt",'r')

for i in file :
    print(i)

