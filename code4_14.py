#4-4
ans = 0
scores = [1,2,3,4,5,6,7,8,9]
count = 0
count_plus = 1

#(1)
for num_A in scores:
    for num_B in scores:
        ans = num_A * num_B
        if not num_A % 2 == 0:
            continue
        elif ans > 50:
             break
        else:
            print("{},".format(ans),end ="")
       
    print()

   