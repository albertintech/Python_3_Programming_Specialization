"""When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change. We can see this happen in the following nested list, which only has two levels."""

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print("original: ", original)
print("copied_version", copied_version)
print("Original object id: ", id(original))
print("copied_version object id: ", id(copied_version))
print("copied_version is original? ", copied_version is original)
print("copied_version == original?", copied_version == original)
original[0].append(["canines"])
print("append 'canines' to original, now: ", original)
print("-------- Now look at the copied version -----------")
print("copied_version", copied_version)
