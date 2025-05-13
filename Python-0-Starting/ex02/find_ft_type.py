def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : <class 'list'>")
    elif isinstance(object, tuple):
        print(f"Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print(f"Set : <class 'set'>")
    elif isinstance(object, dict):
        print(f"Dict : <class 'dict'>")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42