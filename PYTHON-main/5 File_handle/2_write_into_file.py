'''
1. To do write operation on file we have to open a file with 'w' mode
2. If you open a file with write mode if file is not exist it will crate a new file, if file is exist it will remove old data and write new data.

'''

fw = open('write_names.txt', 'w')

# To write data into file
fw.write('Hi Kumar\n')
fw.write('How are you')

# To close a file
fw.close()