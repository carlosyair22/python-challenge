import csv
import os
file=os.path.join("budget_data.csv")
months=0
PL=0
increases=0
greaterIncrease=0
greaterDecrease=0
with open(file,"r") as budget_data:
    budgetReader=csv.reader(budget_data,delimiter=",")
    header=next(budgetReader)
    for rows in budgetReader:
        months+=1
        PL+=float(rows[1])
        if months>1:
            change=float(rows[1])-priorMonth
            increases+=change
            priorMonth=float(rows[1])
            if change>greaterIncrease:
                greaterIncrease=change
                GImonth=rows[0]
            if change<greaterDecrease:
                greaterDecrease=change
                GDmonth=rows[0]
        else:
            priorMonth=float(rows[1])

text=(f'''Financial Analisis
--------------------------------------------------
Months: {months}
Total result: ${int(PL)}
Average change: ${int(increases/months)}
Greates increase in profits: {GImonth}(${int(greaterIncrease)})
Greates decrease in profits: {GDmonth}(${int(greaterDecrease)}) 
''')
print(text)
f=open("output.txt","w+")
f.write(text)