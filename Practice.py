import sys
from functools import reduce, partial
from Encrypt_password_ import get_decrypted_password

## Discount By price
an = 0
if an == 1:
    purchased_amount = 1500
    Gst = purchased_amount * 0.18
    Discount_perc = 0.1
    Fixed_amount = 1300
    Total_amount = purchased_amount + Gst
    if Total_amount > Fixed_amount:
        Discount_amount = Total_amount * Discount_perc
        Total_amount -= Discount_amount
        print('Round of ', round(Total_amount))

## Discount By Age
an = 0
if an == 1:
    age = int(input('Enter the age :'))
    purchased_amount = float(input('Enter the purchased amount :'))
    Gst = purchased_amount * 0.18
    Discount_perc = 0.1
    Fixed_amount = 2000
    Total_amount = purchased_amount + Gst
    if age > 60 or age <= 18:
        Discount_amount = Total_amount * Discount_perc
        Total_amount -= Discount_amount
    print('Total amount : ', Total_amount, '\nRound of :', round(Total_amount))

# Discount by age and price
an = 0
if an == 1:
    age = int(input('Enter the age :'))
    purchased_amount = float(input('Enter the purchased amount :'))
    Gst = purchased_amount * 0.18
    Discount_perc = 0.1
    Fixed_amount = 2000
    Discount_amount = 0
    Total_amount = purchased_amount + Gst
    if age > 60 or age <= 18:
        if Total_amount > Fixed_amount:
            Discount_amount = Discount_amount + Total_amount * Discount_perc
            Total_amount -= Discount_amount
    print('Purchased  amount : ', purchased_amount, '\nGst amount :', Gst, '\nTotal amount : ', Total_amount,
          '\nDiscount amount : ', Discount_amount, '\nRound of :', round(Total_amount))

# Input Handling(Create customer id for new Customer)
an = 0
if an == 1:
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    phone_number_last_4digit = sys.argv[3]
    customer_id = first_name.lower().replace(" ", "") + last_name.lower().replace(" ",
                                                                                  "_") + phone_number_last_4digit + "@myshop"
    print('First name : ', first_name)
    print('Last name :', last_name)
    print('Last 4 digit ph nmbr :', phone_number_last_4digit)
    print('Customer id : ', customer_id)

# Input Handling(Create customer id for new Customer)
an = 0
if an == 1:
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print("Please fill the first name,last name and last 4 digit ")
        sys.exit()

    first_name = sys.argv[1]
    last_name = sys.argv[2]
    phone_number_last_4digit = sys.argv[3]
    customer_id = first_name.lower().replace(" ", "") + last_name.lower().replace(" ",
                                                                                  "_") + phone_number_last_4digit + "@myshop"
    print('First name : ', first_name)
    print('Last name :', last_name)
    print(len(sys.argv))
    print('Last 4 digit ph nmbr :', phone_number_last_4digit)
    print('Customer id : ', customer_id)

# Input Handling(Create customer id for new Customer)
an = 0
if an == 1:
    new_customer = "".join(sys.argv[1:])  ## join all input..it can take all input no limits
    ## only run on terminal ...python Practice.py arfas khan 4584 ...Here,index 0 is .py file ,index 1 is arfas..etc....
    # .py is not input so we avoid index 0 ,So we put sys.argv[1:]...
    transform_data = new_customer.lower().replace(' ', '.') + '@myshop'
    print(transform_data)

# String handling
an = 0
if an == 1:
    customer_name = "  arfas khan  "
    mobile_num = "8870254584"
    # Lower,upper,capitalize,strip,title
    print('Lower of : ', customer_name.lower())  # change all letter in lower case
    print('Upper of : ', customer_name.upper())  # Change all letter in upper case
    print('Capitalize of :', customer_name.capitalize())  # Change the first letter in the first word as Capital
    print('Strip of :', customer_name.strip())  # it remove unwanted indent(space)
    print('Title of :', customer_name.title())  # change the first letter of all words as capital

    # mask the number
    masked_phnmbr = mobile_num[:2] + "******" + mobile_num[-2:]  ## masked the number
    print('Masked number : ', masked_phnmbr)

    # Replace
    item = 'Sugar'
    replaced_item = item.replace('Sugar', 'Jaggery Powder')  ## replace the word
    print(replaced_item)

    # split
    words = 'Choclate section is placed on a 4th section from here'
    len_words = len(words.split())
    print(len_words)

    # Find the index start from
    ind_words = words.find('placed')  # p is in index 20..it gives the first letter index
    print(ind_words)

    # Neeed First letter from all name(firstname,lastname,surname) should be upper
    username = 'arfas khan dasthagir'
    frst_letter = ([words[0].upper() for words in username.split()])
    print(frst_letter)
    print("".join(
        frst_letter))  # this line join all the  frst letter of name without space ..if need space betwwen each letter...Put space in " ".join

#get a otp number
an = 0
if an == 1:
    message_otp = "Your otp is 77889.Please keep it safe"
    otp_ = message_otp.split('is')[1].split('.')[0]
    print(otp_.strip())

# get a coupon code...if coupon match with our fixed coupon code...then apply discount...if not match no discount
an = 0
if an == 1:
    coupon_codde = "myshop100"
    msg_coupon = 'Congratulations!...Your coupon code is myshop100...Please use this to get discount'
    Coupon_ = msg_coupon.split('is')[1].split('.')[0].strip()
    if Coupon_ == coupon_codde:
        print('Discount applied')
    else:
        print('No Discount')

