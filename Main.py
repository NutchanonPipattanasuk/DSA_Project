import Report_load as rl
import Database as db
import search as sc

Data = db.Data
Summary = db.Summary

while True:
    i = (input(">>")).strip().split()
    
    if i[0] == "report_load":
        rl.report_load(Summary)
    elif i[0] == "find_course":
        sc.find_course(i[1])
    elif i[0] == "exit":
        print("Exiting...")
        break
    else:
        print("This function don't exist")