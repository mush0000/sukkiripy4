#4-6
#(1)
numbers = [1,1]
ratios = []
number_A = 0
number_B = 1
ans = 0

for num in numbers :
    ans = numbers[number_A] + numbers[number_B]
    if ans < 1000:
        numbers.append(ans)

        #(2)
        div = ans / number_B
        ratios.append(div)

        number_A += 1
        number_B += 1
    else:
        break
print(numbers)

#(2)
print(ratios)

#(3)
number_A = 0
for num in ratios:
    conver = ratios[number_A] *1000
    conver = int(conver)
    ratios[number_A] = conver /1000

    

    number_A += 1
print(ratios)
