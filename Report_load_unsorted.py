def report_load(file_path): # O(n^2)
    name_arr = []
    credit_arr = []

    with open(file_path,'r') as f: 
        next(f) # 1

        for line in f: # n

            row = line.strip().split(',') # 1
            if len(row) < 6: # 1
                continue

            name = row[5].strip() # 1
            credit = float(row[3][0].strip()) # 1
            index = 0

            if name not in name_arr:
                name_arr.append(name)
                credit_arr.append(credit)
            else:
                for i in name_arr:
                    if i == name:
                        credit_arr[index] += credit
                    index +=1
             
    for i in range(len(name_arr)): 
        print("Lecturer : {} | Total Load : {} Credits".format(name_arr[i],credit_arr[i])) 

report_load("CprE_Subject.csv")