#elegant_bills_calculator.py using the def function to shorten the code and make repairs easier
def incomecalc():
    Shours = input ('Enter Hours:')
    Srate = input ('Enter Rate of Pay:')
    Stax = input ('Enter Payroll Tax Rate:')
    #use try/except to isolate code errors that may happen if the enduser goofs on input
    try:
        Fhours = float (Shours)
        Frate = float (Srate)
        Ftax = float (Stax)
    except:
        print ('user did not enter numbers correctly, please try again')
        exit()
    #calculate overtime and base pay seperately and combine, then calculate how much is removed by taxes and subtract
    if Fhours > 40:
        OT = (Fhours - 40) * (Frate * 1.5)
        BP = 40 * Frate
        TP = OT + BP
        Death = (TP / 100) * Ftax
        TPT = TP - Death
        pay = Fhours * Frate
        print ('You made $', TP)
        print ('You have $', TPT, 'after taxes.')
        print ('Congrats on the overtime.')
    else:
        OT = (Fhours - 40) * (Frate * 1.5)
        BP = 40 * Frate
        TP = OT + BP
        pay = Fhours * Frate
        Death = (pay / 100) * Ftax
        TPT = pay - Death
        print ('This week you made $', pay)
        print ('This week you have $', TPT, 'after taxes.')
        print ('No overtime huh?')
    monthlyp = TPT * 4
    print ('You will make $', monthlyp, 'this month excluding taxes.')
    return monthlyp
#end of def1
print ('<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>')
nam = input ('Hey who are you?')
print ('Oh it is you', nam)
calc = input ('I suppose you want me to do some maths for you?')
if calc == ('yes'):
    print ('Okay then.')
else:
    print ('Well', nam, 'I have somewhere to be. Goodbye.')
    exit()
incomes = input ('Do you have one or two incomes?')
if incomes == ('one'):
    monthlyp = incomecalc()
    C = monthlyp
elif incomes == ('two'):
    user1 = nam
    user2 = input ('What is your partner named?')
    print ('Hello', user2, 'I will ask you for your info in a minute. Please standby.')
    print (user1,'please enter your data')
    monthlyp = incomecalc()
    A = monthlyp
    print (user2, 'please enter your data')
    monthlyp = incomecalc()
    B = monthlyp
    C = A + B
    print ('Your combined income after taxes is $', C, 'this month.')
else:
    print ('Invalid response - please try again.')
    exit()
print ('<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>')
#bill calculations:
print ('What are your household bills this month?')
rent = input ('Rent:')
elect = input ('Electricity:')
water = input ('Water:')
heat = input ('Natural Gas:')
garb = input ('Garbage Removal:')
sewage = input ('Sewage:')
bus = input ('Bus Pass:')
web = input ('Internet:')
phone = input ('Phones:')
subs = input ('Crunchyroll:')
magz = input ('Magazine Subscription:')
try:
    fren = float (rent)
    fele = float (elect)
    fwat = float (water)
    fhea = float (heat)
    fbus = float (bus)
    fweb = float (web)
    fpho = float (phone)
    fsub = float (subs)
    fgarb = float (garb)
    fsewa = float (sewage)
    fmagz = float (magz)
except:
    print ('You did not enter only numbers did you? Try again.')
    exit()
cash = C - fren - fele - fwat - fhea - fbus - fweb - fpho - fsub - fgarb - fsewa - fmagz
if cash > 0:
    print ('You have $', cash, 'to spend on food and other expenses.')
else:
    print ('I am sorry', nam, 'you have insufficient funds to survive this month. You are')
    print ('$', cash, 'in the hole.')
