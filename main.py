import numpy as np
from itertools import product
import copy


def find_solution_with_data_only(query, condition, data):  # finding solution with data
    query_count = 0
    condition_count = 0
    for i in range(len(data[0])):  # iterate for every column
        q_match_count = 0
        match_count = 0
        for variable in condition:
            if len(variable) == 1:
                if data[ord(variable) - 65][i]:  # using ascii a becomes 0th index
                    match_count += 1
            else:
                if data[ord(variable[1]) - 65][i] == False:
                    match_count += 1

        if match_count == len(condition):  # if all the variables in condition matches
            condition_count += 1  # we need to increase number of total correct condition
            for q_variable in query:
                if len(q_variable) == 1:
                    if data[ord(q_variable) - 65][i]:
                        q_match_count += 1
                else:
                    if data[ord(q_variable[1]) - 65][i] == False:
                        q_match_count += 1

            if q_match_count == len(query):  # if all the variables in the querry matches
                query_count += 1  # we also increase the query

    return (query_count / condition_count)


def mainEquation(a, b, c, d, e, f, g):
    equation_dict = {  # a dictionary holds all possible equations and their probabilities
        "A": p_a,
        "B": p_b,
        "nA": 1 - p_a,
        "nB": 1 - p_b,
        "CA": c_a,
        "nCA": not_c_a,
        "CnA": c_not_a,
        "nCnA": not_c_not_a,
        "GD": g_d,
        "nGD": not_g_d,
        "GnD": g_not_d,
        "nGnD": not_g_not_d,
        "FC": f_c,
        "nFC": not_f_c,
        "FnC": f_not_c,
        "nFnC": not_f_not_c,
        "EC": e_c,
        "nEC": not_e_c,
        "EnC": e_not_c,
        "nEnC": not_e_not_c,
        "DAB": d_a_b,
        "nDAB": not_d_a_b,
        "DnAB": d_not_a_b,
        "DAnB": d_a_not_b,
        "DnAnB": d_not_a_not_b,
        "nDnAB": not_d_not_a_b,
        "nDAnB": not_d_a_not_b,
        "nDnAnB": not_d_not_a_not_b
    }
    # takes the probability of variable from dictionary and multiply them to find result
    result = equation_dict[a] * equation_dict[b] * equation_dict[c + a] * equation_dict[e + c] * equation_dict[g + d] * \
             equation_dict[d + a + b] * equation_dict[f + c]

    return result


def sortVariableList(given_list, missing_list):  # it takes the input list and the rest of the elements in network
    for item in given_list:
        missing_list.append(item)

    swapped = True
    while swapped:  # we mix the lists and then sort it in alphabetic order.
        swapped = False
        for i in range(len(missing_list) - 1):  # for every variable we should know if it is negative or positive
            if len(missing_list[i]) == 1 and len(missing_list[i + 1]) == 1:
                if missing_list[i] > missing_list[i + 1]:
                    missing_list[i], missing_list[i + 1] = missing_list[i + 1], missing_list[i]
                    swapped = True
            if len(missing_list[i]) == 2 and len(missing_list[i + 1]) == 1:
                if missing_list[i][1] > missing_list[i + 1]:
                    missing_list[i], missing_list[i + 1] = missing_list[i + 1], missing_list[i]
                    swapped = True
            if len(missing_list[i]) == 1 and len(missing_list[i + 1]) == 2:
                if missing_list[i] > missing_list[i + 1][1]:
                    missing_list[i], missing_list[i + 1] = missing_list[i + 1], missing_list[i]
                    swapped = True
            if len(missing_list[i]) == 2 and len(missing_list[i + 1]) == 2:
                if missing_list[i][1] > missing_list[i + 1][1]:
                    missing_list[i], missing_list[i + 1] = missing_list[i + 1], missing_list[i]
                    swapped = True
    return missing_list


def findProbabilityWithBayesian(variables):
    variable_dict = {  # all nodes and their probabilities
        "A": p_a,
        "B": p_b,
        "C": p_c,
        "D": p_d,
        "E": p_e,
        "F": p_f,
        "G": p_g,
        "nA": 1 - p_a,
        "nB": 1 - p_b,
        "nC": 1 - p_c,
        "nD": 1 - p_d,
        "nE": 1 - p_e,
        "nF": 1 - p_f,
        "nG": 1 - p_g,
    }

    combination_list = []
    for item in variables:
        if len(item) == 1:  # if positive variable
            if item in variable_dict.keys():
                del variable_dict[
                    item]  # we delete the input variables from list so at the end, there will be a list of variables not in the input
                del variable_dict["n" + item]  # we also should delete the negative of variable.
        else:
            if item in variable_dict.keys():
                del variable_dict[item]  # if negative variable
                del variable_dict[item[1]]  # delete the positive of it as well

    for missing_variables in list(variable_dict.keys()):
        if len(missing_variables) == 1:  # for all missing variables, we store them in list of 2 as pair
            small_list = [missing_variables, "n" + missing_variables]
            combination_list.append(small_list)

    result = 0

    for elements in list(product(
            *combination_list)):  # in order to calculate all combination of missing variable, and then combine it with in put variables we need cartesian product
        sorted_variable_list = sortVariableList(list(elements), copy.deepcopy(
            variables))  # sort the all variables we have in the alphabetic order, to use it in calculatin.
        result += mainEquation(sorted_variable_list[0], sorted_variable_list[1], sorted_variable_list[2],
                               sorted_variable_list[3], sorted_variable_list[4], sorted_variable_list[5],
                               sorted_variable_list[6])

    return result