## Discount on saturday and sunday...or coupon code must...and must be purcahed price more than 2000
an = 0
if an == 1:
    coupon_code = "myshop500"  #"myshop100"
    Day = 'Saturday'  #'Monday'
    fixed__price = 2000
    purchased_amount = 2001
    fixed_day = ["Saturday", "Sunday"]
    msg_coupon = 'Congratulations!...Your coupon code is myshop100...Please use this to get discount'
    Coupon_ = msg_coupon.split('is')[1].split('.')[0].strip()
    if Coupon_ == coupon_code:
        if purchased_amount > fixed__price:
            print('You have coupon and purchased more than 2000 ....Discount applied')
        else:
            print('You have coupon and but purchased lower than 2000 ....No Discount')
    elif Day in fixed_day:
        if purchased_amount > fixed__price:
            print('You purchased in a perfect day and purchased more than 2000....Discount applied')
        else:
            print('You purchased in a perfect day  but purchased lower than 2000 ....No Discount')
    elif purchased_amount > fixed__price:
        print('You purchased more than 2000..But you are not in a perfect day and you dont have coupon')

    else:
        print(
            'You dont have coupon and you not purchased more than 2000 and you purchased in an ordinary day ....No discount')

# While
an = 0
if an == 1:
    correct_customer_id = '2232'
    enter_id = ''
    while enter_id != correct_customer_id:
        enter_id = input('Enter correct id :')
    print('Thankyou')

# break
an = 0
if an == 1:
    for i in range(10):
        if i == 7:
            break
        print(i)

# continue
an = 0
if an == 1:
    lst_nmbr = [1, 6, 3, 5, -1, -6, -3, 0, 7]
    for i in lst_nmbr:
        if i < 0:
            continue
        print(i)

# While,count...break the loop or print something,when count < 0
an = 0
if an == 1:
    count = 5
    while count > 0:
        count -= 1
        print(count)
    print('Your time is up')

# While,count ..break the rule ,when count is 18
an = 0
if an == 1:
    count = 0
    while True:
        if count == 18:
            break
        count += 1
        print(count)
    print('Matched')

# Whikle and if
an = 0
if an == 1:
    items_added = []
    while True:
        items = input('Enter the items to add in a cart :')
        items = items.lower()
        if items == 'done':
            break
        items_added.append(items)
    print(items_added)

# function
an = 0
if an == 1:
    def add(a, b):
        print(a + b)


    add(1, 2)


    def add(a, b):
        return a + b


    summ_ = add(1, 2)
    print(summ_)

# function(*args means it takes all input,no limits.....
an = 0
if an == 1:
    def count_(*args):
        count = 0
        for i in args:
            count += i
            print(count)


    count_(1, 2, 34, 67)

# function(**kwargs means it has keys and values...it takes all inputs
an = 0
if an == 1:
    def user_(**kwargs):
        for key, value in kwargs.items():
            print(f"{key} - {value}")


    user_(name="Arfas", phnum=8870254584, age=25, gender='Male')

# List Method....List is mutable
an = 0
if an == 1:
    Playlist = ['Kannadi poove', 'rabta', 'rabta', 'Naa ready', 'Aaluma doluma']
    # append
    Playlist.append('Naan parayan alla')
    print('Append :', Playlist)

    # Insert
    Playlist.insert(2, 'GBU mamey')
    print('Insert :', Playlist)

    # Remove
    Playlist.remove('Naa ready')
    print('Remove : ', Playlist)

    #Pop
    Playlist.pop()
    print('Pop : ', Playlist)

    # reverse
    Playlist.reverse()
    print('reverse : ', Playlist)

    # count
    print('Count : ', Playlist.count('rabta'))  # it returns 2 ..because 2 rabta in playlist

# String slicing
an = 0
if an == 1:
    Playlist = ['Kannadi poove', 'rabta', 'rabta', 'Naa ready', 'Aaluma doluma']

    frst_2 = Playlist[:2]
    print(frst_2)

    last_2 = Playlist[-2:]
    print(last_2)

    second_thrd = Playlist[2:4]
    print(second_thrd)

# List iteration
an = 0
if an == 1:
    food = ['Dosa', 'Briyani', 'Idly', 'Parotta']
    person = ['Arfas', 'Thangam', 'Vijay', 'Peer']
    for item, pers in zip(food, person):
        print(f"{item} is favourite food of {pers}")

# neeed to change the item in food
an = 0
if an == 1:
    food = ['Dosa', 'Briyani', 'Idly', 'Parotta']
    food[2] = 'Burger'
    print(food)

# enumerate
an = 0
if an == 1:
    food = ['Dosa', 'Briyani', 'Idly', 'Parotta']
    for i, item in enumerate(food):
        print(f"{i} {item}")  ## i return index of item , item return food one by one

# Tuples is immutable..We can use tuple for only read purpose and if we need extract any information..it allows...if we want to change in tuples..its not possible
an = 0  #  when we use tuple...if we dont want to change the data ,use tuples...any possiilities to change data in any situation use list
if an == 1:
    food = ('Dosa', 'Briyani', 'Idly', 'Parotta')
    person = ('Arfas', 'Thangam', 'Vijay', 'Peer')
    for item, pers in zip(food, person):
        print(f"{item} is favourite food of {pers}")
    for i, item in enumerate(food):
        print(f"{i} {item}")
    curr_ = food[2]
    print(curr_)

    print(food.count('Briyani'))
    print(food.index('Idly'))

