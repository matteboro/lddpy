from ldd_split import *
from ldd_visualization import *
import graphviz

def ASSERT_TYPES(objs, types, func_name):
    for i, (obj, _type) in enumerate(zip(objs, types)):
        if not isinstance(obj, _type):
            print(f"ERROR in function {func_name}: parameter number {i} \
                  is not of type {_type.__name__} \
                  but of type {obj.__class__.__name__}")
            exit(1)

def SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, case):
    print(f"   SPLIT GRID ERROR at coordinates ({x}, {y}), values: [ before: {before_val}, pos:{pos_val}, neg:{neg_val} ] in case: {case}")
    return False

def SPLIT_SHARE_NODES_ERROR(pos_ldd, neg_ldd):
    print(f"   SPLIT SHARE NODES ERROR")
    dump_ldd_dot(pos_ldd)
    dump_ldd_dot(neg_ldd)
    return False

def check_split_grid(from_x, to_x, from_y, to_y, before, pos, neg, cons):
    ASSERT_TYPES([before,     pos,        neg,        cons], 
                 [np.ndarray, np.ndarray, np.ndarray, constraint], 
                 "check_split(before, pos, neg, constraint)")
    
    if cons.var > 1 or cons.var < 0:
        print("ERROR in check_split: constraint is not fo variable 0 or 1")
        exit(1)

    if not is_std_form(cons):
        cons = complement(cons)
        tmp = pos
        pos = neg
        neg = tmp
    
    if cons.var == 0 and (cons.cst > to_x or cons.cst <= from_x):
        print(f"ERROR in check_split: cons.cst is {cons.cst} which is out of bound of the x axis range [{from_x}, {to_x}]")
    if cons.var == 1 and (cons.cst > to_y or cons.cst <= from_y):
        print(f"ERROR in check_split: cons.cst is {cons.cst} which is out of bound of the y axis range [{from_y}, {to_y}]")

    x_size = to_x - from_x
    y_size = to_y - from_y

    for x in range (from_x, to_x):
        for y in range(from_y, to_y):
            x_idx = x - from_x
            y_idx = y_size - 1 - (y - from_y)
            before_val = before[y_idx, x_idx]
            pos_val = pos[y_idx, x_idx]
            neg_val = neg[y_idx, x_idx]
            if cons.var == 0:
                if x >= cons.cst:
                    if not (neg_val == False and pos_val == before_val):
                        return SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, f"x >= cons.cst")
                else:
                    if not (pos_val == False and neg_val == before_val):
                        return SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, f"x < cons.cst")
            elif cons.var == 1:
                if y >= cons.cst:
                    if not (neg_val == False and pos_val == before_val):
                        return SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, f"y >= cons.cst")
                else:
                    if not (pos_val == False and neg_val == before_val):
                        return SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, f"y < cons.cst")
    return True

def check_split(x_range, y_range, ldd, cons):
    from_x, to_x = x_range
    from_y, to_y = y_range
    before = satisfies_2d_grid(ldd, from_x, to_x, from_y, to_y)
    pos_ldd, neg_ldd = split(ldd, cons)
    pos = satisfies_2d_grid(pos_ldd, from_x, to_x, from_y, to_y)
    neg = satisfies_2d_grid(neg_ldd, from_x, to_x, from_y, to_y)

    if not check_split_grid(from_x, to_x, from_y, to_y, before, pos, neg, cons):
        return False
    if not dont_share_ldd_nodes(pos_ldd, neg_ldd):
        return SPLIT_SHARE_NODES_ERROR(pos_ldd, neg_ldd)
    return True

def test(x_range, y_range, ldd, cons):
    if not check_split(x_range, y_range, ldd, cons):
        print(f"test number {TEST_NUMBER} failed on constraint: {string_constraint(cons)}") 
    else:
        print(f"test number {TEST_NUMBER} passed")

