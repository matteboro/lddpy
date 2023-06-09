from ldd_assume import *

RIGHT = 0
IF_RIGHT = 1
IF_LEFT = 2
LEFT = 3
ONLY_THEN_RIGHT = 4
ONLY_THEN_SPEC = 5
ONLY_THEN_SPEC_SOVRAPP = 6
ONLY_ELSE_LEFT = 7

DEBUG = False

def print_debug(string):
    if DEBUG:
        print(string)

def split_choose_side(cons, cons_else, cons_if, cons_then):
    
    if children_have_different_variables(cons_else, cons_if, cons_then):
        print_debug("case children have different variables")
        if cons.cst - 1 > cons_if.cst:
            return RIGHT
        elif cons.cst - 1 == cons_if.cst:
            return RIGHT
        elif cons.cst == cons_if.cst:
            return IF_LEFT
        elif cons.cst < cons_if.cst:
            return LEFT
        else:
            print("unreachable: split_choose_side.children_have_different_variables")
            exit(1)

    elif only_then_child_has_same_variable(cons_else, cons_if, cons_then):
        print_debug("case only then child have same variables")
        if cons.cst - 1 > cons_if.cst:
            return ONLY_THEN_RIGHT
        elif cons.cst - 1 == cons_if.cst:
            if cons.cst < cons_then.cst:
                return ONLY_THEN_SPEC
            elif cons.cst == cons_then.cst:
                return ONLY_THEN_SPEC_SOVRAPP
            else:
                print("unreachable: split_choose_side.only_then_child_has_same_variable(cons.cst - 1 == cons_if.cst)")
                exit(1)
        elif cons.cst == cons_if.cst:
            return IF_LEFT
        elif cons.cst < cons_if.cst:
            return LEFT
        else:
            print("unreachable: split_choose_side.only_then_child_has_same_variable")
            exit(1)

    elif only_else_child_has_same_variable(cons_else, cons_if, cons_then):
        print_debug("case else then child have same variables")
        if cons.cst < cons_if.cst:
            return ONLY_ELSE_LEFT
        elif cons.cst == cons_if.cst:
            return IF_LEFT
        elif cons.cst > cons_if.cst:
            return RIGHT
        else:
            print("unreachable: split_choose_side.only_else_child_has_same_variable")
            exit(1)

    elif children_have_same_variable(cons_else, cons_if, cons_then):
        print_debug("case both children have same variable")
        if cons.cst < cons_if.cst:
            return ONLY_ELSE_LEFT
        elif cons.cst == cons_if.cst:
            return IF_LEFT
        elif cons.cst > cons_if.cst:
            return ONLY_THEN_RIGHT
        else:
            print("unreachable: split_choose_side.children_have_same_variable")
            exit(1)

    print("unreachable: split_choose_side")
    exit(1)

