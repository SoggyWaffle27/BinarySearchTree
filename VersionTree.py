from friendsbalt.acs import AVLTree,  StringDiff, OrderedMap

class Node:
    def __init__(self, a):
        self.a = a

SD = StringDiff

a = ""
b = SD.deserialize(Node("a"))

#StringDiff.serialize(
diff = SD.raw_diff(a, b)
print(diff)
#StringDiff.apply_diff(a, diff)

#run forever
# om[:time]
# Store 
# restore
# log
# version history