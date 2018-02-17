#Create File paths along operating systems. Import os module
import os

#Inset name of the csv. This is the only thing you need to change if you want to make this replicable to other files
csvpath = os.path.join('raw_data', 'budget_data_1.csv')
csvoutput = os.path.join('raw_data', 'budget_data_1_output.csv')

# Import csv budget_data_1 using CSV module
import csv

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and the variable which holds the contents
    csv_reader_budget = csv.reader(csvfile, delimiter=',')
    #This is optional only if you want to see the path name
    print("<CSV Path Name>:",csv_reader_budget)
  
    #skip the header of the columns in the csv
    next(csv_reader_budget)
    #declare my lists
    total_revenue = []
    date = []
    change_in_revenue = []
    #loop through my rows
    for row in csv_reader_budget:
        total_revenue.append(float(row[1]))
    
        date.append(row[0])
    print("--------------------------")
    print("Revenue Analysis - Budget")
    print("--------------------------")
    print("1. Total Revenue Budget: "," $", sum(total_revenue))
    print("2. Total Months:", len(date))

    for i in range(1, len(total_revenue)):
        change_in_revenue.append(total_revenue[i] - total_revenue[i-1])
        avg_change_in_rev = sum(change_in_revenue)/len(change_in_revenue)
        min_change_in_rev = min(change_in_revenue)
        max_change_in_rev = max(change_in_revenue)
        min_change_in_date_rev = str(date[change_in_revenue.index(min(change_in_revenue))])
        max_change_in_date_rev = str(date[change_in_revenue.index(max(change_in_revenue))])

    print("3. Average change in revenue:", "$", avg_change_in_rev)
    print("4. Min increase in revenue:", min_change_in_date_rev, "($",min_change_in_rev,")")
    print("5. Max increase in revenue:", max_change_in_date_rev, "($",max_change_in_rev,")")

    
    #export csv
    with open(csvoutput, 'w',  newline='') as outputfile:
        csv_writer_budget = csv.writer(outputfile, delimiter=',')
    #it's optional to print the name
        print("<CSV Path Name>:", csv_writer_budget)

    #print in csv, numbers will be printed in strings
        csv_writer_budget.writerow(["---------------------------"])
        csv_writer_budget.writerow(["Revenue Analysis - Budget"])
        csv_writer_budget.writerow(["---------------------------"])
        csv_writer_budget.writerow(["1. Total Revenue Budget:","$"+str(sum(total_revenue))])
        csv_writer_budget.writerow(["2. Total Months:", len(date)])
        csv_writer_budget.writerow(["3. Average change in revenue:", "$"+str(avg_change_in_rev)])
        csv_writer_budget.writerow(["4. Min increase in revenue:", "($" + str(min_change_in_rev) + ")", min_change_in_date_rev, ])
        csv_writer_budget.writerow(["5. Max increase in revenue:", "($" + str(max_change_in_rev) + ")", max_change_in_date_rev, ])

