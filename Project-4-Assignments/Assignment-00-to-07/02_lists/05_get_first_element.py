def get_first_element(list):
    print(list[0])
    
def get_list():
    list = []
    elem:str = input("Enter an element to add to the list:")
    while elem != "":
        list.append(elem)
        elem = input("Enter an element to add to the list:")
    return list

def main():
    list = get_list()
    get_first_element(list)
if __name__ == "__main__":
    main()
    