def load_data(file_path):

    global Data, Summary

    with open(file_path, 'r') as f:
        next(f)

        for line in f: #this loop runs n times where n is the number of lines in the file
            
            #row contains [course code, name, type, credit, semester, lecturer]
            row = line.strip().split(',') #this takes O(1) time
            
            #if the row doesn't contain all the required information, skip it
            if len(row) < 6: # 1 
                continue
            
            coursecode = row[0] #1
            name = row[1] #1
            credit = float(row[3][0]) #1
            lecturer = row[5] #1

            if coursecode not in Data: #1
                #Data use course code as key and store name, credit and lecturer in a dictionary
                #this take space O(number of unique courses) and time O(1)
                Data[coursecode] = { #all these operations take O(1) time
                    "Name": name,
                    "Credit": credit,
                    "Lecturer": [lecturer]
                }
            #if the lecturer is not in the list of lecturers for the course, add it to the list
            elif lecturer not in Data[coursecode]["Lecturer"]:
                Data[coursecode]["Lecturer"].append(lecturer)

            if lecturer not in Summary: # 1
            #summary use lecturer as key and store total load in a dictionary
                Summary[lecturer] = 0.0 # this take space O(number of unique lecturers) and time O(1)
            Summary[lecturer] += credit # 1
            

#So data loading takes O(n) time where n is the number of lines in the file.
#while it take space O(m) where m is the number of unique lecturers in the file.
Data = {}
Summary = {}
load_data("CprE_Subject.csv")