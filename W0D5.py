
#for i in range(1,15+1):
#    if (i%3==0 and i%5==0):
#        print("FuzzBizz")
#    elif (i%3==0):
#        print("Fuzz")
#    elif (i%5==0):
#        print("Bizz")
#    else:
#        print(i)
#

my_entry=int(input("input a number: "))
while my_entry % 2 == 0:
    print("your number was: ", my_entry)
    my_entry=int(input("input a number: "))


while 1:
    my_entry=int(input("input a number: "))
    if my_entry % 2 == 0:
        break
    print("your number was: ", my_entry)