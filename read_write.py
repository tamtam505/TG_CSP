# TG Reading and Writing to Files

# with open they are the keywords to open a file
# paranthesis means it is a function
# File Path
# "r" we can read the file -> r equals read
# as file-> is name of file in code
# content = the method is able to read the file/gives what is written on the file 
# w stands for write-> replaces the content
# r stands for read
# a stands for append-> adds content to the end

with open("practice.txt","r+") as file: # "r+" lets you read and write
    content = file.read()
    content = "Chapter 1:\n" + content + " And Christopher Robin was sitting on his doorstep putting on his big boots" 
    file.write(content)

    with open("practice.txt", "a") as file:
      file.write("\nWinnie the Pooh and the Blustery Day.")