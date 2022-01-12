import math 

#labour, costs and markups
labourCost = 10 # fixed labour cost NZD
printerCost = 400 # NZD
expectedLife = 8000 # hours 

#colour markups
standard = 1.50 #white or black
grey = 1.6
other = 1.8

#elctricity cost
powerCost = 0.24 #price per kW
printerPowerUse = 0.2 # kW

#fillament prices per kg
pla = 45/1000 #convert to price per grams
abs = 45/1000
tpu = 65/1000

#shipping
south = 10
auckland = 10
north = 10

#function to calculate material cost
def calcMaterial(type, weight, colour):

    #calc raw material cost
    if type == "pla":
        preCost = float(weight)*pla

    if type == "abs":
        preCost = float(weight)*abs

    if type == "tpu":
        preCost = float(weight)*tpu

    if type != "pla" and type != "abs" and type != "tpu":
        customFillPrice = float(input("Enter cost of fillament per KG: "))
        markup = float(customFillPrice)/30
        cost = float(weight)*float(markup)*(customFillPrice/1000)
        return cost #dosnt markup colours on custom fill as already high markup.

    #calc markup
    if colour == "white" or colour == "black":
        cost = preCost*standard

    if colour == "grey":
        cost = preCost*grey 

    if colour != "black" or colour != "white" or colour != "grey":
        cost = preCost*other

    return cost
    else return 0

#function to calculate printer costs
def calcPrinterCost(time):

    hourRate = (printerPowerUse * powerCost + (printerCost/expectedLife))
    cost = float(hourRate) * float(time)
    
    return cost
    else return 0

#main loop
while True:

    postage = 0 
    #user inputs
    type = input("Material type: ")
    weight = input("Weight (grams): ")
    colour = input("colour: ")
    printTime = input("Print time (hours): ")
    shipping = input("is there shipping? (y/n): ")

    if shipping == "y":

        print("")
        print("Location codes:")
        print("----------------")
        print("Auckland: 1")
        print("Other north: 2")
        print("South Island: 3")
        print("")

        location = input("Enter location code: ")

        if location == "1":
            postage = auckland

        if location == "2":
            postage = north

        if location == "3":
            postage = south

    #call price functions
    material = calcMaterial(type, weight, colour)
    printer = calcPrinterCost(printTime)
    
    if material != 0 and printer != 0:
        print("")
        print("Results: ")
        print("---------")
        print("Material Cost: $",round(material, 2))
        print("Printing costs: $",round(printer, 2))
        print("Labour: $",labourCost)
        
        if postage != 0:
            print("Shipping: $", postage)

        print("")
        totalCost = (material + printer + labourCost + postage)
        print("Total cost: $", round(totalCost, 2))
        print("")
        wait = input("Press enter to continue...")

    else: 
        print("Materials or colour not available!")
        print("Email howellsamuel101@gmail.com for a custom price.")

