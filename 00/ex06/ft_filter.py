"""my own remake of filter implementation"""


def ft_filter(function, iterable):
	"""Return a list of items from iterable for which function is true."""
	if function is None:
		return [item for item in iterable if item]

	return [item for item in iterable if function(item)]
