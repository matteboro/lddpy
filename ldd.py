from constraint import *
import numpy as np

node_counter = 0

class ldd_node:
    def __init__(self, cons, _then = None, _else = None):
        if isinstance(cons, str):
            self.cons = constraint(cons)
        else:
            self.cons = cons
        self._then = _then
        self._else = _else
        global node_counter
        self.id = node_counter
        node_counter += 1


# an ldd_node could hold a constant value to signify true or false
# a constant ldd_node will have a constraint with a special variable CONS_VAR
# the cst value of the constraint will contain the value of node:
# - 0 for a false node
# - n != 0 for a true node
CONS_VAR = 1000

def set_children(node, _then, _else):
    if isinstance(node, ldd_node) and  isinstance(_then, ldd_node) and isinstance(_else, ldd_node):
        node._then = _then
        node._else = _else
        return node
    else:
        print("ERROR in set_children(node, _then, _else): one of the object is not an ldd_node")

def set_else_child(node, _else):
    if isinstance(node, ldd_node) and isinstance(_else, ldd_node):
        node._else = _else
        return node
    else:
        print("ERROR in set_else_child(node, _else): one of the object is not an ldd_node")


def set_then_child(node, _then):
    if isinstance(node, ldd_node) and isinstance(_then, ldd_node):
        node._then = _then
        return node
    else:
        print("ERROR in set_then_child(node, _then): one of the object is not an ldd_node")


def then_child(node):
    if isinstance(node, ldd_node):
        return node._then
    else:
        print("ERROR in then_child(node): object passed is not an ldd_node")
        exit(1)

def else_child(node):
    if isinstance(node, ldd_node):
        return node._else
    else:
        print("ERROR in else_child(node): object passed is not an ldd_node")
        exit(1)

def var(obj):
    if isinstance(obj, ldd_node):
        return obj.cons.var
    elif isinstance(obj, constraint):
        return obj.var
    else:
        print("ERROR in var(obj): object passed is not an ldd_node or a constraint")
        exit(1)
  
def is_constant(obj):
    if isinstance(obj, ldd_node):
        return obj._else == None and obj._then == None and is_constant(obj.cons)
    elif isinstance(obj, constraint):
        return obj.var == CONS_VAR
    else:
        print("ERROR in is_constant(obj): object passed is not an ldd_node or a constraint")
        exit(1)

# these functions respectively create and check whether a node
# is true/false

def false_node():
    return ldd_node(constraint(CONS_VAR, None, 0))

def true_node():
    return ldd_node(constraint(CONS_VAR, None, 1))

def is_false(node):
    if isinstance(node, ldd_node):
        return is_constant(node) and node.cons.cst == 0
    else:
        print("ERROR in is_false(node): object passed is not an ldd_node")
        exit(1)

def is_true(node):
    if isinstance(node, ldd_node):
        return is_constant(node) and node.cons.cst != 0
    else:
        print("ERROR in is_false(node): object passed is not an ldd_node")
        exit(1)

# this method create a deep copy of an ldd
def copy_ldd(ldd):
    if (is_constant(ldd)):
        if is_false(ldd):
            return false_node()
        else:
            return true_node()
    new_ldd = ldd_node(ldd.cons)
    new_ldd._else = copy_ldd(else_child(ldd))
    new_ldd._then = copy_ldd(then_child(ldd))
    return new_ldd

def satisfies_2d(ldd, x, y):
    if is_constant(ldd):
        return False if ldd.cons.cst == 0 else True
    else:
        if var(ldd) == 0:
            if satisfy_constraint(ldd.cons, x):
                return satisfies_2d(then_child(ldd), x, y)
            else:
                return satisfies_2d(else_child(ldd), x, y)
        elif var(ldd) == 1:
            if satisfy_constraint(ldd.cons, y):
                return satisfies_2d(then_child(ldd), x, y)
            else:
                return satisfies_2d(else_child(ldd), x, y)
        else:
            return False

def satisfies_2d_grid(ldd, from_x, to_x, from_y, to_y):

    x_size = to_x - from_x
    y_size = to_y - from_y

    grid = np.zeros((y_size, x_size), dtype=int)

    for i in range (from_x, to_x):
        for j in range(from_y, to_y):
            grid[y_size - 1 - (j - from_y), i - from_x] = True if satisfies_2d(ldd, i, j) else False
    
    return grid

# this method returns the list of unique indexes of the nodes that compose an ldd 
def list_of_indexes(ldd):
    if isinstance(ldd, ldd_node):
        if is_constant(ldd):
            return []
        else:
            then_list = list_of_indexes(then_child(ldd))
            else_list = list_of_indexes(else_child(ldd))
            my_list = list(set(then_list + else_list))
            if ldd.id not in my_list:
                my_list.append(ldd.id)
            return my_list
    else:
        print("ERROR in list_of_indexes(ldd): object passed is not an ldd_node")
        exit(1)

#this method checks wheter or not the two ldds share any nodes
# it does so checking the unique indexes of the nodes that compose the two ldds
def dont_share_ldd_nodes(ldd1, ldd2):
    ldd1_idxs = list_of_indexes(ldd1)
    ldd2_idxs = list_of_indexes(ldd2)
    for idx in ldd1_idxs:
        if idx in ldd2_idxs:
            return False
    return True