def split_place_constraint(ldd, cons):

    side = split_choose_side(cons, else_child(ldd).cons, ldd.cons, then_child(ldd).cons)

    if side == RIGHT:
        print_debug("caso RIGHT")
        new_ldd_pos = ldd_node(cons)
        new_ldd_neg = ldd_node(ldd.cons)
        new_ldd_neg_then = ldd_node(cons)
        set_children(new_ldd_neg_then, false_node(), copy_ldd(then_child(ldd)))
        return (set_children(new_ldd_pos, then_child(ldd), false_node()), 
                set_children(new_ldd_neg, new_ldd_neg_then, else_child(ldd)))
    elif side == IF_RIGHT:
        print_debug("caso IF_RIGHT")
        # new_ldd_pos = ldd_node(cons)
        # new_ldd_neg = ldd_node(cons)
        # return (set_children(new_ldd_pos, then_child(ldd), false_node()), 
        #         set_children(new_ldd_neg, false_node(), else_child(ldd)))
    elif side == IF_LEFT:
        print_debug("caso IF_LEFT")
        new_ldd_pos = ldd_node(ldd.cons)
        new_ldd_neg = ldd_node(ldd.cons)
        return (set_children(new_ldd_pos, then_child(ldd), false_node()), 
                set_children(new_ldd_neg, false_node(), else_child(ldd)))
    elif side == LEFT:
        print_debug("caso LEFT")
        new_ldd_pos = ldd_node(ldd.cons)
        new_ldd_neg = ldd_node(cons)
        new_ldd_pos_else = ldd_node(cons)
        set_children(new_ldd_pos_else, copy_ldd(else_child(ldd)), false_node())
        return (set_children(new_ldd_pos, then_child(ldd), new_ldd_pos_else), 
                set_children(new_ldd_neg, false_node(), else_child(ldd)))
    elif side == ONLY_THEN_RIGHT:
        print_debug("caso ONLY_THEN_RIGHT")
        new_ldd_pos, new_ldd_neg_then = split_place_constraint(then_child(ldd), cons)
        new_ldd_neg = ldd_node(ldd.cons)
        return (new_ldd_pos, 
                set_children(new_ldd_neg, new_ldd_neg_then, else_child(ldd)))
    elif side == ONLY_THEN_SPEC:
        print_debug("caso ONLY_THEN_SPEC")
        new_ldd_pos = ldd_node(cons)
        new_ldd_neg = ldd_node(ldd.cons)
        new_ldd_neg_then = ldd_node(cons)
        set_children(new_ldd_neg_then, false_node(), copy_ldd(else_child(then_child(ldd))))
        return (set_children(new_ldd_pos, then_child(ldd), false_node()), 
                set_children(new_ldd_neg, new_ldd_neg_then, else_child(ldd)))
    elif side == ONLY_THEN_SPEC_SOVRAPP:
        print_debug("caso ONLY_THEN_SPEC_SOVRAPP")
        new_ldd_pos = then_child(then_child(ldd))
        new_ldd_neg = ldd_node(ldd.cons)
        new_ldd_neg_then = ldd_node(cons, false_node(), else_child(then_child(ldd)))
        return (new_ldd_pos, 
                set_children(new_ldd_neg, new_ldd_neg_then, else_child(ldd)))
    elif side == ONLY_ELSE_LEFT:
        print_debug("caso ONLY_ELSE_LEFT")
        new_ldd_pos_else, new_ldd_neg = split_place_constraint(else_child(ldd), cons)
        new_ldd_pos = ldd_node(ldd.cons)
        return (set_children(new_ldd_pos, then_child(ldd), new_ldd_pos_else),
               new_ldd_neg)
    else:
        print("unreachable: split_place_constraint")
        exit(1)

    print("unreachable: split_place_constraint")
    exit(1)

def split_insert_constraint(ldd, cons):
    if is_false(ldd):
        return (false_node(), false_node())
    pos = ldd_node(cons, ldd, false_node())
    neg = ldd_node(cons, false_node(), copy_ldd(ldd))
    return (pos, neg)

def split_recur(ldd, cons):

    if (var(ldd) == var(cons)):
        return split_place_constraint(ldd, cons)
    
    if (var(ldd) > var(cons)):
        return split_insert_constraint(ldd, cons)

    new_ldd = ldd_node(ldd.cons)

    if (var(then_child(ldd)) > var(cons)):
        new_pos_then, new_neg_then = split_insert_constraint(then_child(ldd), cons)
    else: # (var(then_child(node)) <= var(cons)) 
        new_pos_then, new_neg_then = split_recur(then_child(ldd), cons)

    if (var(else_child(ldd)) > var(cons)):
        new_pos_else, new_neg_else = split_insert_constraint(else_child(ldd), cons)
    else: # (var(else_child(node)) <= var(cons)) 
        new_pos_else, new_neg_else = split_recur(else_child(ldd), cons)

    return (set_children(ldd, new_pos_then, new_pos_else), set_children(new_ldd, new_neg_then, new_neg_else))

def split(ldd, cons):

    # handle of top and bottom cases
    compl = not is_std_form(cons)
    std_cons = complement_if_not_std_form(cons)
    if is_constant(ldd):
        if is_true(ldd):
            pos = ldd_node(std_cons, true_node() , false_node())
            neg = ldd_node(std_cons, false_node(), true_node())
        elif is_false(ldd):
            pos = false_node() 
            neg = false_node()
    else: 
        pos, neg = split_recur(ldd, std_cons)

    if compl:
        return (neg, pos)
    else:
        return (pos, neg)
