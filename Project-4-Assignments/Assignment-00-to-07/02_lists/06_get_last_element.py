def get_last_element(lst):
    print(lst[-1])
    
def get_list():
    lst = []
    elem:str = input("Enter an element to add to the list:")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element to add to the list:")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)
    
if __name__ == "__main__":
    main()
