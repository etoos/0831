

bangdream! girls band party!                1



print("{0:.3f}".format(9.3/2.7))
y=2.5 * 4.8
print("{:.1f}".format(y))
r = 8/float(3)
print("{:.2f}".format(r))
print("{0:.4f}".format(8.0/3))


print("{0:.3f}".format(9.3/2.7))
y=2.5 * 4.8
print("{:.1f}".format(y))
r = 8/3
print("{:.2f}".format(r))
print("{0:.4f}".format(8.0/3))               2

2.문자열



print("{:s}".format('I\'m enjoying learning Python.'))

print("{0:s}".format("This is a long string.Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult in read and edit. By using the backslash you can split the long\
string into smaller strings on seperate lines so that the whole sring is easy\
to view in the editor."))

print("{0:s}".format('''you can use triple single quotes
for multi-line comment strings,'''))

print("{:s}".format("""You can also use triple double quotes 
for multi-line comment strings."""))                                                 3
 
integer.py   float.py string.py  


















string1 = "This is a"
string2 = "short string."
sentence = string1 + string2
print("{}".format(sentence))
print("{}{}{}".format("She is","very"*4,"beautiful."))
m = len(sentence)
print("{}".format(m))
string1 = "My deliveralbe is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print(string1_list1)
print("FIRST PIECE:{0}SECOND PIECE::{1}THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = "Your,deliveralbe,is,due,in,June"
string2_list=string2.split(',')
print(string2_list)
print("{}{}{}{}".format(string2_list[1],string2_list[2],string2_list[5],\
string2_list[-1]))
print("{}".format(','.join(string2_list)))


list01.py

a_list=[1,2,3]
print(a_list)
print("a_list has {} elements.".format(len(a_list)))
print("the maximum value in a_list is {}.".format(max(a_list)))
print("the minimum value in a_list is {}.".format(min(a_list)))
another_list=['printer',5,['star','circle',9]]
print(another_list)
print("another_list also has {} elements.".format(len(another_list)))
print("5 is in another_list {} time.".format(another_list.count(5)))
print(a_list[0])
print(a_list[1])
print(a_list[2])
print(a_list[-1])
print(a_list[-2])
print(a_list[0:2])

tuple.py
#튜플은 값을 변경할 수 없습니다.
#리스트와 동일하지만 값으로 변경할 수는 없습니다.
#값을 변경하는 함수를 제공하지 않습니다.
#튜플은 괄호를 이용하여 생성합니다.
my_tuple=('x','y','z')
your_tuple=(3,4,5,6,7)
print(my_tuple)
print(your_tuple)
print(my_tuple[1])
our_tuple=my_tuple+your_tuple
print(our_tuple)

dictionary.py

#중괄호를 이용하여 딕셔너리를 생성합니다.
#각 쌍의 키와 값 사이에 콜론(:)을 사용합니다.
#len()함수는 딕셔너리에 있는 키-값 쌍의 수를 샙니다.
a_dict={'one':1,'two':2,'three':3}
b_dict={3:'red',4:'green',55:'blue'}
print(a_dict)
print(b_dict)
print("a_dict has{!s} elements".format(len(a_dict)))
print(a_dict['one'])
print(b_dict[3])

test.py

5>3
3<5
3 <= 5
a=[1,2,3,4,5]
5 in a 
7 in a






        



