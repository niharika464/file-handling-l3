with open('sample.txt', 'w') as file:
    file.write("I like eating strawberies with nutela chocolate...")
    file.close()

with open('sample.txt', 'r') as file1:
    data=file1.readlines()
    print("I am gonna split the words of my file..")
    for line in data:
        word=line.split()
        print(word)

file1.close()           