# Set
# Set uses curly braces not dictionary....Set is mutable but we cant update..If we want to update...frst remove and then add....
# Dictionary also use same curly braces but it neeed key and value pair...But Set dont need that....
# Mainly, Set remove duplicates...and we cant eextract using index...set has not index....it return in unorderd...
an = 0
if an == 1:
    a = {1, 2, 3}
    b = {'Chennai', 'Andhra', 'Banglore', 'Kanyakumari', 'Chennai', 'Kerala'}
    c = {'Kochin', 'Delhi', 'Kanyakumari', 'Trichy', 'Madurai'}

    print(
        b)  # it returns only Chennai,Andhra,Banglore,Kanyakumari,kerala.....Chennai placed 2 time is a set.....it remove duplicates and return

    print(b.union(c))

    print(b.intersection(c))

    print(b.difference(c))  # it returns unmatched cities only in b....

    print(c.difference(b))  # it return unmatched cities only ion c....because c comes first.....

    print(a.remove(2))

    print(a.add(5))

    print(a.discard(
        7))  ## it dont return error,if 7 is not in set....if you use remove 7 in set..But 7 is not in set...it returnns error..thats why use discard

# Dictionary
# Use curly braces but key and value pair is must..Ex..{name , 'Arfas'}
# it wont allow duplicate vaaluees.....
an = 0
if an == 1:
    things = {
        'Item': 'Rice',
        'Variety': 'Basmati',
        'Quantity': 5,
        'Price': 400
    }

    print(things["Variety"])
    # print(things["Basmati"]) # it shows errror..because i search using values...extract using key is possible.....

    print(things.get("Variety"))
    # print(things.get("Basmati")) # same meaning,but it dont show error.....instead, this show None...using this to avoid code kill...

    print(things.keys())

    print(things.values())

    things.update({"Type": "Loose"})
    print(things)

    for key, value in things.items():
        print(f"{key} : {value}")

    things.pop('Type')
    print(things)

    things_ = {
        'Item': 'Rice',
        'Variety': 'Basmati',
        'Quantity': 5,
        'Price': 400,
        'Item': 'Brown Rice'
    }

    print(
        things_)  ## This Item key is 2 time....it avoid dupplicates...So it takes lastly updated key and values only take.....

    things_.update({
        'Quantity': 3})  ## if the upated key is new in dict...it added....But if we update already existed key,it will relace the old value....

    print(things_)

    things1 = {
        'Item': 'Rice',
        'Variety': ['Basmati', 'pulungal', 'paccharisi'],
        'Quantity': 5,
        'Price': 400
    }

    for k, v in things1.items():
        print(f"{k} : {v}")

    for items_ in things1['Variety']:
        print(items_)

    things_2 = {
        "Rice": {'Item': 'Rice', 'Variety': 'Basmati', 'Quantity': 5, 'Price': 400},
        "Sugar": {'Item': 'Sugar', 'Variety': 'White', 'Quantity': 2, 'Price': 100},
        "Milk": {'Item': 'Milk', 'Variety': 'Skimmed', 'Quantity': 3, 'Price': 240}
    }

    for k, v in things_2.items():
        print(k)
        if k == 'Milk':
            print(f"The price of your {v['Quantity']}ltr {v['Variety']} {v['Item']} is {v['Price']}")
        else:
            print(f"The price of your {v['Quantity']}kg {v['Variety']} {v['Item']} is {v['Price']}")

# Class
# a class is a blueprint or template for creating objects
# A class is like an architect’s plan for a house.
# An object is the actual house built from that plan
# A class defines the attributes (data) and methods (functions) that the objects created from the class will have.
an = 0
if an == 1:
    class house:
        def __init__(self, sqr_ft_room1, sqr_ft_room2, sqr_ft_hall, cot1, cot2, bathroom1, bathroom2, bathroom3, Ac,
                     furnished, Tv, kitchen_type, sofas, fan1, fan2, fan3, Garden, bike, car):
            self.sqr_ft_room1 = sqr_ft_room1
            self.sqr_ft_room2 = sqr_ft_room2
            self.cot1 = cot1
            self.cot2 = cot2
            self.bathroom1 = bathroom1
            self.bathroom2 = bathroom2
            self.bathroom3 = bathroom3
            self.Ac = Ac
            self.furnished = furnished
            self.Tv = Tv
            self.kitchen_type = kitchen_type
            self.sofas = sofas
            self.sqr_ft_hall = sqr_ft_hall
            self.fan1 = fan1
            self.fan2 = fan2
            self.fan3 = fan3

            self.Garden = Garden
            self.bike = bike
            self.car = car

        # methods
        def Room1(self):
            Room_size = self.sqr_ft_room1
            cot_ = self.cot1
            bathroom = self.bathroom1
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan1

            print(
                f"This is the {Room_size} square feet bedroom.we can put {cot_},{Ac} ,{fan} and it is {furnished}..This room has {bathroom} bathroom")

        def Room2(self):
            Room_size = self.sqr_ft_room2
            cot_ = self.cot2
            bathroom = self.bathroom2
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan2

            print(
                f"This is the {Room_size} square feet bedroom.we can put {cot_},{Ac},{fan} and it is {furnished}..This room has {bathroom} bathroom")

        def hall(self):
            Room_size = self.sqr_ft_hall
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan3
            Tv = self.Tv
            sofas = self.sofas

            print(
                f"This is the {Room_size} square feet Hall.we can put {sofas},{Ac},{fan} and {Tv} , it is {furnished}..")

        def Kitchen(self):
            kitchen_type = self.kitchen_type
            print(f"Kitchen is completely a {kitchen_type}")

        def car_parking(self):
            car = self.car
            bike = self.bike
            print(f"we can park {car} and {bike} in a parking area.")

        def backyard(self):
            Grden = self.Garden
            bathroom = self.bathroom3
            print(f"Beatiful garden area with {Grden}..and it has {bathroom} bathroom")


    # objects
    home = house(240, 140, 400, 'King size cot', 'Medium size cot', 'western', 'western', 'Indian', '1.5 ton AC',
                 'Fully Furnished', '55 inch Tv', 'Modular kitchen', 'Corner Sofa', '1 fan', '1 fan', '2 fans',
                 'Roses and color plant', '2 bikes', '1 car')
    home.Room1()
    home.Room2()
    home.hall()
    home.Kitchen()
    home.car_parking()
    home.backyard()

