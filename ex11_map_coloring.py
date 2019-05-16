################################################################
# FILE : ex11_map_coloring.py
# WRITER : Aviad Dudkewitz
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION:  This program set colors for a given list of
# countries on a map so that no neighboring countries will have
# the same color.
################################################################
from ex11_backtrack import general_backtracking

#from map_coloring_gui import color_map #uncomment if you installed the required libraries

COLORS = ['red','blue','green','magenta','yellow','cyan']

def read_adj_file(adjacency_file):
    """
    This function load a file to a dictionary of countries and their
    neighbors.
    :param adjacency_file: path
    :return: dictionary
    """
    return_dict = {}
    with open(adjacency_file, "r") as load_map:
        for line in load_map:
            country, neighbors = line[:-1].split(":")
            return_dict[country] = neighbors.split(",")
    return return_dict


def legal_color(colored_map, country, dict_of_neighbors):
    """
    This function determines if the color that has been placed to "country"
    is legally.
    :param colored_map: a dictionary representing a painted map.
    :param country: a key in "colored_map"
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: True or False
    """
    neighbors = dict_of_neighbors[country]
    color = colored_map[country]
    for neighbor in neighbors:
        if neighbor and colored_map[neighbor] == color:
            return False
    else:
        return True


def run_map_coloring(adjacency_file, num_colors = 4, map_type = None):
    """
    This set colors for a given list of countries on a map so that no
    neighboring countries will have the same color. if there is no such option,
     the function will return None
    :param adjacency_file: path
    :param num_colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    dict_of_neighbor = read_adj_file(adjacency_file)
    colored_map = {}
    for country in dict_of_neighbor.keys():
        colored_map[country] = ""
    if general_backtracking(list(colored_map.keys()), colored_map, 0,
                    COLORS[:num_colors], legal_color, dict_of_neighbor):
        return colored_map

