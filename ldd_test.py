from ldd_split import *
from ldd_visualization import *

X = 0
Y = 1

def ASSERT_TYPES(objs, types, func_name):
    for i, (obj, _type) in enumerate(zip(objs, types)):
        if not isinstance(obj, _type):
            print(f"ERROR in function {func_name}: parameter number {i} \
                  is not of type {_type.__name__} \
                  but of type {obj.__class__.__name__}")
            exit(1)

def SPLIT_GRID_ERROR(x, y, before_val, pos_val, neg_val, case):
    print(f"SPLIT GRID ERROR at coordinates ({x}, {y}), values: [ before: {before_val}, pos:{pos_val}, neg:{neg_val} ] in case: {case}")
    return False

def SPLIT_SHARE_NODES_ERROR(pos_ldd, neg_ldd):
    print(f"SPLIT SHARE NODES ERROR")
    dump_ldd_dot(pos_ldd)
    dump_ldd_dot(neg_ldd)
    return False

def HAVE_FALSE_CHILDREN_ERROR(ldd, side, test_number):
    print(f"HAVE FALSE CHILDREN ERROR on {side} result")
    save_rendered_dot_ldd(ldd, name=f"_{side}_{test_number}")
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

def check_split(x_range, y_range, ldd, cons, test_number):
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
    if not dont_have_false_children(pos_ldd):
        return HAVE_FALSE_CHILDREN_ERROR(pos_ldd, "positive", test_number)
    if not dont_have_false_children(neg_ldd):
        return HAVE_FALSE_CHILDREN_ERROR(neg_ldd, "negative", test_number)
    return True

def test(x_range, y_range, ldd, cons, test_number):
    if not check_split(x_range, y_range, ldd, cons, test_number):
        print(f"test number {test_number} failed on constraint: {string_constraint(cons)}") 
        print()
    else:
        print(f"test number {test_number} passed")

def show_split_2d(x_range, y_range, ldd, cons):
    show_ldd_2d(ldd, x_range, y_range, f"ldd before constraint {string_constraint(cons)}")
    pos_ldd, neg_ldd = split(ldd, cons)
    show_ldd_2d(pos_ldd, x_range, y_range, f"positive ldd after constraint {string_constraint(cons)}")
    show_ldd_2d(neg_ldd, x_range, y_range, f"negative ldd after constraint {string_constraint(cons)}")

def test_code_generator(name, test_number, ldd_generator_function, var, op, param="", starting_code=""):
    spaces = "    "
    string = starting_code
    string = string + f"def test{name}():\n{spaces}global TEST_NUMBER\n\n"

    for i in range(1, 12):
        string = string + f"{spaces}TEST_NUMBER = {test_number}\n\n"
        string = string + f"{spaces}ldd = {ldd_generator_function}({param})\n"
        string = string + f'{spaces}cons = constraint("v{var} {op} {i}")\n'
        string = string + f"{spaces}test(x_range, y_range, ldd, cons, TEST_NUMBER)\n\n"
        test_number += 1

    return string, test_number

# this method create a new ldd with only one variable on two levels 
def one_var_depth_2_ldd(var=X):
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

def two_var_depth_2_then_child_ldd():
        return ldd_node(constraint(f"v0 >= 6"), 
                    ldd_node(constraint(f"v0 >= 9"),
                            ldd_node(constraint(f"v1 >= 9"),
                                    true_node(),
                                    false_node()),
                            ldd_node(constraint(f"v1 >= 6"),
                                    ldd_node(constraint(f"v1 >= 9"),
                                            false_node(),
                                            true_node()),
                                    false_node())), 
                    ldd_node(constraint(f"v1 >= 6"),
                        false_node(),
                        true_node()))

def two_var_depth_2_else_child_ldd():
    return ldd_node(constraint(f"v0 >= 6"), 
                    ldd_node(constraint(f"v1 >= 6"),
                            false_node(),
                            true_node()), 
                    ldd_node(constraint(f"v0 >= 3"),
                            ldd_node(constraint(f"v1 >= 6"),
                                    ldd_node(constraint(f"v1 >= 9"),
                                            false_node(),
                                            true_node()),
                                    false_node()),
                            ldd_node(constraint(f"v1 >= 9"),
                                    true_node(),
                                    false_node())))

def one_var_depth_2_then_child_ldd():
    return ldd_node(constraint("v0 >= 4"), 
                    ldd_node(constraint("v0 >= 8"), 
                             false_node(), 
                             true_node()),
                    false_node())

def one_var_depth_2_else_child_ldd():
    return ldd_node(constraint("v0 >= 8"), 
                    false_node(),
                    ldd_node(constraint("v0 >= 4"), 
                             true_node(), 
                             false_node()))

x_range = (0, 12)
y_range = (0, 12)

