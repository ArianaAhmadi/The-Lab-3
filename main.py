'''
#Function 1
def two_lists(n):
  list_1 = []
  list_2 = []
  for i in n:
    if i.isdigit() == True:
      list_1.append(i)
    else:
      list_2.append(i)
  print("Numbers List:")
  print(list_1)
  print("Words List:")
  return list_2

print(two_lists([(s) for s in input("Type in any letter and/or number sepereated by spaces:\n").split()]))
'''

'''
#Function 2
def numbers_list(n):
  for i in range(2, len(n), 2):
      list_1 = n.sort()
  return list_1

print(numbers_list([int(s) for s in input("Give list of numbers: ").split()]))
'''
'''
going down by one 
remeber that 1 ex2 a function where one of the return state wsas n*a()-1 something like that do tat for index but

#every second letter replsce with letter then arrange lowest to highest then once done then replace the letter b with th list we rearranged from lowest to highest and boom done
'''

############################
#This one is my fave because you can input six OR MORE and it will make it into decending order and we can just make a way where it effects every two, so [::2] or something like that\

def descend(n):
  even_list = []
  for i in n:
    if i % 2 == 0:
      even_list.append(i)
  for i in even_list:
    if i % 2 == 0:
      new_even_list = 
      even_list.replace(str(i), max(even_list))
  return new_even_list

print(descend([int(s) for s in input("Input any number: \n").split()]))