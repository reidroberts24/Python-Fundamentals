from ninja import Ninja
from pet import Pet



golden_retriever = Pet("Charlie", "dog", ["sit", "lay down", "fetch ball"])
dog_owner = Ninja("Caesar", "Milan", golden_retriever, "dog biscuits", "Purina One")

tabby_cat = Pet("Jones", "cat", ["pounce", "hunt", "sunbathe"])
cat_owner = Ninja("Jenny", "Matthews", tabby_cat, "cat food", "chopped liver")

dog_owner.feed().walk().bathe()
cat_owner.feed().walk().bathe()