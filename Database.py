def load_data(file_path):

    global Data, Summary

    with open(file_path, 'r') as f:
        next(f)

        for line in f:

            row = line.strip().split(',')
            
            if len(row) < 6:
                continue
            
            coursecode = row[0]
            name = row[1]
            credit = float(row[3][0])
            lecturer = row[5]

            if coursecode not in Data:
                Data[coursecode] = {
                    "Name": name,
                    "Credit": credit,
                    "Lecturer": [lecturer]
                }
            elif lecturer not in Data[coursecode]["Lecturer"]:
                Data[coursecode]["Lecturer"].append(lecturer)

            if lecturer not in Summary: # 1
                Summary[lecturer] = 0.0 # 1
            Summary[lecturer] += credit # 1



Data = {}
Summary = {}

load_data("CprE_Subject.csv")