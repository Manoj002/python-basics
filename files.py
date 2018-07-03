file = open("example.txt", "r");
content = file.read();
print(content);

file2 = open("example2.txt", "w");
file2.write("Heyy there!");
file.close()
file2.close()

