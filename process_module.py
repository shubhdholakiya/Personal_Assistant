from output_module import output
from time_module import get_time


def process(query):
    if "what is the time" in query:
        return ("Time is "+get_time())
    else:
        return "Sorry I didn't found time."
