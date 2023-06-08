from ldd_split import *
from ldd_visualization import *


root = ldd_node(constraint("v0 >= 0"), 
                    ldd_node(constraint("v1 >= 4"),
                        false_node(),
                        true_node()), 
                    ldd_node(constraint("v1 >= 6"),
                        true_node(),
                        false_node()))

show_ldd_2d(root, -5, 5, 0, 10)
dump_ldd_dot(root)
print(list_of_indexes(root))

root = assume(root, constraint("v1 >= 1"))
show_ldd_2d(root, -5, 5, 0, 10)
dump_ldd_dot(root)