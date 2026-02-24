def report_load(file_path):
    sum = {}

    with open(file_path,'r') as f:
        next(f)

        for line in f:

            row = line.strip().split(',')
            if len(row) < 6:
                continue

            name = row[5].strip()
            credit = float(row[3][0].strip())
            if name not in sum:
                sum[name] = 0.0
            sum[name] += credit
    
    for key in sum:
        print("Lecturer : {} | Total Load : {} Credits".format(key,sum[key]))

report_load("CprE_Subject.csv")