from labtop import Labtop


# display
def display_labtop():
    if len(my_labtop) ==0:
        print("\nYou had no labtop data.\n")
    else:
        num = 1
        print(f'You had {len(my_labtop)} following:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_laptop()
            num +=1
        print("\n")

# option
def display_option():
    print("Welcome to Labtop Data Store System (LDSS)")
    print("1.Add Labtop")
    print("2.Display all Labtop")
    print("3.Delete labtop")
    print("4.Edit Labtop Price")
    print("5.exit")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_labtop_data()
    elif select==2:
        display_labtop()
    elif select==3:
        delete_labtop()
    elif select==4:
        edit_labtop_price()
    elif select ==5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

def edit_labtop_price():
    print("Which one do you want to edit price?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_price()}')
            newprice = float(input("enter new price: "))
            my_labtop[s-1].set_price(newprice)
            print("\nLaptop price updated.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")


# delete data
def delete_labtop():
    print("Which one do you want to remove?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete laptop data.\n")
            break
        elif s ==0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")
# input data
def input_labtop_data():
    brand = input("Enter labtop brand: ")
    model = input("Enter labtop model: ")
    cpu = input("Enter labtop cpu: ")
    ram = int(input("Enter labtop ram:"))
    display= float(input("Enter display size: "))
    storage= int(input("Enter size of storage: "))
    price = float(input("Enter price: "))

    l = Labtop("","","",0,0,0,0)


    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)
    #return brand,model,color,maxspeed,price # return as tuple
    #my_labtop.append(Labtop(brand,model,cpu,ram,display,storage,price))
    my_labtop.append(l)
    print("\n-----------------------------------")
    print("Already add Labtop to store.")
    print("\n-----------------------------------")

my_labtop = []
my_labtop.append(Labtop("ASUS","Vivobook","Intel Core i5-12500H",8,15.6,512,27990))
my_labtop.append(Labtop("Lenovo","IdeaPad Gaming 3","Intel Core i5-11320H",8,15.6,512,25990))
s = 0
while s == 0:
    display_option()




