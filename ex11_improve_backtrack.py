###################################################################
# FILE : ex11_improve_backtracking.py
# WRITER : Aviad Dudkewitz
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION:  This program contains improve backtracking
# functions to solve graph coloring.
###################################################################
import ex11_map_coloring
from random import choice
from ex11_backtrack import general_backtracking
# from map_coloring_gui import color_map #uncomment if you installed the required libraries


def back_track_degree_heuristic(adj_dict, colors):
    """
    The function solves the graph coloring problem using by using the
    general_backtracking function but the order is based the countries with
    the most neighbors.
    :param adj_dict: dictionary of countries and their
    neighbors.
    :param colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    list_of_index = sorted(adj_dict, key=lambda x: len(adj_dict[x]))
    colored_map = {}
    for country in adj_dict:
        colored_map[country] = ""
    if general_backtracking(list_of_index[::-1], colored_map, 0,
                            colors, ex11_map_coloring.legal_color,
                            adj_dict):
        return colored_map


def num_of_possible_colors(colored_map, country, colors, dict_of_neighbors):
    """
    This function return the number of possible colors out of "colors"
    for uncolored country.
    :param colored_map: a dictionary representing countries
    and their colors.
    :param country: key in "colored_map".
    :param colors: list of string.
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: the number of possible colors.
    """
    return_num = 0
    neighbors = dict_of_neighbors[country]
    for color in colors:
        for neighbor in neighbors:
            if neighbor and colored_map[neighbor] == color:
                break
        return_num += 1
    return return_num


def back_track_MRV(adj_dict, colors):
    """
    The function solves the graph coloring problem using by using the minimum
    remaining values principle.
    :param adj_dict: dictionary of countries and their
    neighbors.
    :param colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    colored_map_dict = {}
    uncolored_countries = []
    for country in adj_dict:
        colored_map_dict[country] = ""
        uncolored_countries.append(country)
    if back_track_MRV_helper(uncolored_countries[0], colored_map_dict,
                             uncolored_countries, colors, adj_dict):
        return colored_map_dict


def back_track_MRV_helper(country, colored_map_dict, uncolored_countries_list,
                          colors, dict_of_neighbors):
    """
    This function aid "back_track_MRV" function.
    :param country: the current country in the recursion
    :param colored_map_dict: a dictionary representing countries
    and their colors.
    :param uncolored_countries_list: list of all the countries that still
    without a color.
    :param colors: list of strings.
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: True or False
    """
    for color in colors:
        # step in -
        colored_map_dict[country] = color
        if ex11_map_coloring.legal_color(colored_map_dict, country,
                                         dict_of_neighbors):
            uncolored_countries_list.remove(country)
            if len(uncolored_countries_list) == 0:
                # All countries are colored.
                return True
            else:
                next_country = min(uncolored_countries_list, key=lambda x:
                num_of_possible_colors(colored_map_dict, x, colors,
                                       dict_of_neighbors))
                if back_track_MRV_helper(next_country, colored_map_dict,
                        uncolored_countries_list, colors, dict_of_neighbors):
                    return True
            # backtrack
            uncolored_countries_list.append(country)
        else:
            # backtrack
            colored_map_dict[country] = ""
    else:
        return False


def all_neighbors_ok(neighbors, colored_map_dict, colors, dict_of_neighbors):
    """
    The function determines whether the last assignment has caused a country
    to left without any legal color.
    :param neighbors: list of countries
    :param colored_map_dict: a dictionary representing countries
    and their colors.
    :param colors: list of strings
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: True or False
    """
    for neighbor in neighbors:
        if neighbor and num_of_possible_colors(colored_map_dict, neighbor,
                                            colors, dict_of_neighbors) == 0:
            return False
    else:
        return True


