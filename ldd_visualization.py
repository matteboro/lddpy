from ldd import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import graphviz
import os

# Color for False and True
my_cmap = matplotlib.colors.ListedColormap(['indianred', 'lightblue'])

counter = 0

def dump_ldd_dot_recursive(node, count, string):
    global counter
    if (is_constant(node)):
        string.append(f'node{count} [label="{"0" if node.cons.cst == 0 else "1"}", shape=square];')
    else:
        my_idx = count
        string.append(f'node{count} [label="{string_constraint(node.cons)}", xlabel=<<FONT COLOR="red" POINT-SIZE="10">{node.id}</FONT>>];')
        counter += 1
        my_else_idx = counter
        dump_ldd_dot_recursive(node._else, counter, string)
        counter += 1
        my_then_idx = counter
        dump_ldd_dot_recursive(node._then, counter, string)
        string.append(f'node{my_idx} -> node{my_else_idx} [style="dashed"];')
        string.append(f'node{my_idx} -> node{my_then_idx};')

def dump_ldd_dot(node, do_print=True):
    string = ["digraph BDD {"]
    global counter
    counter += 1
    dump_ldd_dot_recursive(node, counter, string)
    string.append("}")
    if do_print:
        print('\n'.join(string))
    return '\n'.join(string)

def save_rendered_dot_ldd(ldd, format="pdf", name=""):
    dot_string = dump_ldd_dot(ldd, do_print=False)
    dot = graphviz.Source(dot_string)
    dot.render(f'dot_output/ldd{name}.gv', format=format).replace('\\', '/')
    if os.path.exists(f'dot_output/ldd{name}.gv'):
        os.remove(f'dot_output/ldd{name}.gv')

def dump_ldd(node):
    if (is_constant(node)):
        print("false", end="") if node.cons.cst == 0 else print("true", end="")
    else:
        print("ite(", end="")
        print_constraint(node.cons)
        print(", ", end="")
        dump_ldd(node._then)
        print(", ", end="")
        dump_ldd(node._else)
        print(")", end="")
            
def show_ldd_2d(ldd, x_range, y_range, title="ldd"):
    from_w, to_w = x_range
    from_h, to_h = y_range
    grid = satisfies_2d_grid(ldd, from_w, to_w, from_h, to_h)
    plt.imshow(grid, extent=[from_w, to_w, from_h, to_h], cmap=my_cmap)
    plt.title(title)
    ax = plt.gca()

    # Major ticks
    ax.set_xticks(np.arange(from_w, to_w, 1))
    ax.set_yticks(np.arange(from_h, to_h, 1))
    ax.set_xticklabels([" "]*(to_w - from_w))
    ax.set_yticklabels([" "]*(to_h - from_h))

    # Minor ticks
    ax.set_xticks(np.arange(from_w +.5, to_w, 1), minor=True)
    ax.set_yticks(np.arange(from_h +.5, to_h, 1), minor=True)
    ax.set_xticklabels(np.arange(from_w, to_w, 1), minor=True)
    ax.set_yticklabels(np.arange(from_h, to_h, 1), minor=True)

    # Gridlines based on major ticks
    ax.grid(which='major', color='white', linestyle='-', linewidth=1)

    # Remove minor ticks
    ax.tick_params(which='minor', bottom=False, left=False)

    plt.show()
