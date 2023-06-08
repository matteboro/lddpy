from ldd import *

ELSE = 0
IF_ELSE = 1
THEN = 2
NOTHING = 3
IF = 4
IF_THEN = 5

def children_have_different_variables(cons_else, cons_if, cons_then):
    return (is_constant(cons_else) or var(cons_else) != var(cons_if)) and (is_constant(cons_then) or var(cons_then) != var(cons_if))

def only_then_child_has_same_variable(cons_else, cons_if, cons_then):
    return (is_constant(cons_else) or var(cons_else) != var(cons_if)) and (var(cons_then) == var(cons_if))

def only_else_child_has_same_variable(cons_else, cons_if, cons_then):
    return (var(cons_else) == var(cons_if)) and (is_constant(cons_then) or var(cons_then) != var(cons_if))

def children_have_same_variable(cons_else, cons_if, cons_then):
    return (var(cons_else) == var(cons_if)) and (var(cons_then) == var(cons_if))

def choose_side_std_form(cons, cons_else, cons_if, cons_then):

    if children_have_different_variables(cons_else, cons_if, cons_then):
        if cons_if.cst == cons.cst:
            return IF
        elif cons_if.cst > cons.cst:
            return IF_ELSE
        else: # cons.cst > cons_if.cst
            return IF_THEN
    elif only_else_child_has_same_variable(cons_else, cons_if, cons_then):
        if cons.cst < cons_if.cst:
            return ELSE
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst > cons_if.cst
            return IF_THEN
    elif only_then_child_has_same_variable(cons_else, cons_if, cons_then):
        if cons.cst < cons_if.cst:
            return IF_ELSE
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst > cons_if.cst
            return THEN 
    elif children_have_same_variable(cons_else, cons_if, cons_then): 
        if cons.cst <  cons_if.cst:
            return ELSE
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst > cons_if.cst
            return THEN
        
    print("UNREACHABLE: choose_side_std_form")
    exit(1)

def choose_side_non_std_form(cons, cons_else, cons_if, cons_then):

    cons = complement_if_not_std_form(cons)
    if children_have_different_variables(cons_else, cons_if, cons_then):
        if cons_if.cst == cons.cst:
            return IF
        elif cons_if.cst > cons.cst:
            return IF_ELSE
        else: # cons.cst > cons_if.cst
            return IF_THEN
    elif only_else_child_has_same_variable(cons_else, cons_if, cons_then):
        if cons.cst > cons_if.cst:
            return IF_THEN
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst < cons_if.cst
            return ELSE
    elif only_then_child_has_same_variable(cons_else, cons_if, cons_then):
        if cons.cst > cons_if.cst:
            return THEN
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst > cons_if.cst
            return IF_ELSE 
    elif children_have_same_variable(cons_else, cons_if, cons_then): 
        if cons.cst > cons_if.cst:
            return THEN
        elif cons.cst == cons_if.cst:
            return IF
        else: # cons.cst > cons_if.cst
            return ELSE
        
    print("UNREACHABLE: choose_side_non_std_form")
    exit(1)

def place_constraint(node, cons):
    # assert(v(node) == v(cons))

    if (is_std_form(cons)):
        side = choose_side_std_form(cons, else_child(node).cons, node.cons, then_child(node).cons)
        if side == ELSE:
            new_else = place_constraint(else_child(node), cons)
            return set_else_child(node, new_else)
        elif side == IF_ELSE:
            new_else = ldd_node(cons, else_child(node), false_node()) if not is_false(else_child(node)) else false_node()
            set_else_child(node, new_else)
            return node
        elif side == IF:
            set_else_child(node, false_node())
            return node if not is_false(then_child(node)) else false_node()
        elif side == IF_THEN:
            node.cons = cons
            set_else_child(node, false_node())
            return node if not is_false(then_child(node)) else false_node()
        elif side == THEN:
            return place_constraint(then_child(node), cons)
           
    else: 
        compl_cons = complement_if_not_std_form(cons)
        side = choose_side_non_std_form(cons, else_child(node).cons, node.cons, then_child(node).cons)
        if side == ELSE:
            return place_constraint(else_child(node), cons)
        if side == IF_ELSE:
            node.cons = compl_cons
            set_then_child(node, false_node())
            return node if not is_false(else_child(node)) else false_node()
        if side == IF:
            set_then_child(node, false_node())
            return node if not is_false(else_child(node)) else false_node()
        if side == IF_THEN:
            new_then = ldd_node(compl_cons, false_node(), then_child(node)) if not is_false(then_child(node)) else false_node()
            return set_then_child(node, new_then)
        if side == THEN:
            new_then = place_constraint(then_child(node), cons)
            return set_then_child(node, new_then)

def insert_constraint(node, cons):
    if is_false(node):
        return node
    return ldd_node(complement_if_not_std_form(cons), 
                    node         if is_std_form(cons) else false_node(), 
                    false_node() if is_std_form(cons) else node)

def assume(node, cons):
    if is_false(node):
        return node
    elif is_true(node):
        compl_cons = complement_if_not_std_form(cons)
        return ldd_node(compl_cons, 
                        true_node() if is_std_form(cons) else false_node(), 
                        false_node() if is_std_form(cons) else true_node())

    if (var(node) == var(cons)):
        return place_constraint(node, cons)
    
    if (var(node) > var(cons)):
        return insert_constraint(node, cons)

    if (var(then_child(node)) > var(cons)):
        new_then = insert_constraint(then_child(node), cons)
    else: # (var(then_child(node)) <= var(cons)) 
        new_then = assume(then_child(node), cons)

    if (var(else_child(node)) > var(cons)):
        new_else = insert_constraint(else_child(node), cons)
    else: # (var(else_child(node)) <= var(cons)) 
        new_else = assume(else_child(node), cons)

    return set_children(node, new_then, new_else)
