list1 = [1, 2.4, "hello", ["and", "or", 1, 2.5]]
print(list1);

print(type(list1))


for item in list1:
    if(isinstance(item, list)):
        for tht in item:
            print(tht)
    else:
        print(item)

print("******Next Example***********");

for item in list1:
    if(type(item) == int):
        product = item * 10;
        print(product);
    elif type(item) == float:
        product = item * 100;
        print(product)
    else:
        print("Not int and not float");
