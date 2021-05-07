file = open("chocolate.txt", "w")
file.write("i'm writing chocolate in this txt document\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line2\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line3\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line4\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line5\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line6\n")
file.close()

file2 = open("chocolate.txt", "a")
file2.write("i'm appending to line7\n")
file.close()

readme = open("chocolate.txt", "r")
read = readme.read()
file.close()
print(read)