def back_track_FC(adj_dict, colors):
    """
    The function solves the graph coloring problem using by using the Forward
    Checking principle.
    :param adj_dict: dictionary of countries and their
    neighbors.
    :param colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    colored_map_dict = {}
    list_of_countries = []
    for country in adj_dict:
        colored_map_dict[country] = ""
        list_of_countries.append(country)
    if back_track_FC_helper(list_of_countries, colored_map_dict,
                             0, colors, adj_dict):
        return colored_map_dict


def back_track_FC_helper(list_of_countries, colored_map_dict, index, colors,
                         dict_of_neighbors):
    """
    This function aid "back_track_FC" function.
    :param list_of_countries: lists of all keys in colored_map_dict.
    :param colored_map_dict: a dictionary representing countries
    and their colors.
    :param index: the index of current country in "list_of_countries" to check.
    :param colors: list of strings
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: True or False
    """
    if index == len(list_of_countries):
        # the function successfully set colors to all countries.
        return True
    for color in colors:
        # step in -
        colored_map_dict[list_of_countries[index]] = color
        neighbors = dict_of_neighbors[list_of_countries[index]]
        if ex11_map_coloring.legal_color(colored_map_dict,
                            list_of_countries[index], dict_of_neighbors) and\
            all_neighbors_ok(neighbors, colored_map_dict, colors,
                             dict_of_neighbors) and \
            back_track_FC_helper(list_of_countries, colored_map_dict,
                                     index + 1, colors, dict_of_neighbors):
            return True
        # back track -
        colored_map_dict[list_of_countries[index]] = ""
    else:
        return False


def all_possible_colors(colored_map, country, dict_of_neighbors,
                        colors):
    """
    This function return all the possible colors that legal to assign to
    "country". Note: the "country" should not be colored!
    :param colored_map: a dictionary representing countries
    and their colors.
    :param country: key in colored_map
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :param colors: list of strings.
    :return: a list of possible colors.
    """
    return_list =[]
    for color in colors:
        colored_map[country] = color
        if ex11_map_coloring.legal_color(colored_map, country,
                                         dict_of_neighbors):
            return_list.append(color)
    colored_map[country] = ""
    return return_list


def colors_list_based_on_neighbors(colored_map, country, dict_of_neighbors,
                                  colors, possible_colors):
    """
    This function return the color out of "possible_colors" that allow the
    most options for neighboring countries to country.  Note: the "country"
    should not be colored!
    :param colored_map: a dictionary representing countries
    and their colors.
    :param country: key in colored_map
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :param possible_colors: the possible colors to assign to country.
    :param colors: list of the original colors.
    :return: list of colors out of "possible_colors"
    """
    dict_of_colors = {}
    neighbors = dict_of_neighbors[country]
    if neighbors[0] == "":
        return choice(possible_colors)
    for color in possible_colors:
        colored_map[country] = color
        counter = 0
        for neighbor in neighbors:
            counter += num_of_possible_colors(colored_map, neighbor, colors,
                                              dict_of_neighbors)
        dict_of_colors[color] = counter
    colored_map[country] = ""
    return sorted(dict_of_colors.keys(), key=lambda x: dict_of_colors[x])[::-1]


def back_track_LCV(adj_dict, colors):
    """
    The function solves the graph coloring problem using by using the Least
    Constraining Value principle.
    :param adj_dict: a dictionary of countries and their
    neighbors.
    :param colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    colored_map_dict = {}
    list_of_countries = []
    for country in adj_dict:
        colored_map_dict[country] = ""
        list_of_countries.append(country)
    if back_track_LCV_helper(list_of_countries, colored_map_dict,
                            0, colors, adj_dict):
        return colored_map_dict

def back_track_LCV_helper(list_of_countries, colored_map_dict, index, colors,
                          dict_of_neighbors):
    """
    This function aid "back_track_LCV" function.
    :param list_of_countries: list of keys in "colored_map_dict".
    :param colored_map_dict: a dictionary representing countries
    and their colors.
    :param index: the index of current country in "list_of_countries" to check.
    :param colors: list of strings
    :param dict_of_neighbors: dictionary of countries and their
    neighbors.
    :return: True or False
    """
    if index == len(list_of_countries):
        # the function successfully set colors to all countries.
        return True
    country = list_of_countries[index]
    possible_colors = all_possible_colors(colored_map_dict, country,
                                          dict_of_neighbors, colors)
    if not possible_colors:
        return False
    else:
        possible_colors = colors_list_based_on_neighbors(colored_map_dict,
                         country, dict_of_neighbors, colors, possible_colors)
        if type(possible_colors) == str: # to prevent a situation that the
            # function "colors_list_based_on_neighbors" return a sting and
            # not a list.
            # step in-
            colored_map_dict[country] = possible_colors
            if back_track_LCV_helper(list_of_countries, colored_map_dict,
                                     index + 1, colors, dict_of_neighbors):
                return True
            else:
                # backtrack
                colored_map_dict[country] = ""
                return False
        else:
            for color in possible_colors:
                # step in -
                colored_map_dict[country] = color
                if back_track_LCV_helper(list_of_countries, colored_map_dict,
                                    index + 1, colors, dict_of_neighbors):
                    return True
            else:
                # backtrack
                colored_map_dict[country] = ""
                return False


def fast_back_track(adj_dict, colors):
    """
    The function solves the graph coloring problem by using the Minimum
    Remaining Values principle but the order is based on the countries with
    the most neighbors.
    :param adj_dict: a dictionary of countries and their
    neighbors.
    :param colors: the amount of colors to check
    :return: if there is a solution - a dictionary representing countries
    and their colors.
    """
    uncolored_countries = sorted(adj_dict, key=lambda x:
                                    len(adj_dict[x]))[::-1]
    colored_map_dict = {}
    for country in adj_dict:
        colored_map_dict[country] = ""
    if back_track_MRV_helper(uncolored_countries[0], colored_map_dict,
                             uncolored_countries, colors, adj_dict):
        return colored_map_dict

if __name__ == "__main__":
    my_map = ex11_map_coloring.read_adj_file("adjacency_files/adj_world_ex11.txt")
    print(fast_back_track(my_map,ex11_map_coloring.COLORS[:4]))
