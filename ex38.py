ten_things = "Apples oranges crows telephone light sugar"
print "Lets fix an amount of fruits"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee"]
while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