an = 0
if an == 1:
    class house:
        def __init__(self, sqr_ft_room, cot, bathroom, Ac,
                     furnished, Tv, kitchen_type, sofas, fan, Garden, bike, car):
            self.sqr_ft_room = sqr_ft_room
            self.cot = cot
            self.bathroom = bathroom
            self.Ac = Ac
            self.furnished = furnished
            self.Tv = Tv
            self.kitchen_type = kitchen_type
            self.sofas = sofas
            self.fan = fan
            self.Garden = Garden
            self.bike = bike
            self.car = car

        # methods
        def Room1(self):
            Room_size = self.sqr_ft_room
            cot_ = self.cot
            bathroom = self.bathroom
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan

            print(
                f"This is the {Room_size} square feet bedroom.we can put {cot_},{Ac} ,{fan} and it is {furnished}..This room has {bathroom} bathroom")

        def Room2(self):
            Room_size = self.sqr_ft_room
            cot_ = self.cot
            bathroom = self.bathroom
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan

            print(
                f"This is the {Room_size} square feet bedroom.we can put {cot_},{Ac},{fan} and it is {furnished}..This room has {bathroom} bathroom")

        def hall(self):
            Room_size = self.sqr_ft_room
            Ac = self.Ac
            furnished = self.furnished
            fan = self.fan
            Tv = self.Tv
            sofas = self.sofas

            print(
                f"This is the {Room_size} square feet Hall.we can put {sofas},{Ac},{fan} and {Tv} , it is {furnished}..")

        def Kitchen(self):
            kitchen_type = self.kitchen_type
            print(f"Kitchen is completely a {kitchen_type}")

        def car_parking(self):
            car = self.car
            bike = self.bike
            print(f"we can park {car} and {bike} in a parking area.")

        def backyard(self):
            Grden = self.Garden
            bathroom = self.bathroom
            print(f"Beautiful garden area with {Grden}..and it has {bathroom} bathroom")


    # objects
    room1 = house(240, 'King size bed', 'Western', '1.5 ton AC', 'Fully furnished', 0, 0, 0, '1 fan', 0, 0, 0)
    room1.Room1()
    room2 = house(140, 'Medium size bed', 'Western', '1.5 ton AC', 'Fully furnished', 0, 0, 0, '1 fan', 0, 0, 0)
    room2.Room2()
    hall_ = house(400, 0, 0, '1.5 ton AC', 'Fully furnished', '55 inch TV', 0, 'Corner Sofa', '2 fan', 0, 0, 0)
    hall_.hall()
    kitchen_ = house(0, 0, 0, 0, 0, 0, 'Modular Kitchen', 0, 0, 0, 0, 0)
    kitchen_.Kitchen()
    parking = house(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '2 bikes', '1 car')
    parking.car_parking()
    garden = house(0, 0, 'Indian', 0, 0, 0, 0, 0, 0, 'Roses and money plant', 0, 0)
    garden.backyard()

## Inheritance##
## Inheritance allows you to reuse code from an existing class (parent) instead of writing it again in a new class (child).
# You don’t need to “kill” or rewrite the existing class.
# You can safely override, extend, or modify using inheritance.
# Single Inheritance
an = 0
if an == 1:
    class dad:
        def house(self):
            print(f"4 bhk luxuries house")

        def shop(self):
            print(f"Restaurent")


    class son(dad):
        def salaried(self):
            print(f"Monthly salary : 1L")


    property = son()
    property.house()
    property.shop()
    property.salaried()

# Multiklevel Inheritance
an = 0
if an == 1:
    class grandfather:
        def land(self):
            print(f"5 acres land")

        def estate(self):
            print(f"50 acres tea estate")


    class dad(grandfather):
        def house(self):
            print(f"4 bhk luxuries house")

        def shop(self):
            print(f"Restaurent")


    class son(dad):
        def salaried(self):
            print(f"Monthly salary : 1L")


    property = son()
    property.land()
    property.shop()
    property.estate()
    property.house()
    property.salaried()

# Hierarchy
an = 0
if an == 1:
    class dad:
        def house(self):
            print(f"4 bhk luxuries house")

        def shop(self):
            print(f"Restaurent")


    class son1(dad):
        def shop2(self):
            print(f"Tea shop")


    class son2(dad):
        def shop3(self):
            print(f"Jewelley shop")


    property1 = son1()
    property2 = son2()
    property1.house()
    property1.shop()
    property1.shop2()
    property2.house()
    property2.shop()
    property2.shop3()

# Multipole inheritence
an = 0
if an == 1:
    class dad:
        def house(self):
            print(f"4 bhk luxuries house")


    class mom:
        def land(self):
            print(f"5 acres of land")


    class son(dad, mom):
        def shop(self):
            print(f"Tea shop")


    property = son()
    property.house()
    property.shop()
    property.land()

## Hybrid...It include, multilevel and multiple,single and hierarchy...any possiblities..include more type of inheritance in single inheritance is hybris....
## In real time, hardly to use hybrid, now we avoid....will see in future....


# Polymorphism ...Poly means mini....morphism means many forms..
## Method Overriding...It redefine the method in a child class
an = 0
if an == 1:
    class dad:
        def house(self):
            print(f"old paint color is blue")


    class son(dad):
        def house(self):
            print(f"New paint color is white")


    paint = son()
    paint.house()

