return_date =list(map(int, input().split()))
due_date = list(map(int, input().split()))
fine = 0
# if return_date[0]<=due_date[0] and return_date[1]<=due_date[1] and return_date[2]<=due_date[2]:
#     print(fine)
if return_date[0]>=due_date[0] and return_date[1]==due_date[1] and return_date[2]==due_date[2]:
    late_days = return_date[0]-due_date[0]
    print(late_days)
    fine = late_days*15
    print(fine)

elif return_date[1]>=due_date[1] and return_date[2]==due_date[2]:
    late_days = return_date[1]-due_date[1]
    fine=late_days*500
    print(fine)

elif return_date[2]>=due_date[2]:
    late_day = return_date[2]-due_date[2]
    fine=late_day*10000
    print(fine)

else:
    print(fine)