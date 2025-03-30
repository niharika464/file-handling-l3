with open('sample.txt', 'w') as file:
    file.write("AI is the most powerful weapon to change the world...")
    file.close()

with open('sample.txt', 'r') as file1:
    data=file1.readlines()
    print("I am doing my after class project...")
    for line in data:
        word=line.split()
        print(word)

file1.close()           