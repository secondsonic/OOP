#Private and Public Classes extended from Tutorial #6
import Tutorial6

from Tutorial6 import NotPrivate

test = NotPrivate('Arsalan')

test.display()

#Although we consider _display() as private but still accessible
test._display()