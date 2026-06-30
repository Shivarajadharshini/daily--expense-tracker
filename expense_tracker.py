expense_name=[]
expense_amount=[]
while True:
    print("DAILY EXPENSE TRACKER")
    print("1.add expense")
    print("2.show expense")
    print("3.total amount")
    print("4.delete amount")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
       name=input("enter expense name:")
       amount=float(input("enter amount:"))
       expense_name.append(name)
       expense_amount.append(amount)
       print("expense saved successfully")
    elif choice==2:
       if len(expense_name)==0:
        print("no expense found")
       else:
        print("total expense")
        for i in range(len(expense_amount)):
           print(i+1,".",expense_name[i],"-Rs",expense_amount[i])
    elif choice==3:
     total=0
     for amount in expense_amount:
       total=total+amount
     print("total amount=Rs",total)
    elif choice==4:
           name=input("enter expense name to delete:")
           if name in expense_name:
              index=expense_name.index(name)
              expense_name.pop(index)
              expense_amount.pop(index)
              print("expense delete successfully")
           else:
              print("no expense found")
    elif choice==5:
     print("tq for using daily expense tracker")
     break
    else:
     print("invalid choice!,pls try agian")
                        
                    
                 
