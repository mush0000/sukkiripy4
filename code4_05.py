count = 0
student_num = int(input("学生の数を入力>>"))
score_list = list()
while count < student_num:
    count += 1
    score = int(input("{}>>".format(count)))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print("平均点は{}です".format(total / student_num ))