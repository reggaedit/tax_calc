#from Tkinter import
#root = Tk()
#filetest = Label(root, text="Calculate my Taxes, thanks.")
#filetest.pack()
#root.mainloop()

import locale
locale.setlocale( locale.LC_ALL, 'english-uk' )	

# -*- coding: utf-8 -*-
#Base Variables (ni=national insurance)
print "What is your Gross pay/salary? (Please do not use apostrophe's):"
gross_pay = int(raw_input())
income_allowance = 10600.00
income_rate_20 = 0.2
income_rate_40 = 0.4
income_rate_45 = 0.45
ni_allowance = 8060
ni_rate = 0.12

#Income TAX calculations, taking into consideration taxation at different bands.
taxable_income = gross_pay - income_allowance
#Evaluates when there is no tax
if taxable_income <= 0:
	income_in_band_20 = 0
	income_in_band_40 = 0
	income_in_band_45 = 0
	tax_band_msg = "I do not pay income tax."
#Evaluates 20% tax
elif taxable_income <= 31785:
	income_in_band_20 = taxable_income
	income_in_band_40 = 0
	income_in_band_45 = 0
	income_tax = taxable_income * income_rate_20
	tax_band_msg = "I have reached the 20% band."
#Evaluates 20% and 40% tax
elif taxable_income <= 150000:
	income_in_band_20 = 31785
	income_in_band_40 = taxable_income - 31785
	income_in_band_45 = 0
	income_tax = 6357 + ((taxable_income - 31785) * income_rate_40)
	tax_band_msg = "I have reached the 40% band."
#Evaluates 20%, 40%, and 45% tax
else:
	income_in_band_20 = 31785
	income_in_band_40 = 118215
	income_in_band_45 = taxable_income - 150000
	income_tax = 6557 + 47285.6 + ((taxable_income - 150000) * income_rate_45)
	tax_band_msg = "I have reached the 45% band."

#NI TAX
ni_taxable = gross_pay - ni_allowance
ni_tax = ni_taxable * ni_rate

#Total tax payable
total_tax = income_tax + ni_tax

#Calculates the net wage
yr_net_wage = gross_pay - total_tax
mth_net_wage = yr_net_wage / 12

#summarises various monthly costs
rent = 650.00
energy = 150.00 / 4
piano_lessons = 0
phone = 60.00
council_tax = 110
food = 200.00
barclays = 150

#Calculates costs
mth_expense = rent + energy + piano_lessons + phone + council_tax + food + barclays
yr_expense = mth_expense * 12

#Printing the various statements
print "\nMy yearly gross income is: %s\n" % locale.currency(gross_pay, grouping=True)
print "The tax free allowance is: %s\n" % locale.currency(income_allowance, grouping=True)
print "My taxable income is: %s" % locale.currency(taxable_income, grouping=True)
print tax_band_msg, "\n"
#Printing the income tax amounts at different tax rate bands
print "My income is taxed at multiple levels: "
print "\t20%% rate (of %s): %s" % (locale.currency(income_in_band_20, grouping=True), locale.currency(income_in_band_20*income_rate_20, grouping=True))
print "\t40%% rate (of %s): %s" % (locale.currency(income_in_band_40, grouping=True), locale.currency(income_in_band_40*income_rate_40, grouping=True))
print "\t45%% rate (of %s): %s" % (locale.currency(income_in_band_45, grouping=True), locale.currency(income_in_band_45*income_rate_45, grouping=True))
print "\tTotal income tax: %s\n" % locale.currency(income_tax, grouping=True)
#Printing the NI tax figures
print "My NI is taxed at %r percent of %s. I need to pay: %s\n" % (ni_rate*100, locale.currency(ni_taxable, grouping=True), locale.currency(ni_taxable * ni_rate, grouping=True))
#Printing the total tax and net wage
print "\tMy total deductions are: %s\n" % locale.currency(total_tax, grouping=True)
print "My net wage is..."
print "\t* yearly: %s" % locale.currency(yr_net_wage, grouping=True)
print "\t* monthly: %s" % locale.currency(mth_net_wage, grouping=True)
#Printing
print "After all other monthly costs, I have %s of disposable income left" % locale.currency(mth_net_wage - mth_expense, grouping=True)