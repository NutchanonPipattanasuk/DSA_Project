# DSA_Project
''''''''
for search algorithm 
if we using dict when we create database we also creat dict call data
where its key is course_code so when we find course we access it from key
which take time complexity of O(1) to access
while using array you need to make loops to access from idex
worst case is course_code is in the last index so it take O(n) 
'''''''''

'''''''''
for report load 
If we use a dictionary, we can take data from a CSV file and create a dictionary named 'summary', with 'lecturer' as the key and 'credit' as the value. We need to check if 'lecturer' already exists. If not, we set its value to 0. If it does exist, we simply add 'credit' so it take O(1). This function then takes the data from 'summary' and prints it so it take O(n).
'''''''''