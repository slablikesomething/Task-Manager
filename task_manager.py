import datetime

#pssd means password, ussnm is username
def user_information(ussnm, pssd):
    name = input("Enter Your Name Please: ")
    address = input("Your Address: ")
    age = input("Your Age Please: ")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address: ")

    f.write(address)
    f.write('\n')
    f.write("Age: ")
    f.write('\n')
    f.close()

def signup():
    print("Please Enter Username")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    user_information(username, password)
    print("Please Proceed To Login, Sir")
    login()

def login():
    print("Please Enter Username")
    user_nm = input("Enter Here: ")

    # password as entered while logging in
    pssd_wr = (input("Please Enter Password: "))+'\n'
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')

        # variable 'k' contains the password as saved in the file
        k = f_.readlines(0)[0]
        f_.close()

        # checking if the password entered is the same as the password saved while signing in
        if pssd_wr == k:
            print("1--To view your data \n2--To add task \n3--Update task \n4--View Task Status")
            a = input()

            if a == '1':
                view_data(usernm)
            elif a == '2':
                # add task
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Wrong Input! bhai dekh kr input dal")
        else:
            print("Sir, Your Password or Username Is Wrong")
            login()
    except Exception as e:
        print(e)
        login()

def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()

def task_information(username):
    print("Sir, Please Enter N.o Of Task You Want To Add")
    j = int(input())
    f1 = open(username, 'a')

    for i in range(1, j+1):
        task = input("Enter The Task")
        target = input("Enter The Target")
        pp = "TASK "+str(i)+' :'
        qq = "TARGET "+str(i)+" :"

        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')
        print("Do You Want To Stop? If So Press Space Bar, Otherwise Press Enter")
        s = input()
        if s == ' ':
            break
    f1.close()

def task_update(username):
    username = username+" TASK.txt"
    print("Please Enter The Tasks Which Are Completed")
    task_completed = input()

    print("Enter The Task Which You Still Haven't Started")

    print("Enter The Task You Are In The Process Of Doing")
    task_ongoing = input()

    fw = open(username, 'a')
    DT = str(datetime.datetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED \n")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    ussnm = username+" TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()

if __name__ == '__main__':
    print("WELCOME TO KRYTEN")
    print("Sir, Are You New To This Software?")
    a = int(input("Type 1 If New, Otherwise Press 0 ::"))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You Have Provided The Wrong Input, Sir")