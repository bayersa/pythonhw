# Python Homework 1

## Exercise 1: print() function

### Exercise 1-a
# Replace "type here" on line 2 with "Hello World!"
```
{
    print("Hello World!")

}
```

### Exercise 1-b
# You can assign "Hello World!" to the variable below on line 3.
```
{
    my_text="Hello World!"
    
    print(my_text)

}
```

## Exercise 2: Variables
### Exercise 2-a
# Type here. Assign a number to the variable: glass_of_water
```
{
    glass_of_water=3
    
    print("I drank", glass_of_water, "glasses of water today.")

}
```

### Exercise 2-b
# Fill the print function so it prints glass_of_water
```
{
    glass_of_water=3
    
    glass_of_water=glass_of_water + 1
    
    print(glass_of_water)

}
```

## Exercise 3: Data Types
### Exercise 3-a
# Assign an integer to the variable, then print it.
```
{
    men_stepped_on_the_moon= 12
    
    print(men_stepped_on_the_moon)

}
```

### Exercise 3-b
# Type a couple of words or a short sentence for your variable, then print it.
```
{
    my_reason_for_coding="Learn for school"
    
    print(my_reason_for_coding)

}
```

### Exercise 3-c
# Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.
```
{
    global_mean_sea_level_2018=21
    
    global_mean_sea_level_2018=21.36
    
    print(global_mean_sea_level_2018)

}
```

## Exercise 9: Strings
### Exercise 9-a
# Assign the string below to the variable in the exercise "It's always darkest before dawn." Type your answer here.
```
{
    str="It's always darkest before dawn."
    
    print(str)

}
```

### Exercise 9-b
# By using first, second and last characters of the string, create a new string.
```
{
    str="It's always darkest before dawn."
    
    ans_1=str[0]+str[1]+str[-1]
    
    print(ans_1)

}
```

### Exercise 9-c
# Replace the (.) with (!)
```
{
    str="It's always darkest before dawn."
    
    str = str.replace(".","!")
    
    print(str)

}
```

## Exercise 10: len() function
### Exercise 10-a
# Using len() function find out how many items are in the list.
```
{
    lst=[11, 10, 12, 101, 99, 1000, 999]
    
    answer_1=len(lst)
    
    print(answer_1)

}
```

### Exercise 10-b
# len() function can also tell the length of a string. Find out the length of the string given below.
```
{
    msg="Be yourself, everyone else is taken."
    
    msg_length=len(msg)
    
    print(msg_length)

}
```

### Exercise 10-c
# How many keys are there in the dictionary?
```
{
    dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
    
    ans_1=len(dict)
    
    print(ans_1)

}
```

## Exercise 11: .sort() method
### Exercise 11-a
# Sort the list in ascending order with .sort() method.
```
{
    lst=[11, 100, 99, 1000, 999]
    
    lst.sort()
    
    print(lst)

}
```

### Exercise 11-b
# This time sort the countries in alphabetic order.
```
{
   lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
   
   lst.sort()
   
   print(lst) 

}
```

### Exercise 11-c 
# Now sort the list in descending order with .sort() method.
```
{
    lst=[11, 100, 101, 999, 1001]
    
    lst.sort(reverse = True) 
    
    print(lst)

}
```

## Exercise 12: .pop() method 
### Exercise 12-a
# Pop the last item of the list below.
```
{
    lst=[11, 100, 99, 1000, 999]
    
    popped_item=lst.pop()
    
    print(popped_item)
    print(lst)
}
```

### Exercise 12-b
# Remove "broccoli" from the list using .pop and .index methods.
```
{
    lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
    
    a=lst.index("broccoli")
    
    item=lst.pop(a)
    
    print(lst, item)

}
```

### Exercise 12-c
# Save Italy's GDP in a separate variable and remove it from the dictionary.
```
{
    GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
    
    italy_gdp=GDP_2018.pop("Italy")
    
    print(GDP_2018)
    print(italy_gdp, "trillion USD")
}
```