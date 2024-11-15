# 1. To determine the profit or loss on sale.
profit=0 
loss=0
while  True:
    no_of_item = int(input("Enter the no of item :")) 
    buying_price = eval(input("Enter the buying price :"))
    selling_price = eval(input("Enter the selling price :"))
    invest = no_of_item * buying_price
    income = no_of_item * selling_price
    if(invest < income) :
        profit = profit + ( income - invest )
        print(f"Profit {profit} Rs. ")
               
    elif(invest > income):
        loss = loss + ( invest - income ) 
        print(f"Loss {loss} Rs")   
        
        
    else :      
        print("No profit , no loss.....")

    choice = input("If you want to calculate any other item's profit loss..press yes or no :")    
    if (choice == 'yes'):
        continue
    else :
        break

total_profit = profit - loss
print(f"Total profit is {total_profit}.")    

   


