#4-2

#(1)
count = 0
select = "y"

while select == "y":
    #(2)
    print("カレーを召しあがれ")

    #(3)
    print("{}皿のカレーを食べました".format(count))

    #(4)
    select = input("おかわりはいかがですか？(y/n)>>")

    #(5)
    if select == "y":
        count += 1
        continue
    if select == "n":
        break
print("ごちそうさまでした")