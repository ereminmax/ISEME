def print_two(*args):
    arg1,arg2=args
    print "arg1: %r, arg2: %r"%(arg1,arg2)
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r"%(arg1,arg2)
def print_one(arg1):
    print "arg1: %r"%arg1
def print_none():
    print "Nothin\'"
print_none()
print_one("Max")
print_two("Super", "Coder")
print_two_again("Nice", "Person")
