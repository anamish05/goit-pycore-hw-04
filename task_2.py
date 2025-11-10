# comment to mentor - I just wanted to practice around **kwargs to understand it better, so I included it. Hope will not affect the mark:)
# this function is to create a dictionary of a cat
def create_cat(**kwargs):
    return {'id':kwargs.get('id'),'name':kwargs.get('name'),'age':kwargs.get('age')}

#This function reads the file about cats and returns a cats dictionaries list
def get_cats_info(path:str) -> list[dict]:
    cats_list=[]    # creating an empty list
    try:
        with open(path,'r') as file:     #reading a file with cats info
            for l in file:
                id, name, age=l.strip().split(',')  #reading each element of a line and adding them to variables
                cat_dict=create_cat(id=id,name=name,age=age)  #creating a cat dictionary using a user defined function
                cats_list.append(cat_dict)                      # adding a dictionary to a list
            return cats_list
    except FileNotFoundError:
        print('File does not exist! You have no cats it seems')
        return []

my_cats=get_cats_info('cats.txt')
print(my_cats)