## Method overloading is not support in python....
## python wont allow same method name in a same class...must be all method have different name...
## this code dont run....python doesnt support same class name..same function name in a  class class...we use parameter type to use the needed function in java...
# here, python dont allow overloading....Each methiod have diff name
an = 0
if an == 1:
    # class dad:
    #     def house(self,a):
    #         print(f"{a} bhk house in delhi")
    #
    #     def house(self,a):
    #         print(f"3 bhk {a} in Chennai")
    #
    # home = dad()
    # home.house('house')
    class dad:
        def house1(self, a):
            print(f"{a} bhk house in delhi")

        def house2(self, a):
            print(f"3 bhk {a} in Chennai")


    home = dad()
    home.house1(2)
    home.house2('house')

# Abstraction
# we should import from abc import ABC, abstractmethod
# from abc import ABC - To make your class abstract..it is default
## Here using @abstractmethod above each function means...these method should be implement..mandatory...without implelment this method,code dont run
# ABC: A base class that marks a class as abstract.
# @abstractmethod: A decorator to declare a method that must be implemented in child classes.
# if i didnt mention mention @abstractmethod,it not mandotory..without implement is not problem..code will run....
an = 0
if an == 1:
    from abc import ABC, abstractmethod


    class Manager(ABC):
        @abstractmethod
        def login(self):
            pass

        @abstractmethod
        def logout(self):
            pass

        @abstractmethod
        def checkout(self):
            pass

        def feedback(self):
            pass


    class employee(Manager):
        def login(self):
            print('Login Succesfully')

        def logout(self):
            print('Logout Succesfully')

        def checkout(self):
            print('Checkout Succesfully')


    task = employee()
    task.login()
    task.logout()
    task.checkout()

## Access Specifiers
# Variables
## Same classs
an = 0
if an == 1:
    class Bank:
        def __init__(self, balance, Branch_name, Acc_nmbr):
            self.balance = balance
            self._Branch_name = Branch_name
            self.__Acc_nmbr = Acc_nmbr

        def Customer(self):
            print(f"Your acc number is {self.__Acc_nmbr}")
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    details = Bank(5000, 'Nagercoil', 12345566)
    details.Customer()

## Sub classs
an = 0
if an == 1:
    class Bank:
        def __init__(self, balance, Branch_name, Acc_nmbr):
            self.balance = balance
            self._Branch_name = Branch_name
            self.__Acc_nmbr = Acc_nmbr


    class Third_party(Bank):
        def Customer_details(self):
            try:
                print(f"Your acc number is {self.__Acc_nmbr}")
            except:
                print(
                    f"You dont have access to account number")  ## this willl run......cant access the private variable in sub classs or strange class
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    details = Third_party(5000, 'Nagercoil', 12345566)
    details.Customer_details()

## Strange classs
an = 0
if an == 1:
    class Bank:
        def __init__(self, balance, Branch_name, Acc_nmbr):
            self.balance = balance
            self._Branch_name = Branch_name
            self.__Acc_nmbr = Acc_nmbr

        def Customer(self):
            print(f"Your acc number is {self.__Acc_nmbr}")
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    class Finance:
        def Customer_details(self, details):
            try:
                print(f"Your acc number is {details.__Acc_nmbr}")
            except:
                print(
                    f"You dont have access to account number")  ## this willl run......cant access the private variable in sub classs or strange class
            print(f"Your Branch Name is {details._Branch_name}")
            print(f"Your Balance is {details.balance}")


    details = Bank(5000, 'Nagercoil', 12345566)
    details_finance = Finance()
    details_finance.Customer_details(details)

## Name mangling by subclass
an = 0
if an == 1:
    class Bank:
        def __init__(self, balance, Branch_name, Acc_nmbr):
            self.balance = balance
            self._Branch_name = Branch_name
            self.__Acc_nmbr = Acc_nmbr

        def Customer(self):
            print(f"Your acc number is {self.__Acc_nmbr}")
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    class Third_party(Bank):
        def Customer_details(self):
            print(
                f"Your acc number is {self._Bank__Acc_nmbr}")  ## use name mangling to get acc number from subclass...using parent class name and acc number
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    details = Third_party(5000, 'Nagercoil', 12345566)
    details.Customer_details()

## Name mangling by Strange class
an = 0
if an == 1:
    class Bank:
        def __init__(self, balance, Branch_name, Acc_nmbr):
            self.balance = balance
            self._Branch_name = Branch_name
            self.__Acc_nmbr = Acc_nmbr

        def Customer(self):
            print(f"Your acc number is {self.__Acc_nmbr}")
            print(f"Your Branch Name is {self._Branch_name}")
            print(f"Your Balance is {self.balance}")


    class Finance:
        def Customer_details(self, obj):
            print(
                f"Your acc number is {obj._Bank__Acc_nmbr}")  ## use name mangling to get acc number from stranger class...using parent class name and acc number
            print(f"Your Branch Name is {obj._Branch_name}")
            print(f"Your Balance is {obj.balance}")


    obj = Bank(5000, 'Nagercoil', 12345566)
    details_finance = Finance()
    details_finance.Customer_details(obj)

## Encapsulation
#Encapsulation is the concept of binding data (variables) and code (methods) that operates on that data into a single unit — typically a class — and restricting direct access to some of the object's components.
# Encapsulation = Data hiding + Controlled access

