"""Given N numbers in the input. Print these numbers in the same order as they come in input.
Input:
First line contains integer N - denoting total count of numbers that are to be printed.
Second line contains N space separated integers.

Output:
Print the numbers in input.
"""


N=int(input())
A=list(map(int,input().split(' ')))
for i in range(len(A)):
    print(A[i],end=" ")
