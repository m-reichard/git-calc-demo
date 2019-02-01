print('enter two numbers')
a = int(input())
b = int(input())

print('enter an operation')
op = input()

if op not in '+-':
    print('unknown op')

if op == '+':
    print('the sum is', a + b)

if op == '-':
    print('the difference is', a - b)
