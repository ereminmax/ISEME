input_file ='ex16_sample.txt'
def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_line(line_count, f):
    print line_count, f.readline()
current_file=open(input_file)
print_all(current_file)
rewind(current_file)
current_line=1
print_line(current_line, current_file)
current_line=current_line+1
print_line(current_line, current_file)
current_line=current_line+1
print_line(current_line, current_file)