"""
# test cases where the variable of the constraint is not present in the ldd
# TEST_NUMBER [0..3]
def test0():
    global TEST_NUMBER

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
# TEST_NUMBER [4..23]
def test1():
    global TEST_NUMBER

    # constraint in std form and on X
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

    # constraint not in std form and on X
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
    cons = constraint(f"v0 <= 4")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 13

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v0 >= 2")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    # constraint in std form and on Y
    TEST_NUMBER = 14

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 10")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 15

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 7")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 16

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 6")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 17

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 5")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 18

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 2")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    # constraint not in std form and on Y
    TEST_NUMBER = 19

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 <= 10")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 20

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 <= 6")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 21

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 <= 5")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 22

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 <= 4")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

    TEST_NUMBER = 23

    ldd_2_var_depth_1 = two_var_depth_1_ldd()
    cons = constraint(f"v1 >= 2")
    test(x_range, y_range, ldd_2_var_depth_1, cons)

# test cases where the variable of the constraint is only on the then child
# these cases cover only the X variable
# TEST_NUMBER [24..39]
def test2():
    global TEST_NUMBER

    # constraint in std form and on X
    TEST_NUMBER = 24

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 11")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 25

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 26

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 9")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 27

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 8")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 28

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 29

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 6")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 30

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 31

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 >= 2")
    test(x_range, y_range, ldd, cons)

    # constraint not in std form and on X
    TEST_NUMBER = 32

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 33

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 9")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 34

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 8")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 35

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 36

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 6")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 37

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 38

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 39

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint(f"v0 <= 2")
    test(x_range, y_range, ldd, cons)

# test cases where the variable of the constraint is only on the else child
# these cases cover only the X variable
# TEST_NUMBER [40..55]
def test3():
    global TEST_NUMBER

    # constraint in std form and on X
    TEST_NUMBER = 40

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 11")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 41

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 42

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 6")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 43

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 44

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 45

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 46

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 2")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 47

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 >= 1")
    test(x_range, y_range, ldd, cons)

    # constraint not in std form and on X
    TEST_NUMBER = 48

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 49

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 50

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 6")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 51

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 52

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 53

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 54

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 55

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint(f"v0 <= 1")
    test(x_range, y_range, ldd, cons)

# test cases where we only have one var but on two levels
# these should test better for the cases where is possible to create nodes with both false children
# TEST_NUMBER [56..71]
def test4():
    global TEST_NUMBER

    # cases with only child
    TEST_NUMBER = 56

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 57

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 58

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 59

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 60

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 61

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 62

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 63

    ldd = one_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons)

    # cases with ony else child
    TEST_NUMBER = 64

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 65

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 66

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 67

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 68

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 69

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 70

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 71

    ldd = one_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons)

def test5():
    global TEST_NUMBER

    TEST_NUMBER = 72

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 73

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 74

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 75

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 76

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 77

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 78

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 79

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 80

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 81

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons)

    TEST_NUMBER = 82

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons)
"""

test_number = 0
test_code, test_number = test_code_generator(0, test_number, "one_var_depth_2_ldd", Y, GEQ, param="X")
test_code, test_number = test_code_generator(1, test_number, "one_var_depth_2_ldd", Y, LEQ, param="X", starting_code=test_code)
test_code, test_number = test_code_generator(2, test_number, "one_var_depth_2_ldd", X, GEQ, param="Y", starting_code=test_code)
test_code, test_number = test_code_generator(3, test_number, "one_var_depth_2_ldd", X, LEQ, param="Y", starting_code=test_code)

test_code, test_number = test_code_generator(4, test_number, "two_var_depth_1_ldd", X, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(5, test_number, "two_var_depth_1_ldd", X, LEQ, starting_code=test_code)
test_code, test_number = test_code_generator(6, test_number, "two_var_depth_1_ldd", Y, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(7, test_number, "two_var_depth_1_ldd", Y, LEQ, starting_code=test_code)

test_code, test_number = test_code_generator(8,  test_number, "two_var_depth_2_then_child_ldd", X, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(9,  test_number, "two_var_depth_2_then_child_ldd", X, LEQ, starting_code=test_code)
test_code, test_number = test_code_generator(10, test_number, "two_var_depth_2_then_child_ldd", Y, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(11, test_number, "two_var_depth_2_then_child_ldd", Y, LEQ, starting_code=test_code)

test_code, test_number = test_code_generator(12, test_number, "two_var_depth_2_else_child_ldd", X, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(13, test_number, "two_var_depth_2_else_child_ldd", X, LEQ, starting_code=test_code)
test_code, test_number = test_code_generator(14, test_number, "two_var_depth_2_else_child_ldd", Y, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(15, test_number, "two_var_depth_2_else_child_ldd", Y, LEQ, starting_code=test_code)

test_code, test_number = test_code_generator(16, test_number, "one_var_depth_2_ldd", X, GEQ, starting_code=test_code)
test_code, test_number = test_code_generator(17, test_number, "one_var_depth_2_ldd", X, LEQ, starting_code=test_code)

with open("tests.py", "w") as text_file:
    text_file.write("from ldd_test import *\n\n")
    text_file.write("TEST_NUMBER = 0\n\n")
    text_file.write(test_code)
    for i in range(0, 18):
        text_file.write(f"test{i}()\n")


"""
ldd = two_var_depth_2_then_child_ldd()
save_rendered_dot_ldd(ldd, name="_negative_weird_before")
cons = constraint("v1 >= 1")
pos, neg = split(ldd, cons)
print(dont_have_false_children(neg))
save_rendered_dot_ldd(neg, name="_negative_weird")

ldd = two_var_depth_2_then_child_ldd()
show_split_2d(x_range, y_range, ldd, cons)
"""