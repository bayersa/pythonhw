# Intro to Python 2 

## Rosalind HW
### Variables and Some Arithmetic
{
    a = 966
    b = 892
    a**2 + b**2 
    1728820
}

## Dictionary Exercises 

### Dictionaries 
#### Which one of these is a dictionary ?
##### x = {'type' : 'fruit', 'name' : 'banana'}

#### Can dictionary items be removed after theyu have been created? 
##### yes 

#### Can a Dictionary have two keys with the same name?
##### No 

#### Select the correct function to print the number of key/value pairs in the dictionary:
{
    x = {'type' : 'fruit', 'name' : 'banana'} 
    print(len(x))
}


### Access Dictitonaries 
#### True or False. You can access item values by referring to the key name.
##### True 

#### Use the get method to print the value of the "model" key of the car dictionary.
{
    car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
}
##### What is get? 

#### Consider the following code:
{ 
    x = {'type' : 'fruit', 'name' : 'banana'}
    print(x['type'])
}
#### What will be the printed result?
##### fruit 


### Change Dictionaries 
#### Consider the following code:
{
    x = {'type' : 'fruit', 'name' : 'banana'}
}
#### What is a correct syntax for changing the type from fruit to berry?
{
    x['type'] = 'berry'

}

#### Change the "year" value from 1964 to 2020.
{
    car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
}

#### Consider the following code:
{
    x = {'type' : 'fruit', 'name' : 'banana'}
}
#### What is a correct syntax for changing the name from banana to apple?
{
    x.update({'name': 'apple'})
}


### Add Dictionary Items 
#### Which one of these dictionary methods can be used to add items to a dictionary?
##### update()

#### Add the key/value pair "color" : "red" to the car dictionary.
{
    car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red" 
}
##### when do you use update? why didnt we use it here?

#### Insert the missing part to add an item to the dictionary.
{
    x = {'type' : 'fruit', 'name' : 'apple'}
    x.update({'color' :'green'})
}

### Remove Dictionary Items 
#### What is a dictionary method for removing an item from a dictionary?
##### pop()

#### Use the pop method to remove "model" from the car dictionary.
{
   car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
}

#### Use the clear method to empty the car dictionary.
{
    car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
    car.clear()
}

#### Insert a correct syntax for removing the 'color' item of the dictionary:
{
    myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
    
    del myvar('color')
}


## Slicing 
### Lesson 17: Slicing 
#### Exercise 17-a
##### Slice the word until first "a". (Tosc)
{
    wrd="Toscana"

    ans_1=(wrd[0:4])
    
    print(ans_1)

}

##### Exercise 17-b 
###### Slice the word so that you get "cana".
{
    wrd="Toscana"
    
    ans_1=(wrd[3:])
    
    print(ans_1)

}
