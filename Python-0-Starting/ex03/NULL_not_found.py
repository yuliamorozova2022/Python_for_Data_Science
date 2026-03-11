def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and object != object:
        # isinstance(object, float) - is float AND only after
        # that object is 'nan' with object != object (nan != nan)
        print("Cheese: nan <class 'float'>")
    elif object is False:
        # bool type by default
        # important to check this before int case - cos bool is subtype of int
        print("Fake: False <class 'bool'>")
    elif isinstance(object, int) and object == 0:
        print("Zero: 0 <class 'int'>")
    elif isinstance(object, str) and object == '':
       print("Empty: <class 'str'>")
    else:
        print("Type not Found")
        return 1
    return 0