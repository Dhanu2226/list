"""
4)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
"""
l=[]
l1=[]
l2=[]
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
for j in l:
    if(j%2==0):
        l1.append(j)
    else:
        l2.append(j)
print('The even list ',l1)
print('The odd list ',l2)
