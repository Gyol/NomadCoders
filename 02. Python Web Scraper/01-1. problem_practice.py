dictionary = {}


def add_to_dict(dict_name, food, desc=None):
    if type(dict_name) == str:
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif desc is None:
        print("You need to send a word and a definition")
    else:
        if food not in dict_name.keys():
            dict_name[food] = desc
        else:
            print(f"{food} is already on the dictionary. Won't add")


def get_from_dict(dict_name, food=None):
    if type(dict_name) == str:
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif food is None:
        print("You need to send a word to search for.")
    else:
        if food not in dict_name.keys():
            print(f"{food} was not found in this dict.")
        else:
            print(f"{food}: {dict_name[food]}")

def update_word(dict_name, food, desc=None):
    if type(dict_name) == str:
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif desc is None:
        print("You need to send a word and a definition to update.")
    else:
        if food not in dict_name.keys():
            print(f"{food} is not on the dict. Can't update non-existing word.")
        else:
            dict_name[food] = desc
            print(f"{food} has been updated to: {dict_name[food]}")

def delete_from_dict(dict_name, food=None):
    if type(dict_name) == str:
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif food is None:
        print("You need to specify a word to delete.")
    else:
        if food not in dict_name.keys():
            print(f"{food} is not in this dict. Won't delete")
        else:
            del dict_name[food]
            print(f"{food} has been deleted.")





add_to_dict("hi", "Gyol")
add_to_dict(dictionary, "Gyol")
add_to_dict(dictionary, "Gyol", "Girl")
add_to_dict(dictionary, "Gyol", "Boy")
print()
get_from_dict("hi", "Gyol")
get_from_dict(dictionary)
get_from_dict(dictionary, "Ming")
get_from_dict(dictionary, "Gyol")
print()
update_word("hi", "Gyol")
update_word(dictionary, "Gyol")
update_word(dictionary, "Ming", "Boy")
update_word(dictionary, "Gyol", "Boy")
get_from_dict(dictionary, "Gyol")
print()
delete_from_dict("hi", "Gyol")
delete_from_dict(dictionary)
delete_from_dict(dictionary, "Ming")
delete_from_dict(dictionary, "Gyol")
get_from_dict(dictionary, "Gyol")