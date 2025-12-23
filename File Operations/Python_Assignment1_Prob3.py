#Opening file in W Mode to create and write to a file this method creates file if absent 
f = open("Example.txt",'w')
#Using write() to write to the file newly created above
f.write('This is sample text getting added to the above created file.')
#Closing file since the write operation is done 
f.close()
# Reopening file to check content if added or not in read mode 
f1 = open("Example.txt",'r')
#gradding the file content to a variable after reading it using read()
file_content = f1.read()
#printing the file content to the console
print(file_content)
#Closing the file 
f1.close()