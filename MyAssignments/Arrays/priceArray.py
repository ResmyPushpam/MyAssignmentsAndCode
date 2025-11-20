'''Create an array of prices [2.99, 5.50, 1.25, 8.00, 3.75]. Write a program that applies a 10% 
discount to each price and stores the new prices in a separate array. '''

priceArray=[2.99, 5.50, 1.25, 8.00, 3.75]
newpriceArray=[]
for price in priceArray:
    price=price-10/100*price
    newpriceArray.append(round(price,2))
    
print(newpriceArray)


