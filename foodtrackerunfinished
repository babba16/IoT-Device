#new day should begin at breakfast 
def foodtracker(newday, newfeedingtime, foodlefttobedispensedday, foodlefttobedispensedmeal, previousfoodatstartofday, previousfoodatstartofmeal)
    if newday = true #thecase for a new day starting, resets amount of food to be dispensed for day to max
        foodatstartofday =  normalise # food left over at beginning of day from previous
        print ("Food from the last day not dispensed was")
        print (foodlefttobedispensedday)
        print ("previous day dog ate") 
        print (previousfoodatstartofday + (3-foodlefttobedispensedday) - foodatstartofday)
        foodtobedispensed = 3     #totalamountoffoodtobedispensedforday #set to 3 for now but should be a variable "max"
    else
        foodatstartofday = previousfoodatstartofday
        foodtobedispensed = foodlefttobedispensedday
    if newfeedingtime = true  # new feeding time e.g breakfast/lunch/ dinner
        foodatstartofmeal = normalize
        print ("Food from the last meal not dispensed was")
        print (foodlefttobedispensedmeal)
        print ("Food left in bowl at start of the new meal was")
        print (foodatstartofmeal)
        print ("previous meal dog ate")
        print (previousfoodatstartofmeal + (1-foodlefttobedispensedmeal) - foodatstartofmeal)
        foodtogivethismeal = 1 #need to save how much food was dispensed #should be max/3
        
    else
        foodatstartofmeal = previousfoodatstartofmeal
        foodtogivethismeal = foodlefttobedispensedmeal
        
    fooddispensed = dispensefood(foodtogivethismeal) # fucntion for dispensing food, it takes in as input the food left to be dispensed for this meal
    foodtogivethismeal = foodtogivethismeal - fooddispensed #equals amount left to be dispensed after the dispense.
    foodtobedispensed = foodtobedispensed - fooddispensed  #lefttobedispensed for day
    
    return [foodtogivethismeal, foodtobedispensed, foodatstartofmeal, foodatstartofday]
        
def dispensefood(foodtogive) #dispensesfood(up to limit)and returns how much dispensed 
    initialbowl = normalise # this curretn weight of bowl
    while normalise < 1 && 1 - normalise > foodtogive # only dispense if bowl is not full and space left in bowl is greater than foodtogive
        #turn motor on to dispense need to write this when we have output
    return totaldispensed= normalise - initialbowl #this is the total dispensedintothebowl
    
def normalise #ask sensor for data and normalise into 1 unit = max weight of bowl
    
        
        
    
        



