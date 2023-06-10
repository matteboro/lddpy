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
        print("ERROR in check_split: constraint is not of variable 0 or 1")
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

def test_code_generator(name, test_number, ldd_generator_function, var, op, param="", starting_code="", rng = (1, 12)):
    spaces = "    "
    string = starting_code
    string = string + f"def test{name}():\n{spaces}global TEST_NUMBER\n\n"

    for i in range(rng[0], rng[1]):
        string = string + f"{spaces}TEST_NUMBER = {test_number}\n\n"
        string = string + f"{spaces}ldd = {ldd_generator_function}({param})\n"
        string = string + f'{spaces}cons = constraint("v{var} {op} {i}")\n'
        string = string + f"{spaces}test(x_range, y_range, ldd, cons, TEST_NUMBER)\n\n"
        test_number += 1

    string = string + f"test{name}()\n\n"
    return string, test_number

def from_list_to_ldd_like_list(l):
    if len(l) % 2 == 0:
        print("ERROR list passed to from_list_to_ldd(l) cannot have a even number of element")
        exit(1)
    if len(l) == 1:
        return [l[0], True, False]
    return [l[int(len(l)/2)], from_list_to_ldd_like_list(l[:int(len(l)/2)]), from_list_to_ldd_like_list(l[int(len(l)/2)+1:])]

def from_ldd_like_list_to_ldd(l):
    if l is True:
        return true_node()
    elif l is False:
        return false_node()
    cons = constraint(f"v0 >= {l[0]}")
    ldd_else = from_ldd_like_list_to_ldd(l[1])
    ldd_then = from_ldd_like_list_to_ldd(l[2])
    return ldd_node(cons, ldd_then, ldd_else)

def complete_binary_tree_number_of_nodes(levels):
    if levels == 1:
        return 1
    return complete_binary_tree_number_of_nodes(levels-1) + (2**(levels-1))

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

def two_var_depth_2_ldd():
    else_else_child = ldd_node(constraint("v1 >= 3"), 
                               false_node(), 
                               ldd_node(constraint("v1 >= 1"), 
                                        true_node(), 
                                        false_node()))
    else_then_child = ldd_node(constraint("v1 >= 6"), 
                               false_node(), 
                               ldd_node(constraint("v1 >= 3"), 
                                        true_node(), 
                                        false_node()))
    then_else_child = ldd_node(constraint("v1 >= 9"), 
                               false_node(), 
                               ldd_node(constraint("v1 >= 6"), 
                                        true_node(), 
                                        false_node()))
    
    then_then_child = ldd_node(constraint("v1 >= 9"),  
                               ldd_node(constraint("v1 >= 11"), 
                                        false_node(), 
                                        true_node()), 
                                false_node())
    
    return ldd_node(constraint(f"v0 >= 6"), 
                ldd_node(constraint(f"v0 >= 9"),
                    then_then_child,
                    then_else_child),
                ldd_node(constraint(f"v0 >= 3"),
                    else_then_child,
                    else_else_child))

def one_var_arbitrary_depth_complete_ldd(levels):
    l = [3*(i+1) for i in range(complete_binary_tree_number_of_nodes(levels))]
    l = from_list_to_ldd_like_list(l)
    return from_ldd_like_list_to_ldd(l)

x_range = (0, 12)
y_range = (0, 12)

if __name__ == "__main__":
    test_number = 0
    test_code = "from ldd_test import *\n\n" + "TEST_NUMBER = 0\n\n" + "x_range = (0, 12)\n" + "y_range = (0, 12)\n\n"
    test_code, test_number = test_code_generator(0, test_number, "one_var_depth_2_ldd", Y, GEQ, param="X", starting_code=test_code)
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

    test_code, test_number = test_code_generator(18, test_number, "one_var_depth_2_then_child_ldd", X, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(19, test_number, "one_var_depth_2_then_child_ldd", X, LEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(20, test_number, "one_var_depth_2_then_child_ldd", Y, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(21, test_number, "one_var_depth_2_then_child_ldd", Y, LEQ, starting_code=test_code)

    test_code, test_number = test_code_generator(22, test_number, "one_var_depth_2_else_child_ldd", X, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(23, test_number, "one_var_depth_2_else_child_ldd", X, LEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(24, test_number, "one_var_depth_2_else_child_ldd", Y, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(25, test_number, "one_var_depth_2_else_child_ldd", Y, LEQ, starting_code=test_code)

    test_code, test_number = test_code_generator(26, test_number, "two_var_depth_2_ldd", X, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(27, test_number, "two_var_depth_2_ldd", X, LEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(28, test_number, "two_var_depth_2_ldd", Y, GEQ, starting_code=test_code)
    test_code, test_number = test_code_generator(29, test_number, "two_var_depth_2_ldd", Y, LEQ, starting_code=test_code)

    test_code = test_code + "x_range = (0, 24)\n" + "y_range = (0, 6)\n\n"
    test_code, test_number = test_code_generator(30, test_number, "one_var_arbitrary_depth_complete_ldd", X, GEQ, param=3, starting_code=test_code, rng=(1, 24))
    test_code, test_number = test_code_generator(31, test_number, "one_var_arbitrary_depth_complete_ldd", X, LEQ, param=3, starting_code=test_code, rng=(1, 24))

    with open("tests.py", "w") as text_file:
        text_file.write(test_code)

    save_rendered_dot_ldd(one_var_depth_2_ldd(X), name="_one_var_depth_2_ldd")
    save_rendered_dot_ldd(two_var_depth_1_ldd(), name="_two_var_depth_1_ldd")
    save_rendered_dot_ldd(two_var_depth_2_then_child_ldd(), name="_two_var_depth_2_then_child_ldd")
    save_rendered_dot_ldd(two_var_depth_2_else_child_ldd(), name="_two_var_depth_2_else_child_ldd")
    save_rendered_dot_ldd(one_var_depth_2_then_child_ldd(), name="_one_var_depth_2_then_child_ldd")
    save_rendered_dot_ldd(one_var_depth_2_else_child_ldd(), name="_one_var_depth_2_else_child_ldd")
    save_rendered_dot_ldd(two_var_depth_2_ldd(), name="_two_var_depth_2_ldd")
    save_rendered_dot_ldd(one_var_arbitrary_depth_complete_ldd(3), name="one_var_arbitrary_depth_complete_ldd(3)")
    save_rendered_dot_ldd(one_var_arbitrary_depth_complete_ldd(4), name="one_var_arbitrary_depth_complete_ldd(4)")
    save_rendered_dot_ldd(one_var_arbitrary_depth_complete_ldd(5), name="one_var_arbitrary_depth_complete_ldd(5)")


