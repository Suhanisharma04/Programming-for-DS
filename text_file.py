## Opening a file
file1 = open("MyFile1.txt","a")
file2 = open(r"MyFile2.txt","w+")

# Closing a file
file1 = open("MyFile.txt","a")
file1.close()

# Ways to read and write data in a file

file1 = open("myfile.txt","w")
L =["This is Delhi \n","This is Paris \n","This is London \n"]

file1.write("Hello \n")
file1.writelines(L)
file1.close()

## Reading from a file
file1 = open("myfile.txt","r+")
print("Output of read function is")
print(file1.read())
print()
file1.seek(0)

print("Output readline function is")
print(file1.readline())
print()
file1.seek(0)

# Difference between read and readline

print("Output of read(9) function is")
print(file1.read(9))
print()
file1.seek(0)
print("Output of readline(9) function is")
print(file1.readline(9))
file1.seek(0)

#readlines function
print("Output of Readlines function is")
print(file1.readlines())
print()
file1.close()

## Appending to a file

file1 = open("myfile.txt","w")
L= ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt","a")
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 =open("myfile.txt","w")
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()

import pandas as pd
dummy_data= {'Name': pd.Series(['james','tom']), 'Age': pd.Series([22,33])}

df = pd.DataFrame(dummy_data)
print(df)
# Writing a csv file
df.to_csv('dummy_data.csv')

#df.pd.read_csv('dummy_data.csv', index_col=0)
df2 = pd.DataFrame(df).T
df2.to_json('dummy_data.json')
print(df2)

#Writing an excel file
df.to_excel('dummy_data.xlsx')

#reading excel file
df = pd.read_excel('dummy_data.xlsx', index_col=0)
print(df)

#JSON file
df = pd.DataFrame(data=dummy_data).T
df.to_json('dummy_data-columns.json')

df.to_json('dummy_data-index.json', orient='index')