users = [{'name':'mahmoud','balance':500000,'pinCode':1570},
         {'name':'kareem','balance':100000,'pinCode':1234},
         {'name':'rehab','balance':10000,'pinCode':2033},
         {'name':'mom','balance':110000,'pinCode':2211},
         {'name':'bob','balance':1000000,'pinCode':1345},
         {'name':'eman','balance':60000,'pinCode':1888},
         {'name':'akrm','balance':120,'pinCode':5555},
         {'name':'body','balance':3000,'pinCode':4444},
         {'name':'saed','balance':120000,'pinCode':3333},
         {'name':'boqlz','balance':120,'pinCode':6666},
         {'name':'bebo','balance':510000,'pinCode':9999},]
currentUser = {}
currentpinCode = 0
import time
def load (t):
    for i in range(1,t):
        print ('\rloading' + '.' * i , end=' ' )
        time.sleep(1)
def initialscreen ():
    global currentpinCode
    global currentUser
    found = False
    load(3)
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                please enter your                 @')
    print('@                  secret number ?                 @')
    currentpinCode = int(input('                        '))
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    print('\n\n\n\n\n\n')
    for user in users :
        if user ["pinCode"] == currentpinCode :
            currentUser = user
            found = True
    if found :
        selectscreen()
    else :
        errorScreen1()
    return
def errorScreen1() :
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                                                  @')
    print('@              Your pincode is wrong               @')
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    load(4)
    print('\n\n\n\n\n\n\n')
    initialscreen()
def errorScreen2() :
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                                                  @')
    print('@            your balance is not Enough            @')
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    load(4)
    print('\n\n\n\n\n\n\n')
    another()
def selectscreen():
    load(3)
    print('\r##################################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                  ' , currentUser['name'] ,'                        @')
    print('@ 1- cash Withdrawal              4-Bill Payment   @')
    print('@ 2- Balance Inquiry              5-Deposit money  @')
    print('@ 3-Transfer                      6-Donate         @')
    op = int(input('\n  Enter the required operation and then press enter  '))
    print('##############################################')
    if op == 1 :
        CashWithdrawal()
    elif op == 2:
        BalanceInquiry()
    elif op == 3 :
        Transfer()
    elif op == 4 :
        BillPayment()
    elif op == 5 :
        Depositmoney()
    elif op == 6 :
        Donate()
    else :
        errorScreen3()
    load(4)
    return
def CashWithdrawal ():
    load(3)
    global currentUser
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@          Please enter required  amount           @')
    print('@                                                  @')
    amount = int(input('                        '))
    print('####################################################')
    if amount <= currentUser['balance']:
        currentUser ['balance'] = currentUser ['balance'] - amount
        load(3)
        BalanceInquiry()
        thanks()
        initialscreen()
    else:
        errorScreen2()
    load(4)
    return
def BalanceInquiry():
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ' , currentUser['name'] ,'                       @')
    print('@            your Balance is :',currentUser["balance"],'             @')
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    load(4)
    another()
    return
def Transfer():
    global currentUser
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@          Please enter required  amount           @')
    print('@                                                  @')
    amount = int(input('                        '))
    name = input(' enter the person name ?')
    print('####################################################')
    if amount <= currentUser['balance']:
        for user in users :
            if (name.lower() == user ['name'].lower()):
                user ['balance'] = user ['balance'] + amount
                currentUser['balance'] = currentUser['balance'] - amount
        BalanceInquiry()
        load(3)
        thanks()
    else:
        errorScreen2()
    return
def BillPayment2 ():
    global currentUser
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@          Please enter required  amount           @')
    print('@                                                  @')
    amount = int(input('                        '))
    print('####################################################')
    if amount <= currentUser['balance']:
        currentUser['balance'] = currentUser['balance'] - amount
        BalanceInquiry()
        another()
    else:
        errorScreen2()
    load(4)
    return
def Depositmoney ():
    load(3)
    global currentUser
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@          Please enter required  amount           @')
    print('@                                                  @')
    amount = int(input('                        '))
    print('####################################################')
    currentUser['balance'] = currentUser['balance'] + amount
    load(3)
    BalanceInquiry()
    another()
    return
def Donate ():
    global currentUser
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@    Please enter required  amount for donate      @')
    print('@                                                  @')
    amount = int(input('                        '))
    print('####################################################')
    if amount <= currentUser['balance']:
        currentUser['balance'] = currentUser['balance'] - amount
        BalanceInquiry()
        another()
    else:
        errorScreen2()
    load(4)
    return
def thanks ():
    print('\r##############################################')
    print('@                                                  @')
    print('@                                                  @')
    print('@            tanks for using M7MOUD ATM            @')
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    initialscreen()
    return
def another ():
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@          if yo want another operation            @')
    print('@ 1- yes                             2- no         @')
    an = int(input('                        '))
    print('####################################################')
    if an == 1 :
        load(3)
        selectscreen()
    elif an == 2 :
        load(3)
        thanks()
    else :
        errorScreen3()
    return
def errorScreen3():
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                                                  @')
    print('@               this not an option                 @')
    print('@                                                  @')
    print('@                                                  @')
    print('####################################################')
    load(4)
    print('\n\n\n\n\n\n\n')
    another()
    return
def BillPayment ():
    print('\r##############################################')
    print('@             welcome to M7MOUD ATM                @')
    print('@                   ', currentUser['name'], '                       @')
    print('@   This ATM is paid to the electric company only  @')
    print('@ 1- yes                             2- no         @')
    am = int(input('                        '))
    print('####################################################')
    if am == 1 :
        BillPayment2()
    elif am == 2 :
        selectscreen()
    else :
        errorScreen3()
    return
initialscreen ()