def show_split_2d(x_range, y_range, ldd, cons):
    show_ldd_2d(ldd, x_range, y_range, f"ldd before constraint {string_constraint(cons)}")
    pos_ldd, neg_ldd = split(ldd, cons)
    show_ldd_2d(pos_ldd, x_range, y_range, f"positive ldd after constraint {string_constraint(cons)}")
    show_ldd_2d(neg_ldd, x_range, y_range, f"negative ldd after constraint {string_constraint(cons)}")

# this method create a new ldd with only one variable on two levels 
def one_var_depth_2_ldd(var):
    return ldd_node(constraint(f"v{var} >= 6"), 
                ldd_node(constraint(f"v{var} >= 9"),
                    false_node(),
                    true_node()), 
                ldd_node(constraint(f"v{var} >= 3"),
                    false_node(),
                    true_node()))

def two_var_depth_1_ldd():
    return ldd_node(constraint(f"v0 >= 6"), 
                ldd_node(constraint(f"v1 >= 6"),
                    true_node(),
                    false_node()), 
                ldd_node(constraint(f"v1 >= 6"),
                    false_node(),
                    true_node()))

def save_dot_ldd(ldd, format="pdf", name=""):
    dot_string = dump_ldd_dot(ldd, do_print=False)
    dot = graphviz.Source(dot_string)
    dot.render(f'dot_output/ldd{name}.gv', format=format).replace('\\', '/')

X = 0
Y = 1

x_range = (0, 12)
y_range = (0, 12)

# test cases where the variable of the constraint is not present in the ldd

TEST_NUMBER = 0

ldd_only_x_depth_2 = one_var_depth_2_ldd(X)
cons = constraint(f"v1 <= 6")
test(x_range, y_range, ldd_only_x_depth_2, cons)

TEST_NUMBER = 1

ldd_only_x_depth_2 = one_var_depth_2_ldd(X)
cons = constraint(f"v1 >= 6")
test(x_range, y_range, ldd_only_x_depth_2, cons)

TEST_NUMBER = 2

ldd_only_y_depth_2 = one_var_depth_2_ldd(Y)
cons = constraint(f"v0 >= 6")
test(x_range, y_range, ldd_only_y_depth_2, cons)

TEST_NUMBER = 3

ldd_only_y_depth_2 = one_var_depth_2_ldd(Y)
cons = constraint(f"v0 <= 6")
test(x_range, y_range, ldd_only_y_depth_2, cons)

# test cases where the variable of the constraint is only on the root node

# constraint in std form

TEST_NUMBER = 4

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 10")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 5

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 7")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 6

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 6")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 7

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 5")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 8

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 2")
test(x_range, y_range, ldd_2_var_depth_1, cons)

# constraint not in std form

TEST_NUMBER = 9

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 <= 10")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 10

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 <= 6")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 11

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 <= 5")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 12

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 4")
test(x_range, y_range, ldd_2_var_depth_1, cons)

TEST_NUMBER = 13

ldd_2_var_depth_1 = two_var_depth_1_ldd()
cons = constraint(f"v0 >= 2")
test(x_range, y_range, ldd_2_var_depth_1, cons)

"""
print("cons: " + string_constraint(cons) + 
      "\ncons_else: " + string_constraint(else_child(ldd_2_var_depth_1).cons) + 
      "\ncons_if: " + string_constraint(ldd_2_var_depth_1.cons) + 
      "\ncons_then: " + string_constraint(then_child(ldd_2_var_depth_1).cons))

print(split_choose_side(cons, else_child(ldd_2_var_depth_1).cons, ldd_2_var_depth_1.cons, then_child(ldd_2_var_depth_1).cons))

ldd_2_var_depth_1 = two_var_depth_1_ldd()
# show_split_2d(x_range, y_range, ldd_2_var_depth_1, cons)
save_dot_ldd(ldd_2_var_depth_1, name="before")
pos_ldd, neg_ldd = split(ldd_2_var_depth_1, cons)
save_dot_ldd(pos_ldd, name="pos")
save_dot_ldd(neg_ldd, name="neg")
"""