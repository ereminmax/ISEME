def secret_formula(started):
    jelly_beans=started*500
    jars =jelly_beans/1000
    crates =jars/100
    return jelly_beans,jars, crates
start_point =100000
start_point=start_point/10
beans,jars,crates=secret_formula(start_point)
print "Staring point %d"%start_point
print "We have %d beans, %d jars, and %d crates"%(beans,jars,crates)
