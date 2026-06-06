'''
Problem Name : Equation

Problem Link : https://codeforces.com/contest/20/problem/B

Description : You are given an equation: Ax2 + Bx + C = 0.
Your task is to find the number of distinct roots of the equation and print all of them in ascending order.
Input : The first line contains three integer numbers A, B and C ( - 105 ≤ A, B, C ≤ 105). Any coefficient may be equal to 0.
Output : In case of infinite root count print the only integer -1. In case of no roots print the only integer 0. In other cases print the number of root on the first line and the roots on the following lines in the ascending order. Print roots with at least 5 digits after the decimal point.

Examples
Input
1 -5 6
Output
2
2.0000000000
3.0000000000

My Approach : To find the roots of the equation, we first calculate the discriminant using the formula: D = b^2−4ac
The discriminant helps us determine the nature of the roots:
If D < 0, the equation has no real roots.
If D > 0, the equation has two distinct (unequal) real roots.
If D = 0, the equation has two equal real roots.

According to the problem statement:
Print 0 if there are no real roots.
Print -1 if there are infinitely many solutions. Infinitely many solutions occur when a = 0, b = 0, and c = 0.

To find the roots, we use the quadratic formula:
This formula gives two possible values of x: x1 = (-b+(D^0.5)/2a) and x2 = (-b-(D^0.5) /2a).
'''

a, b, c = map(int, input().split())
D = (b**2)-(4*a*c)
if a == 0 and (b == 0 and c == 0):
    x = -1
elif D < 0 or (a == 0 and (b == 0 and c != 0)):
    x = 0
elif a == 0 and c == 0:
    x = c/(-b)
    y = c/(-b)
elif a == 0:
    x = (-c)/b
    y = (-c)/b
else:
    x = (-b+(D**0.5))/(2*a)
    y = (-b-(D**0.5))/(2*a)
if x == -1 and type(x) == int:
    print(x)
elif x == 0 and type(x) == int:
    print(x)
elif x == y:
    print(1)
    print(str(x)+'00000')
else:
    print(2)
    print(str(min(x,y))+'00000')
    print(str(max(x,y))+'00000')
