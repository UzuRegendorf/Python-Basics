#Read the file and store all the lines in list
#Reverse the list
#Write the reverse list back to the file

with open("test.txt", 'r') as reader:
    content = reader.readlines()   #stored data
    reversed(content)     #reversed
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
