dic = {1 : "you will die before 90", 2 : "when the clock stikes 12 you will want water", 3 : "you will act out your first thought", 4 : "look to you left4", 5 : "only go right to win", 6 : "fortune6", 7 : "fortune7", 8 : "f8", 9 : "f9", 10 : "f10", 11 : "f11", 12 : "f12", 13 : "f13", 14 : "f14", 15 : "f15", 16 : "f16", 17 : "f17", 18 : "f18", 19 : "f19", 20 : "f20"}



def fortuneteller(number):
    for number in dic:
        if number > 20:
            return "pick a number less or equal to 20"
        else:
            return dic[number]
#fortuneteller(3)

#def fortuneteller(name):
  #name = list(name)
##  count = 0
  #for x in name:
    #count += 1
 # if count <= 20:
#    return count
  #else:
#    return "over"

#key = fortuneteller(input)

#output = dictionary.get(key)
