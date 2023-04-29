import random
start_input=(input('press ENTER to START, F to QUIT '))
print('type 1 to choose addition\ntype 2 to choose division\ntype 3 to choose multiplication\ntype 4 to choose division')
user_input=int(input('Select the type of math problem: '))
while start_input!='f':
    if user_input==1:
        def addition(num1,num2):
            return user_answer==problem1
        count1=0
        count0=0
        num1=random.randrange(1,500)
        num2=random.randrange(1,100)
        problem1=num1+num2
        user_answer=int(input(f'{num1}+{num2}='))
        if addition(num1,num2) is True:
            print('You got it!')
            count1+=1
        else:
            print('At least you tried(')
            count0+=1
        a=input('ENTER to continue, F ENTER to quit ')
        if a=='f':
            print(f'You got {count1} correct, {count0} incorrect answer(s).')
            break
    elif user_input==2:
        def substraction(num1,num2):
            return user_answer==problem1
        count1=0
        count0=0
        num1=random.randrange(99,500)
        num2=random.randrange(1,100)
        problem1=num1-num2
        user_answer=int(input(f'{num1}-{num2}='))
        if substraction(num1,num2) is True:
            print('You got it!')
            count1+=1
        else:
            print('At least you tried(')
            count0+=1
        a=input('ENTER to continue, F ENTER to quit ')
        if a=='f':
            print(f'You got {count1} correct, {count0} incorrect answer(s).')
            break
    elif user_input==3:
        def multiplication(num1,num2):
            return user_answer==problem1
        count1=0
        count0=0
        num1=random.randrange(1,100)
        num2=random.randrange(1,10)
        problem1=num1*num2
        user_answer=int(input(f'{num1}x{num2}='))
        if multiplication(num1,num2) is True:
            print('You got it!')
            count1+=1
        else:
            print('At least you tried(')
            count0+=1
        a=input('ENTER to continue, F ENTER to quit ')
        if a=='f':
            print(f'You got {count1} correct, {count0} incorrect answer(s).')
            break
    elif user_input==4:
        def division(num1,num2):
            return user_answer==problem1
        count1=0
        count0=0
        num1=random.randrange(1,500)
        num2=random.randrange(1,10)
        if num1%num2==0:
            problem1=num1/num2
            user_answer=int(input(f'{num1}:{num2}='))
        else:
            continue
        if division(num1,num2) is True:
            print('You got it!')
            count1+=1
        else:
            print('At least you tried(')
            count0+=1
        a=input('ENTER to continue, F ENTER to quit ')
        if a=='f':
            print(f'You got {count1} correct, {count0} incorrect answer(s).')
            break