import Report_load as rl
import Database as db

Data = db.Data
Summary = db.Summary

while True:
    i = (input(">>")).strip().split()
    
    if i[0] == "report_load":
        rl.report_load(Summary)
    elif i[0] == "find_course":
        pass
    else:
        print("This function don't exist")