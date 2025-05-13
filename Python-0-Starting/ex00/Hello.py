ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list
ft_list.remove("tata!")
ft_list.append("World!")
#tuple 
#is immutable. needs converstion to list, modification and than back to tuple
tmp = list(ft_tuple)
tmp.remove("toto!")
tmp.append("Czechia!")
ft_tuple = tuple(tmp)
# print(ft_tuple)
#set
# print(ft_set)
ft_set.remove("tutu!")
# print(ft_set)
ft_set.add("Praha!")
# print(ft_set)
#dictionary
ft_dict["Hello"] = "42Prague!"


#printing
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)