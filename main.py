import math 

#labour, costs and markups
labourCost = 10 # fixed labour cost NZD
standard = 1.20 #white or black
other = 1.40
printerCost = 400 # NZD
expectedLife = 8000 # hours 

#elctricity cost
powerCost = 0.24 #price per kW
printerPowerUse = 0.2 # kW

#fillament prices per kg
pla = 45/1000 #convert to price per grams
abs = 45/1000
tpu = 65/1000


def calcMaterial(type, weight, colour):

    #calc raw material cost
    if type == "pla":
        preCost = float(weight)*pla
    if type == "abs":
        preCost = float(weight)*abs
    if type == "tpu":
        preCost = float(weight)*tpu
    if type != "pla" and type != "abs" and type != "tpu":
        return 0 

    #calc markup
    if colour == "white" or colour == "black":
        cost = preCost*standard

    if colour != "black" or colour != "white":
        cost = preCost*other

    return cost

def calcPrinterCost(time):
    hourRate = (printerPowerUse * powerCost + (printerCost/expectedLife))
    cost = float(hourRate) * float(time)
    
    return cost

while True:
    type = input("Material type: ")
    weight = input("Weight (grams): ")
    colour = input("colour: ")
    printTime = input("Print time (hours): ")

    material = calcMaterial(type, weight, colour)
    printer = calcPrinterCost(printTime)
    
    if material != 0:
        print("")
        print("Results: ")
        print("---------")
        print("Material Cost: $",round(material, 2))
        print("Printing costs: $",round(printer, 2))
        print("Labour: $",labourCost)
        
        totalCost = (material + printer + labourCost)
        print("Total cost: $", round(totalCost, 2))
        print("")
        wait = input("Press enter to continue...")

    else: 
        print("Materials or colour not available!")
        print("Email howellsamuel101@gmail.com for a custom price.")

