
file_name = "phonebook.txt"
file1 = open(file_name, "a+")
file1.close


def show_main_menu():
    
    print( "------------------------------------------\n"+
         "  Welcome to Bot PhoneBook services\n"+
            "    ____Phone Book Menu___  \n" +
          "------------------------------------------\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To Quit the PhoneBook\n------------------------------------------\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Sorry :( your Phone Book is empty")
        else:
            print ("\n",file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        searching()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice== "4":
        print("Thanks for using Bot Phone Book Services")
    else:
        print("Wrong choice :/ , Please Enter valid input\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()



def searching():
    unsorted_name,unsorted_no,unsorted_mail= extracting()
    print('''Enter1 to search by name \nEnter2 to search by PhoneNumber''')
    x=int(input())
   
    if x==1:
        sorted_name,sorted_no,sorted_mail = bubble_sort(unsorted_name,unsorted_no,unsorted_mail)
        y = input("Enter the name: ")
        position = binary_search(sorted_name, 0, len(sorted_name)-1, y)

    elif x==2:
        sorted_no,sorted_name,sorted_mail = bubble_sort(unsorted_no,unsorted_name,unsorted_mail)
        y = input("Enter the PhoneNumber: ")
        position = binary_search(sorted_no, 0, len(sorted_no)-1, y)

    else:
        print("Please Enter valid input\n")
        searching()

    if position==-1:
        print("Sorry :(  Contact is not present in records")

    else:
        print(":)  Contact is present")
        print(f"name: {sorted_name[position]} \nphone number: {sorted_no[position]}\nmail: {sorted_mail[position]}")





def bubble_sort(list1,list2,list3):  
     
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp1 = list1[j]  
                temp2 = list2[j]
                temp3 = list3[j]
                list1[j] = list1[j+1]  
                list2[j] = list2[j+1]
                list3[j] = list3[j+1]
                list1[j+1] = temp1 
                list2[j+1] = temp2
                list3[j+1] = temp3
    return list1,list2,list3





def binary_search(arr, low, high, x):
    
  
    
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
 
   



def extracting():
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
    unsorted_name=[]
    unsorted_no=[]
    unsorted_mail=[]
      
    for line in file_contents:
        a=line.split()
        unsorted_name.append(a[0])
        unsorted_no.append(a[1])
        unsorted_mail.append(a[2])
    return unsorted_name,unsorted_no,unsorted_mail
    
    


def enter_contact_record():
    
   
    name = input("Enter Name: ")
    phone = input('Enter Phone number: ')
    email = input('Enter E-mail: ')
    contact = (name+ "   " + phone + "   " + email +  "\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "\nThis contact:\n",contact,"has been added successfully!")

show_main_menu()