form="%r %r"
print form%("one", "two")
print form%(True,False)
print form%(form, form)
print form%(
    "One",
    "Two"
)
