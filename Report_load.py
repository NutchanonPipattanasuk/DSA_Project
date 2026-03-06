def report_load(summary): # O(n)
    
    for key in summary: # m | m<=n
        print("Lecturer : {} | Total Load : {} Credits".format(key,summary[key])) # 1