an = 0
if an == 1:
    class Order:
        def __init__(self, Customer_name, item, total_price, discout_price):
            self.Customer_name = Customer_name
            self.item = item
            self._total_price = total_price
            self.__discout_price = discout_price

        def __discount(self):
            return (self._total_price - self.__discout_price)

        def _admin_view(self):
            return {
                'Customer Name': self.Customer_name,
                'Items ': self.item,
                'Total Price ': self._total_price,
                'Discount Price ': self.__discout_price,
                'Final Price ': f"{self.__discount()}"
            }

        def customer_view(self):
            return {
                'Customer Name': self.Customer_name,
                'Items ': self.item,
                'Final Price ': f"{self.__discount()}"
            }


    class admin_portal:
        def show_order(self, Orders):
            return Orders._admin_view()


    class customer_portal:
        def show_order(self, Orders):
            return Orders.customer_view()


    Orders = Order("Arfas khan", ["Briyani", "Pepsi"], 300, 50)
    asdmin = admin_portal()
    custmr = customer_portal()
    print(asdmin.show_order(Orders))
    print(custmr.show_order(Orders))

## Instance vs class vs static method
# 3 types of methods
# instance_method	Behaviors that use or modify object data
# class_method	Behaviors that use or modify class data
# static_method	Helper functions unrelated to object or class
an = 0
if an == 1:
    class Student:
        # class variable to store school name
        school = "Global High School"

        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

        def student_info(self):  # instances
            print(f"Name : {self.name} \nGrade : {self.grade}")

        @classmethod
        def change_school(cls, new_school):  # class
            # Update class variable
            cls.school = new_school

        @staticmethod
        def school_notice():  # static
            # Print a static notice
            print(f"He is a School first student")


    stud = Student('Arfas Khan', 12)
    stud.student_info()
    Student.change_school('Scott')
    print(f"New school name is {Student.school}")
    Student.school_notice()

# File handling
# r - read only(file must exist),w - write ony(overwrite or creates),a - appends only(adds to end of file),r+ - read + write(fuile must exist),w+ - write + read(overwrites or creates),/
# a+ - append + read (creates if not exist) , r - read binary,wb - write binary , a - append binary
an = 0
if an == 1:
    file = open('File1.txt', 'w')
    file.write('Hi...Im Arfas Khan\n')
    file.write('I was a volleyball player\n')
    file.write('I will be a Data Engineer in September\n')
    file.close()

an = 0
if an == 1:
    file = open('File1.txt', 'r')
    content = file.read()
    print(content)
    file.close()

an = 0
if an == 1:
    file = open('File1.txt', 'a')
    file.write('Im learning python\n')
    file.close()

an = 0
if an == 1:
    with open('File1.txt', 'r') as file:
        for f in file:
            print(f.strip())

an = 0
if an == 1:
    count = 10
    while count > 0:
        input_ = input('Enter the data : ')
        with open('File1.txt', 'a') as file:
            file.write(input_ + '\n')

        with open('File1.txt', 'r') as file:
            for f in file:
                print(f.strip())
        count -= 1

