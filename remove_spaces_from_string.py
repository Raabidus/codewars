#  function that removes the spaces from the string, then return the resultant string
def no_space(x):
    x_list = []
    new_string = ""
    x_list = x.rsplit(" ")
    return new_string.join(x_list)