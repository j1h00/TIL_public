"""
    세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

    그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

    괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
"""

# 무조건 덧셈을 한 뒤에 뺄셈을 해야 한다. ( 최대한 큰 값을 만든 뒤에 빼는 것이, 최소로 가는 방법.)
eq = input().split('-') # '-' 뺄셈으로 분리한다. 
new_eq = []

for eq2 in eq:
    _sum = 0
    nums = eq2.split('+') # '+' 덧셈으로 분리한다. 
    for num in nums:
        _sum += int(num) # 덧셈을 먼저 처리한다. 
    new_eq.append(_sum)

sub = new_eq[0]
for i in range(1, len(new_eq)):
    sub -= new_eq[i] # 뺄셈을 나중에 처리한다. 

print(sub)