if __name__ == '__main__':
    arr = np.load('data 1.npy')
    number_of_data = len(arr[0])

    # all the possible variable combinations should be calculated
    p_a = 0
    p_b = 0
    p_c = 0
    p_d = 0
    p_e = 0
    p_f = 0
    p_g = 0

    g_and_d = 0
    g_and_not_d = 0

    f_and_c = 0
    f_and_not_c = 0

    e_and_c = 0
    e_and_not_c = 0

    c_and_a = 0
    c_and_not_a = 0

    d_and_a_b = 0
    d_and_not_a_b = 0
    d_and_a_not_b = 0
    d_and_not_a_not_b = 0

    p_a_b = 0
    p_a_not_b = 0
    p_not_a_b = 0
    p_not_a_not_b = 0

    for i in range(len(arr[0])):
        if not arr[0][i] and not arr[1][i]:
            p_not_a_not_b += 1
        if arr[0][i]:  # a
            p_a += 1
            if arr[1][i]:  # a and b both true
                p_a_b += 1
            else:
                p_a_not_b += 1
        if arr[1][i]:  # b
            p_b += 1
            if not arr[0][i]:  # b true and a false
                p_not_a_b += 1
        if arr[2][i]:  # c
            p_c += 1
            if arr[0][i]:  # both c and a true
                c_and_a += 1
            else:
                c_and_not_a += 1  # c true and a false
        if arr[3][i]:  # d
            p_d += 1
            if arr[0][i] and arr[1][i]:  # d true and a true and b true
                d_and_a_b += 1
            elif arr[0][i] and not arr[1][i]:
                d_and_a_not_b += 1
            elif not arr[0][i] and arr[1][i]:
                d_and_not_a_b += 1
            else:
                d_and_not_a_not_b += 1

        if arr[4][i]:  # e
            p_e += 1
            if arr[2][i]:  # e and c both true
                e_and_c += 1
            else:  # e true and c false
                e_and_not_c += 1

        if arr[5][i]:  # f
            p_f += 1
            if arr[2][i]:  # f and c bot true
                f_and_c += 1
            else:
                f_and_not_c += 1  # f true c false
        if arr[6][i]:  # g
            p_g += 1
            if arr[3][i]:  # g and d both true
                g_and_d += 1
            else:
                g_and_not_d += 1  # g true and d false

    g_d = g_and_d / p_d  # G|D
    not_g_d = 1 - g_d
    g_not_d = g_and_not_d / (number_of_data - p_d)
    not_g_not_d = 1 - g_not_d

    f_c = f_and_c / p_c  # F|C
    not_f_c = 1 - f_c
    f_not_c = f_and_not_c / (number_of_data - p_c)
    not_f_not_c = 1 - f_not_c

    e_c = e_and_c / p_c  # E|C
    not_e_c = 1 - e_c
    e_not_c = e_and_not_c / (number_of_data - p_c)
    not_e_not_c = 1 - e_not_c

    c_a = c_and_a / p_a  # C|A
    not_c_a = 1 - c_a
    c_not_a = c_and_not_a / (number_of_data - p_a)
    not_c_not_a = 1 - c_not_a

    d_a_b = d_and_a_b / p_a_b  # D| A,B and all combinations
    not_d_a_b = 1 - d_a_b
    d_not_a_b = d_and_not_a_b / p_not_a_b
    not_d_not_a_b = 1 - d_not_a_b
    d_a_not_b = d_and_a_not_b / p_a_not_b
    not_d_a_not_b = 1 - d_a_not_b
    d_not_a_not_b = d_and_not_a_not_b / p_not_a_not_b
    not_d_not_a_not_b = 1 - d_not_a_not_b

    p_a /= number_of_data  # probabilities of A,B,C,D,E,F,G
    p_b /= number_of_data
    p_c /= number_of_data
    p_d /= number_of_data
    p_e /= number_of_data
    p_f /= number_of_data
    p_g /= number_of_data

    query_variables = input("Please give query variables:")
    evidence_variables = input("Please give evidence variables:")
    pay = query_variables.split(" ")
    payda = evidence_variables.split(" ")
    pay2 = copy.deepcopy(pay)
    isImpossible = False
    for items in payda:
        if items not in pay2:
            pay2.append(items)
        if "n" + items in pay2:
            isImpossible = True
        if len(items) == 2:
            if items[1] in pay2:
                isImpossible = True

    # pay = ["D", "nG", "A", "C"]
    # payda = ["A", "C"]
    if not isImpossible:
        a = findProbabilityWithBayesian(pay2)
        b = findProbabilityWithBayesian(payda)

        print(a / b)

        print(find_solution_with_data_only(pay, payda, arr))
    else:
        print(0)
        print(0)
