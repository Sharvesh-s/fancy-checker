'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def is_goodNum(num):
    str_num = str(num)
    first = str_num[:2]
    second = str_num[2:]
    if int(second)>int(first):
        return True
    else: 
        return False
 
def total_(num):
    total= 0
    last_digit = num%10
    if num ==0:
        return 0
    else :
        total += last_digit
        return total+total_(num//10)

def lucky_(num):
    if num in lucky:
        return "lucky"
    elif num in very_lucky:
        return "very_lucky"
    else:
        return

def is_fancy(num):
    lst = list(str(num))
    for i in lst:
        if lst.count(i)>=2:
            return True
    else:
        return False

def fancy_num(lst):
    count = 0
    for i in lst:
        #to check for fancy.
        if is_fancy(i):
            #to check for good number.
            if is_goodNum(i):
                summ = total_(i)
                #to check for luck.
                if (lucky_(summ)!=None):
                    count+=1
                    print(i,'-',summ,end = " ")
                    print(lucky_(summ),"|", summ+17,end = " ")
                    if summ+17 in lucky:
                        print("lucky")
                    elif summ+17 in very_lucky:
                        print("very lucky")
                    else :
                        print("Not lucky")
                
    else:
        print()
        print("Choose any one from ",count)

lucky = (1,3,5,6,9,10,14,15,16,18,21,24,27,32,33,36,42,46,50,51)
very_lucky = (19,23,37,41,45)

number = [x for  x in range(7000,8501)]
fancy_num(number)

