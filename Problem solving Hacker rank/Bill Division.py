n =  list(map(int, input().split()))
bill = [3, 10, 2, 9]
b = 7
charge= (sum(bill)-bill[n[1]])/2
# print(charge)
if charge==b:
    print("Bon Appetit")
else:
    print(int(b-charge))