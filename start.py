# This is Self Learning Personal Assistant, it's name is Sam
from input_module import take_input
from process_module import process
from output_module import output
while True:
    i = take_input()
    o = process(i)
    output(o)


