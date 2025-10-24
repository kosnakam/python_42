from typing import Any


def all_thing_is_obj(object: Any) -> int:

	ft_dict = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: f"{object}" " is in the kitchen"
	}

	ft_type = type(object)

	if ft_type in ft_dict:
		print(ft_dict[ft_type], ":", ft_type)
	else:
		print("Type not found")
	
	return 42