an = 0
if an == 1:
    with open('File1.txt', 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            if 'python' in line:
                print(line.strip())

an = 0
if an == 1:
    with open('File1.txt', 'r') as file:
        for _ in range(7):
            print(file.readline().strip())

an = 0
if an == 1:
    with open('Players.csv', 'r') as infile, open('Volleyball_players.csv', 'w') as outfile:
        for line in infile:
            print(line.strip())
            outfile.write(line)

an = 0
if an == 1:
    import csv

    with open('Players.csv', 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            print(row['position'])

an = 0
if an == 1:
    with open('Players.csv', 'r') as file:
        read = file.readlines()
        for f in read[1:]:
            print(f.strip().split(',')[2])  # [2] for jersey number column

# Exception Handling
an = 0
if an == 1:
    try:
        quantity = int(input("Enter the quantity : "))
        amount = 200 * quantity
        average = amount / quantity
        print(f"Average amount of product is {average}")
    except Exception:
        print('Please enter the correct quantity')
# if you know the error,then specify the error name in except...otherwise put Exception..it will take /
# corrrect error name
# and you can put lots of exceptiion..if you have more than 1 error..but only if you know the error befor..
# otherwise simpley put exception..But if you know, 2 errors 1 is zerodivisionerror and memory error
an = 0
if an == 1:
    try:
        quantity = int(input("Enter the quantity : "))
        amount = 200 * quantity
        average = amount / quantity
        print(f"Average amount of product is {average}")
    except ZeroDivisionError:
        print('Please enter the correct quantity.')
    except MemoryError:
        print('Memory is not enough to run this code....')
    finally:
        print(f"Executed Succesfully")  # in finally block,You can run all inside the finally block/
        # if code has no error,,try block run and also finally block run....if code has error, the excpet block run and also finally block run...

# mmysql connectiion
an = 0
if an == 1:
    import pymysql

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='test',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            Create_query = """
            CREATE TABLE IF NOT EXISTS students (
                Id SERIAL PRIMARY KEY,
                First_name VARCHAR(50),
                Last_name VARCHAR(50),
                Grade VARCHAR(50),
                Section VARCHAR(10),
                Mobile_number VARCHAR(15),
                Guardian VARCHAR(50)
            );
            """
            cursor.execute(Create_query)

            insert_query = "INSERT INTO students (First_name,Last_name,Grade,Section,Mobile_number,Guardian) VALUES(%s,%s,%s,%s,%s,%s);"
            values = [('Aarav', 'Sharma', '10', 'A', '9123456701', 'Rakesh Sharma'),
                      ('Vivaan', 'Verma', '9', 'B', '9123456702', 'Nitin Verma'),
                      ('Aditya', 'Gupta', '8', 'C', '9123456703', 'Suresh Gupta'),
                      ('Krishna', 'Mishra', '11', 'D', '9123456704', 'Arvind Mishra'),
                      ('Vihaan', 'Patel', '10', 'A', '9123456705', 'Ketan Patel'),
                      ('Ishaan', 'Yadav', '12', 'B', '9123456706', 'Sanjay Yadav'),
                      ('Shaurya', 'Joshi', '9', 'C', '9123456707', 'Harish Joshi'),
                      ('Atharv', 'Reddy', '8', 'D', '9123456708', 'Mohit Reddy'),
                      ('Aryan', 'Khan', '7', 'A', '9123456709', 'Rajiv Khan'),
                      ('Kabir', 'Singh', '11', 'B', '9123456710', 'Anil Singh')]

            cursor.executemany(insert_query, values)
            connection.commit()

            select_query = "SELECT * FROM students;"
            cursor.execute(select_query)
            result = cursor.fetchall()
            with open('write_table_students.csv', 'w') as f:
                for row in result:
                    f.write(f"{row}\n")
    finally:
        connection.close()

# mmysql connectiion with masking password
an = 0
if an == 1:
    import pymysql

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=get_decrypted_password(),
        database='test',
        cursorclass=pymysql.cursors.DictCursor
    )
    print(f"Mysql is connected successfully!!!")
    print(get_decrypted_password())
    connection.close()

## Types of Functions

# Normal function code
an = 0
if an == 1:
    def build_email(username, domain):
        if domain == 'gmail':
            return print(f"{''.join(username).strip().lower().replace(' ', '')}@{domain.lower()}.com")
        elif domain == 'ymail':
            return print(f"{''.join(username).strip().lower().replace(' ', '')}@{domain.lower()}.com")
        elif domain == 'yahoo':
            return print(f"{''.join(username).strip().lower().replace(' ', '')}@{domain.lower()}.com")
        else:
            return print(f"{''.join(username).strip().lower().replace(' ', '')}@example.com")


    build_email('Arfas khan', 'gmail')

# 1. Higher order function
# a) Take another function in argument
# If any new mail domains..we just create a seperate function only for that domain...
# easy to maintain the code
an = 0
if an == 1:
    def gmail_(username, domain='gmail.com'):
        return print(f"{username}@{domain}")


    def ymail_(username, domain='ymail.com'):
        return print(f"{username}@{domain}")


    def yahoo_(username, domain='yahoo.com'):
        return print(f"{username}@{domain}")


    def build_email(username, mail_func):
        return mail_func(''.join(username).strip().lower().replace(' ', ''))


    # build_email('Arfas Khan',ymail_)
    build_email('Arfas Khan', yahoo_)

#b) Return a function as its output
##
an = 0
if an == 1:
    def build_mail(domain):
        def create_mail(username):
            print(f"{username.strip().lower().replace(' ', '')}@{domain}")

        return create_mail


    gmail = build_mail('gmail.com')
    gmail('Arfas khan')

# pass the function as an arguments (Higher order function)
from functools import reduce

an = 0
if an == 1:
    def sugar(kgs ,item = 'Sugar'):
        print(f"Price of {kgs}kgs {item} : {kgs* 70}")

    def Wheat_flour(kgs, item='Wheat Flour'):
        print(f"Price of {kgs}kgs {item} : {kgs * 50}")

    def water_bottle(litre ,item = 'Water Bottle'):
        print(f"Price of {litre}litre {item} : {litre* 30}")

    def Coconut_oil(litre ,item = 'Coconut Oil'):
        print(f"Price of {litre}litre {item} : {litre* 230}")

    def generate_bill(quantity,item_func):
        return item_func(quantity)

    items_function = [Coconut_oil,water_bottle,sugar,Wheat_flour]
    quanty = [5,2,1/2,1.5]
    for i,q in zip(items_function,quanty):
        generate_bill(q,i)


# it returns function as an output (Higher order function)
an = 0
if an == 1:
    def item_(item):
        def quantity(qntyty,quantity_name,price):
            print(f"Price of {qntyty}{quantity_name} of {item} : {qntyty*price}")
        return quantity

    sugar = item_(item = 'sugar')
    sugar(5,'Kgs',70)

    Coconut_oil = item_(item = 'Coconut oil')
    Coconut_oil(4,'Ltr',230)

    Wheat_flour = item_(item='Wheat Flour')
    Wheat_flour(4, 'Kgs', 50)

    water_bottle = item_(item='water Bottle')
    water_bottle(4, 'Ltr', 30)



# Pure and impure functions
 # pure functionn
 # username = 'Arfas khan' is globally assigned...So every function can use this variable...
 # Pure function is never affect the globally assigned variable
an = 0
if an == 1:
    username = 'Arfas Khan'

    def New_user():
         username = 'Vijay'
         print(f"Im a new user {username}")

    def old_user():
        print(f"Im a old user {username}")

    New_user() # Im a new user Vijay
    old_user() # Im a old user Arfas Khan

# Impure Function
an = 0
if an == 1:
    username = 'Arfas Khan'

    def New_user():
         global username  # if you change anything in a same variable, it change the global variable values also...
         username = 'Vijay'
         print(f"Im a new user {username}")

    def old_user():
        print(f"Im a old user {username}")

    New_user() # Im a new user Vijay
    old_user() # Im a old user Vijay

# lambda function
an = 0
if an == 1:
    ## lambda
    add = lambda a,b :a+b
    print(add(5,2))

    sqr = lambda x: x**2
    print(sqr(10))

    # Map
    nmbr = [ 5,10,33,554,367]
    add = list(map(lambda a : a+100 , nmbr))  ## map can take one by one vlaues in a list...Here a represent each values by iteration
    print(add)

    name = ['  Arfas khan  ', '  viJay moN','Gold Michael  ']
    rename = list(map(lambda a: a.strip().title().replace(' ','_'), name))
    print(rename)

    # Filter
    nmbr = [5, 10, 33, 554, 367]
    grtr_than_10 = list(filter(lambda a:a>10,nmbr))
    print(grtr_than_10)

    nmbr = [5, 10, 33, 554, 367]
    even_nmbr = list(filter(lambda a: a%2==0, nmbr))
    print(even_nmbr)

    name = ['  Arfas khan  ', '  viJay moN', 'Gold Michael  ','Alwin']
    rename = list(filter(lambda a: a.strip().capitalize().startswith('A'), name))
    print(rename)

    # Reduce
    nmbr = [5, 10, 33, 554, 367]
    add = reduce(lambda a,b: a+b, nmbr)
    print(add)

    nmbr = [5, 10, 33, 554, 367]
    largest_nmbr = reduce(lambda a, b: a if a>b else b, nmbr)
    print(largest_nmbr)

    # Filter and reduce
    nmbr = [5, 10, 33, 554, 367]
    grtr_than_10 = list(filter(lambda a: a > 10, nmbr))
    add = reduce(lambda a,b : a+b,grtr_than_10)
    print(add)

# Lambda
an = 0
if an == 1:

    lmb_data1  = lambda a,b,c,d : a*b*(c+d)
    print(lmb_data1(3,7,5,2))

    lmb_data2 = lambda a, b, c, d: a * d * (b + d) +(a /c)
    print(lmb_data2(3, 7, 5, 2))

# Map
an = 0
if an == 1:
    names = ['Divya','Sudha','Samiga','Suhaina']
    names_upper = list(map(lambda nms: nms.upper().strip() , names))
    print(names_upper)

    names = ['Divya', 'Sudha', 'Samiga', 'Suhaina']
    names_upper = list(map(lambda nms: nms.upper().strip(), names[::-1]))
    print(names_upper)

    names = ['   Divya Parvathi  ', ' Jeya Sudha  ', '  Samiga ', '  Suhaina  ']
    names_upper = list(map(lambda nms: nms.title().strip().replace(' ',''), names))
    print(names_upper)

    names = ['   Divya Parvathi  ', ' Jeya Sudha  ', '  Samiga ', '  Suhaina  ']
    names_upper = list(map(lambda nms: nms.title().strip().replace(' ',''), names))
    print(names_upper)

# Filter
an = 0
if an == 1:
    names = ['Divya','Sudha','Samiga','Suhaina']
    names_upper = list(filter(lambda nms: nms.upper().strip().startswith('S'), names))
    print(names_upper)

    names = ['Divya', 'Sudha', 'Samiga', 'Suhaina']
    names_upper = list(map(lambda nms: nms.lower().strip()[::-1], names[::-1]))
    print(names_upper)

    nmbr = [7336387,92829,3635363,484774,7736727]
    grtst_nmbrs = list(filter(lambda nmb : nmb > round(nmbr[4]/3) , nmbr))
    print(grtst_nmbrs)

# Reduce
an = 0
if an == 1:
    nmbr = [63798339,484733,7478933,836373]
    nmbr_ = reduce(lambda a,b : a if a>b else b ,nmbr)
    print(nmbr_)


# closure function
# inner function  can take all argument from outer function ....
an = 0
if an == 1:
    def outer(username,domain):
        def inner():
            print(f"{username}@{domain}.com")
        return inner()

    mail_ = outer('arfaskhan','gmail')

# Partially Function
an = 0
if an == 1:
    def calculate_tax(price,tax_rate):
        taxed_price = price * tax_rate
        return print(f"{price + taxed_price}")

    tax_ = partial(calculate_tax,tax_rate = 0.18)
    tax_(2000)

an = 0
if an == 1:
    def calculate_expression(a,b):
        expres = a*b+(b**2)*(a^b) - (b*a)
        return print(expres)

    calc_ = partial(calculate_expression,b = 5)
    calc_(8)

# Composed Function
# It is when the output of function is given as the inpput of other function..
an = 0
if an == 1:
    def add(x,y):
        return x+y

    def multiply(x):
        return x*x

    print(multiply(add(5,10)))

# Call ack function....A callback is a function you give to another function to be "called back" later...
# greet is a callback function — passed to process_name and then process_name receives the function as an argument (callback)
# It then calls that function with the name "Arfas"
an = 0
if an == 1:
    def greet(name):
        return f"Hello, {name}!"


    def process_name(callback):
        name = "Arfas"
        return callback(name)


    print(process_name(greet))

# Recursive function
# It is a function that calls itself...
an = 0
if an == 1:
    def factorial(n):
        if n == 1:
            return 1
        return n * (factorial(n-1))

    print(factorial(10))

an = 0
if an == 1:
    def countdown(n):
        if n == 0:
            print(f"The title winner is Arfas Khan")
            return
        print(n)
        countdown(n-1)
    print(countdown(10))

# Generator function
# A generator function is a special type of function that uses the yield keyword to return value one by one,instead of returning everything at once..
an = 0
if an == 1:
    def numbers(n):
        for i in range(n):
            yield  i

    for num in numbers(10):
        print(num)

# Test case (Run test_code.py to test this section codes
an = 0
if an == 1:
    def amnt_prdct(quantity):
        amount = 200 * quantity
        return amount

an =0
if an == 1:
    def sugar(kgs):
        return kgs * 70


    def Wheat_flour(kgs):
        return kgs * 50


    def water_bottle(litre):
        return litre * 30


    def Coconut_oil(litre):
        return litre * 230


    def generate_bill(quantity, item_func):
        return item_func(quantity)
