ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list
ft_list.remove("tata!")
ft_list.append("World!")

# tuple
# is immutable. needs convertion to list, modification and then back to tuple
tmp = list(ft_tuple)
tmp.remove("toto!")
tmp.append("Czechia!")
ft_tuple = tuple(tmp)

# set
# Unordered!
ft_set.remove("tutu!")
ft_set.add("Praha!")

# dictionary
ft_dict["Hello"] = "42Prague!"

# printing
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)