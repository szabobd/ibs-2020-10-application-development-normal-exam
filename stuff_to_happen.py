from fish import Fish
from fish import Tang
from fish import Kong
from fish import Clownfish
from aquarium import Aquarium



a = Tang("Annácska", 3, "pink", True)
b = Kong("Benike", 9, "red")
c = Clownfish("Ceci", 2, "blue", "yellow")
d = Kong("Dögike", 12, "white")
e = Tang("Viktor", 6, "orange", False)
a.status()
a.feed()
a.status()

q = Aquarium()
q.add_fish(a)
q.add_fish(b)
q.add_fish(c)
q.add_fish(d)
q.add_fish(e)

q.get_status()
q.feed()
q.get_status()
q.remove_fish()
q.get_status()