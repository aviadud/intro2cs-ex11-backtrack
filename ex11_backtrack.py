################################################################
# FILE : ex11_backtrack.py
# WRITER : Aviad Dudkewitz
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION:  This program contains a function works
# in recursive way and implements the principle of backtracking.
# it is implemented in ex11_sudoku.py, ex11_map_coloring.py
# and ex11_improve_backtracking.py .
################################################################

def general_backtracking(list_of_items, dict_items_to_vals, index, 
                    set_of_assignments, legal_assignment_func,
                    *args):
    """
    This function works in recursive way and implements
    the principle of backtracking. It checks whether all the variables given
    in "set_of_assignments" can be placed in "dict_items_to_vals" in a legal
    way based on "legal_assignment_func".
    :param list_of_items: list of keys from "dict_items_to_vals"
    :param dict_items_to_vals: dictionary
    :param index: index for item in "list_of_items"
    :param set_of_assignments: List of the values to placed in
    "dict_items_to_vals".
    :param legal_assignment_func: a function that determines whether a post is
     valid.
    :param args: a list of additional optional variables for
    "legal_assignment_func".
    :return: True or False
    """
    if index == len(list_of_items):
        # the function successfully set values to all keys in
        # "dict_items_to_vals"
        return True
    for assignment in set_of_assignments:
        org_value = dict_items_to_vals[list_of_items[index]]
        dict_items_to_vals[list_of_items[index]] = assignment
        # step in:
        if legal_assignment_func(dict_items_to_vals, list_of_items[index],
                                 *args) and \
            general_backtracking(list_of_items, dict_items_to_vals, index + 1,
                        set_of_assignments, legal_assignment_func, *args):
                return True
        else:
            # Backtrack
            dict_items_to_vals[list_of_items[index]] = org_value
    else:
        return False
