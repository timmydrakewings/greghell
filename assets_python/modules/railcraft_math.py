import pandas as pd

from modules import useful_functions as uf

def tank_math():
    width = int(input("What is the width?"))
    depth = int(input("What is the depth?"))
    height = int(input("What is the height?"))
    capMod = int(input("How many buckets per block?"))
    wall = (2*(depth*width))+((height-2)*4)-1
    gauge = (2*((height-2)*(width-2)))+(2*((height-2)*(depth-2)))-1
    capacity = (width*height*depth)*capMod*1000
    print(uf.to_stack_str(wall) + " walls and " + uf.to_stack_str(gauge) + " gauges and 2 valves. Capacity is " + f"{capacity:,d}")

# ---------------

timeTicks = pd.Series(
    [1, 20, 1200, 72000, 1728000],
    index = ["tick", "second", "minute", "hour", "24-hour"]
)
boilerVars = pd.DataFrame({
    "Shape": ["1x1x2", "2x2x3", "2x2x4", "3x3x3", "3x3x4", "3x3x5"],
    "Size": [1, 8, 12, 18, 27, 36],
    "LP": [0.66875, 5, 7.2, 10.125, 13.66875, 16.2],
    "HP": [1.5875, 12, 17.4, 24.75, 34.0875, 41.4]
})
ovenProd = pd.Series(
    [0.0005556, 0.0000617, 0.0001389, 0.0001389],
    index = ["charcoal", "block of charcoal", "creosote", "creosote bucket"]
)
fuelTimes = pd.Series(
    [1600, 16000, 6400, 6400],
    index = ["charcoal", "block of charcoal", "creosote", "creosote bucket"]
)

def boiler_math():
    pressure = uf.selectFromList(["LP", "HP"])
    boilerSize = uf.selectFromList(boilerVars['Shape'].tolist())
    timeFrame = "hour"                                              #uf.selectFromList(timeTicks.index.to_list())
    fuelType = uf.selectFromList(ovenProd.index.to_list())
    numBoilers = 1                                                  #int(input("How many boilers?"))
    numWater = int(input("How many water tanks?"))
    numOvens = int(input("How many coke ovens?"))
    rainMod = 0.8                                                   #float(input("What is the rain modifier?"))
    solidWater, solidSteam, waterProd = boiler_vars(boilerSize, timeFrame, fuelType, numBoilers, numWater, numOvens,rainMod, pressure)
    liquidWater, liquidSteam, waterProd = boiler_vars(boilerSize, timeFrame, 'creosote', numBoilers, numWater, numOvens,rainMod, pressure)
    totalWater = waterProd-(solidWater+liquidWater)
    totalSteam = solidSteam+liquidSteam
    print("Total Water Difference: " + f"{totalWater:,d}" + " and Total Steam Production: " + f"{totalSteam:,d}")

def boiler_vars(boilerSize, timeFrame, fuelType, numBoilers, numWater, numOvens, rainMod, pressure):
    tanks = boilerVars.loc[boilerVars['Shape'] == boilerSize, 'Size'].iloc[0]
    lpMod = boilerVars.loc[boilerVars['Shape'] == boilerSize, pressure].iloc[0]
    numTicks = timeTicks.loc[timeFrame]
    burnTime = fuelTimes.loc[fuelType]
    fuelConsumption = lpMod*numTicks/burnTime*numBoilers
    steamProduction = tanks*numTicks*10*numBoilers
    waterConsumption = steamProduction/150
    ovenProduction = ovenProd.loc[fuelType]*numTicks*numOvens
    waterProduction = numWater*rainMod*1.25*numTicks
    fuelDifference = ovenProduction-fuelConsumption
    waterDifference = waterProduction-waterConsumption
    print("For " + fuelType + " use")
    print("Fuel Difference: " + str(fuelDifference) + "\nWater Difference: " + str(waterDifference) + "\nSteam Production: " + str(steamProduction))
    return int(waterConsumption), int(steamProduction), int(waterProduction)

# ---------------

def coke_oven_blocks(num):
    blocks = num * 36
    bricks = blocks * 4
    mats = bricks/2
    print("Num blocks: " + uf.to_stack_str(blocks) + "\nNum bricks: " + uf.to_stack_str(bricks) + "\nNum sand and clay: " + uf.to_stack_str(mats))