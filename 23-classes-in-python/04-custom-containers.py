# Creating Custom Containers
class TagCloud:
	def __init__(self):
		self.__tags = {}
	# def __str__(self):
	# 	return f"{self}"

	def add(self, tag):
		self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
	# Defines behavior for when an item is accessed, using the notation self[key]. This is also part of both the mutable and immutable container protocols.
	def __getitem__(self, tag):
		return self.__tags.get(tag.lower(), 0)

	def __setitem__(self, key, value):
		self.__tags[key.lower()] = value

	def __len__(self):
		return len(self.__tags)

	def __iter__(self):
		return iter(self.__tags)

cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("PYTHON")
print(cloud["PYTHon"])

# private attribute .__tags
print(cloud.__tags)