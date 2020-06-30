#Budget Data
import os
import budget_data.csv

csvpath = os.path.join('..','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_header = next(csvfile)
    Month = []
    Total = []
    Profit_Loss = []
    Revenue_Change = []
    Monthly_Change = []

    #print(f"Header: {csv_header}")

    #Months
    for row in csvreader:
        Month.append(row[0])
        Revenue.append(row[1])
    print(len(months))

    #Profit/Loss
    Revenue_Int = map (int, revenue)
    Total_Revenue = (sum(revenue))
    print(Total_Revenue)

    #Average Change in Profit/Loss
    i = 0
    for i in range (len(revenue)
        profit_loss = int(revenue[i+1]) - int(revenue[i])
    if:
        Revenue_Change.append(Profit_Loss)
        Total = Sum(Revenue_Change)
    else:
        Monthly_Change = Total / Revenue_Change
        print(Monthly_Change)
        print(Total)

    #Greatest Increase in Profits
    Profit_Increase = Max(Revenue_Change)
    print(Profit_Increase)
    k = Revenue_Change.index(Profit_Increase)
    Month_Increase = Month[k+1]

    #Greatest Decrease in Profits
    Profit_Decrease = Min(Revenue_Change)
    print(Profit_Decrease)
    j = revenue_change.index(profit_decrease)
    Month_Decrease = Month[j+1]
 
#Print Statements

print(f'Financial Analysis'+'\n')

print(f'----------'+'\n')   

print("Total Number of Months: " + str(len(month)))

print("Total: $" + str (Total_Revenue))

print("Average Change: $" + str (monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")