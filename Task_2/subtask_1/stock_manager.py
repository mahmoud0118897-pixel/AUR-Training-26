
def add_stock():
    dec={}
    try:
        with open("stock.txt", "r") as f:
            for line in f:
                data=line.strip()
                key , value = data.split(",")
                dec[key]=value
        for index ,(key, value) in enumerate(dec.items(), 1):
            print(f"{index}. {key}: {value}")            
    except OSError:
        print("Error occurred while opening the file.")

    print("enter the stock name or id to add : ")
    x=input()
    if type(x) is str : 
            if x.isalpha():
                x=x.lower()
                if not (x in dec):
                    dec[x]=0    
            elif x.isdigit() :
                if int(x)>0:
                    x=int(x)
                    l=list(dec.keys())
                    if x>len(l):
                        print("Invalid input. Please enter a valid stock id.")
                        return
                    else:
                        x=l[x-1]
            else:
                print("Invalid input. Please enter a positive number.")
                return
    print("enter the stock value to add : ")
    y=input()
    if y.isdigit() and int(y)>0:
        y=int(y)
    else:
        print("Invalid input. Please enter a positive number.")
        return
    dec[x]=str(int(dec[x])+y)
    print(f"Stock '{x}'. New value: {dec[x]}")
    with open("stock.txt", "w") as f:
        for key, value in dec.items():
            f.write(f"{key},{value}\n")
    print("Stock updated successfully.")
    f.close()
def remove_stock():
    dec={}
    try:
        with open("stock.txt", "r") as f:
            for line in f:
                data=line.strip()
                key , value = data.split(",")
                dec[key]=value
        for index ,(key, value) in enumerate(dec.items(), 1):
            print(f"{index}. {key}: {value}")            
    except OSError:
        print("Error occurred while opening the file.")
    print("enter the stock name or id to remove : ")
    x=input()
    if type(x) is str :
        if x.isalpha():
                x=x.lower()
                if not (x in dec):
                    print("Stock not found.")
                    return
        elif x.isdigit() :
                if int(x)>0:
                    x=int(x)
                    l=list(dec.keys())
                    if x>len(l):
                        print("Invalid input. Please enter a valid stock id.")
                        return
                    else:
                        x=l[x-1]
                else:
                    print("Invalid input. Please enter a positive number.")
                    return
    print("enter the stock value to remove : ")
    y=input()
    if y.isdigit() and int(y)>0:
        y=int(y)
    else:
        print("Invalid input. Please enter a positive number.")
        return
    if x in dec:
        if int(dec[x]) >= y:
            dec[x] = str(int(dec[x]) - y)
        else:
            print("Insufficient stock.")
            return
    with open("stock.txt", "w") as f:
        for key, value in dec.items():
            f.write(f"{key},{value}\n")
    print("Stock updated successfully.")
    print("done")
    f.close()
def show_stock_components():
    dec={}
    try:
        with open("stock.txt", "r") as f:
            for line in f:
                data=line.strip()
                key , value = data.split(",")
                dec[key]=value
        for index ,(key, value) in enumerate(dec.items(), 1):
            print(f"{index}. {key}: {value}")            
    except OSError:
        print("Error occurred while opening the file.")
def main():
    while True:
        print("____menu____")
        print("enter : 1. Add stock")
        print("enter : 2. Remove stock")
        print("enter : 3. show stock components")
        print("enter : 4. Exit the program")
        try :
            x=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        if x<1 or x>4:
            print("Invalid choice")
            main()
        elif x==1:
         
            add_stock()
            main()
        elif x==2:
            remove_stock()
            main()
        elif x==3:
            show_stock_components()
            main()
        elif x==4:
            print("Exiting the program...")
            exit()
if __name__ == "__main__":
    main()
