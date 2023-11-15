#4-5
#(1)
temp = [7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
count =0
temp_new =[]



#(2)
for num in temp:
    print(temp[count])
    count += 1
    
#(3)
count = 0
for num in temp:
    print(count)
    if count == 5:
        temp_new.append("N/A")
        print(temp_new[count])
        count += 1
    else:
        temp_new.append(num)
        print(temp_new[count])
        count += 1

#(4)
ave = 0
count = 0
ane = 0

for num in temp_new:
    if  isinstance(num,str):
        continue
    else:
        ave += temp[count]
        ans = ave / len(temp_new)
        count += 1
print("今日の平均気温は{}です。".format(ans))