#create a code block for calculating food expenditures
print ('<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>')
members = input ('How many people are you feeding?')
month = input ('What month is it? Jan Feb Mar Apr etc.')
#restaurant calculations
restaurant = input ('How many meals will be eaten at a restaurant as a family?')
friends = input ('How many times will one of you go out with friends and pay dutch?')
datenight = input ('How many times will you go out on a date?')
#takeout calculations
pizza = input ('How many large pizzas will you order at once?')
pizz2 = input ('How many times will you order pizza this month?')
#packed lunches vs cafeteria
schlunch = input ('How many of you attend school?')
wrklunch = input ('How many of you work?')
packlunch = input ('Will you be packing lunches or eating at the cafeteria? pack/cafe: ')
#cost of groceries
groceries = input ('How much do your eggs cost?')
try:
    fmem = float (members)
    fres = float (restaurant)
    ffri = float (friends)
    fdat = float (datenight)
    fpiz = float (pizza)
    fpi2 = float (pizz2)
    fsch = float (schlunch)
    fwrk = float (wrklunch)
    fgro = float (groceries)
except:
    print ('You failed to input only numbers where it asked for numbers.')
    exit()
#Define general variables and calculate number of meals in the month
if month == 'Jan' or 'Mar' or 'May' or 'Jul' or 'Aug' or 'Oct' or 'Dec':
    days = 31
elif month == 'Feb':
    days = 28
else:
    days = 30
if month == 'Jan' or 'Mar' or 'May' or 'Jul' or 'Aug' or 'Oct' or 'Dec':
    wkdays = 23
elif month == 'Feb':
    wkdays = 20
else:
    wkdays = 22
mealspermonth = fmem * days * 3
print ('Your household will eat about', mealspermonth, 'meals this month.')
print ('These meals will have different costs based on various factors.')
print ('The costs declared here are estimates based on US averages in 2022.')
print ('These estimates are to help you determine if your income is sufficient.')
#calculate Restaurant costs and output variable for number of meals eaten at restaurants
restmpm = (fmem * fres) + (fdat * 2) + ffri
costrestmpm = restmpm * (24 + (restmpm * 24 / 100 * 15))
print ('You will spend about $', costrestmpm, 'at restaurants this month.')
#calculate pizza budget and output variable representing number of individual meals which were pizza
pizzacost = fpiz * 20
takeout = fpi2 * fmem
print ('You will spend about $', pizzacost, 'on Pizza this month.')
#if lunches are packed count them as home meals, otherwise calculate cost and subtract total lunches from home meals
meelswkdayz = wkdays * (fsch + fwrk)
if packlunch == 'cafe':
    wrkcafelunchcost = 6.99 * wkdays * fwrk
    schcafelunchcost = 3.1 * wkdays * fsch
    print ('Your work cafeteria food costs this month are $', wrkcafelunchcost)
    print ('Your school cafeteria food costs this month are $', schcafelunchcost)
else:
    wrkcafelunchcost = 0
    schcafelunchcost = 0
    print ('You saved a dollar-fity per meal per person by packing lunches.')
    print ('That adds up quickly, considering that you have', meelswkdayz, 'meals away from home this month.')
#calculate number of meals eaten at home and cost of groceries
if packlunch == 'cafe':
    noncookinstances = restmpm + takeout + meelswkdayz
else:
    noncookinstances = restmpm + takeout
if fgro > 3.99:
    homemealscost = 5.75
else:
    homemealscost = 3.75
homemealsnumber = mealspermonth - noncookinstances # subtract all the instances of eating without cooking
homemealscosttotal = homemealscost * homemealsnumber
print ('You will eat', homemealsnumber, 'home-cooked meals this month.')
print ('To prepare these home-cooked meals you will need about $', homemealscosttotal, 'worth of groceries.')
#Calculate total food costs
totalfoodcost = homemealscosttotal + schcafelunchcost + wrkcafelunchcost + pizzacost + costrestmpm
print ('Your total food costs this month are about $', totalfoodcost)
if totalfoodcost > cash:
    print ('Insufficient funds.')
else:
    print ('You are making it work.')
print ('<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>-<=>')
print ('While the love of money is the root of all evil - it really seems that the lack of')
print ('money is the root of all suffering. See you later', nam, '- call me if you need me.')
