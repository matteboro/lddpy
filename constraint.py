
# the only two operators permitted for constraints are >= and <=
GEQ = ">="
LEQ = "<="

class constraint:
    def __init__(self, var_or_string, op=None, cst=None):
        if isinstance(var_or_string, str):
            self.var, self.op, self.cst = constraint_parser(var_or_string)
        else:
            self.var = var_or_string
            self.op = op
            self.cst = cst

# string should be of the form: "[letter][number] [op] [constant]"
# ex. v10 <= 6, f4 >= 0
def constraint_parser(string):
    elems = string.split(" ")
    var = int(elems[0][1:])
    op = elems[1]
    cst = int(elems[2])
    return var, op, cst

def copy_cons(cons):
    return constraint(cons.var, cons.op, cons.cst)

# this method return wheter or not the constraint is satisfied
# if the variable would be substituted with x
def satisfy_constraint(cons, x):
    if cons.op == GEQ:
        return True if x >= cons.cst else False
    elif cons.op == LEQ:
        return True if x <= cons.cst else False

# standard form means the operator is >=
# the nodes of a ldd always contains constraints written in standard form

def is_std_form(cons):
    return cons.op == GEQ

def complement_if_not_std_form(cons):
    if is_std_form(cons):
        return cons   
    return constraint(cons.var, GEQ, cons.cst+1)

def complement(cons):
    if cons.op == GEQ:
        return constraint(cons.var, LEQ, cons.cst-1)
    elif cons.op == LEQ:
        return constraint(cons.var, GEQ, cons.cst+1)
    else:
        print("unreachable: method complement(cons)")
        exit(1)

def string_constraint(cons):
    return f"v{cons.var} {cons.op} {cons.cst}"

def print_constraint(cons):
    print(string_constraint(cons), end="")
