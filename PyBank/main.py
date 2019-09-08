import csv
import os
file=os.path.join("budget_data.csv")
#variables that will be used to gather the statistics
months=0
PL=0
increases=0
greaterIncrease=0
greaterDecrease=0

with open(file,"r") as budget_data:
    budgetReader=csv.reader(budget_data,delimiter=",")
    # Remove header line
    header=next(budgetReader) 
    for rows in budgetReader:
        # count months and add total P&L
        months+=1
        PL+=float(rows[1])
        # starting in the second month, calculate the increase/decrease in profits
        if months>1:
            change=float(rows[1])-priorMonth
            increases+=change
            # store result of current row to calculate the increase/decrease in the following row
            priorMonth=float(rows[1])
            #determine whether the current variance in the largest increase/decrease
            if change>greaterIncrease:
                greaterIncrease=change
                GImonth=rows[0]
            if change<greaterDecrease:
                greaterDecrease=change
                GDmonth=rows[0]
        else:
            # store the first result for the increase/decrease computation
            priorMonth=float(rows[1])
#Save as a string the summary that we want to product in order to print it in the terminal and add it to a text file
text=(f'''Financial Analisis
--------------------------------------------------
Months: {months}
Total result: ${int(PL)}
Average change: ${int(increases/months)}
Greates increase in profits: {GImonth}(${int(greaterIncrease)})
Greates decrease in profits: {GDmonth}(${int(greaterDecrease)}) 
''')
print(text)
f=open("financial_analysis.txt","w+")
f.write(text)