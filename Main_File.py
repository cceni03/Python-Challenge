#Module
import os
import csv

csvpath=os.path.join('..','Resources', 'budget_data.csv')
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_reader = next (csvreader)
    Month = 0
    Total = 0
    Revenue = 0
    Revenue_Change = 0
    Monthly_Change = 0

    print(f"Header: {csv_header}")

#Months
    for row in csvreader:
            month.append(row[0])
            revenue.append(row[1])
    print(len(month))
#Profit/Loss
    Revenue_Int = map (int, revenue)
Total_Revenue = (sum(revenue_int))
print(Total_Revenue)

#Average Change in Profit/Loss
        i = 0
        for i in range(len(revenue) - 1):
            profit_loss = int(revenue[i+1]) - int(revenue[i])
#Append Profit_Loss
            Revenue_Change.append(Profit_Loss)
        Total = sum(Revenue_Change)
        #print(revenue_change)
        Revenue_int = map(int, revenue)
        print(Monthly_Change)
        #print(Total)

    #Greatest Increase in Profits
        profit_increase = Max(Revenue_Change)
        print(Profit_Increase)
        k = Revenue_Change.Index(Profit_Increase)
        Month_Increase = Month[k+1]

    #Greatest Decrease in Profits
        Profit_Decrease = Min(Revenue_Change)
        print(Profit_Decrease)
        j = Revenue_Change.Index(Profit_Decrease)
        Month_Decrease = Month[j+1]
 
#Print Statements

print(f'Financial Analysis'+'\n')

print(f'----------'+'\n')   

print("Total Number of Months: " + str(len(month)))

print("Total: $" + str (Total_Revenue))

print("Average Change: $" + str (monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")