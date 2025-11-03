
# this finction will return sum and average of salaries of your employees
def total_salary(path):
    try:   # check if path and file exist
        with open(path,"r") as sl:                                     # open for read file
            workers=[el.strip().split(',') for el in sl.readlines()]   # add each line to list of workers
            if not workers:                                            # exception if file is empty or contains not expected values 
                print("File is empty or not correct")
                return None
            workers_salaries=[float(row[-1]) for row in workers]       # we only need salaries, so add to a list second value in a row
            total_sal=sum(workers_salaries)                            # calculate total salary
            aver_sal=total_sal/len(workers_salaries)                    # calc average salary
            summary=(total_sal,aver_sal) if len(workers_salaries)!=0 else print("You have no workers!") #add them to a tuple and check for zero division
        return summary
    except FileNotFoundError:
        print ("File does not exist")                                   # if path does not exist

tuple_salaries=total_salary("salaries.txt")
print(f"Total salary is {tuple_salaries[0]}, Average salary is {tuple_salaries[1]}")