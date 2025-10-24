from typing import Any


def NULL_not_found(object: Any) -> int:

	if (object == None):
		print("Nothing", ": ", object, " ", type(object), sep='')
	elif (object != object):
		print("Cheese", ": ", object, " ", type(object), sep='')
	elif (object == 0 and type(object) == int):
		print("Zero", ": ", object, " ", type(object), sep='')
	elif (object == '' and type(object) == str):
		print("Empty", ": ", object, type(object), sep='')
	elif (object == False and type(object) == bool):
		print("Fake", ": ", object, " ", type(object), sep='')
	else:
		print("Type not found")
		return 1
	return 0
