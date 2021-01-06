import numpy as np
from itertools import product
import copy


def find_solution(query, condition, data):  # yöntem 2 eklenece
    query_count = 0
    condition_count = 0
    for i in range(len(data[0])):
        q_match_count = 0
        match_count = 0
        for variable in condition:
            if len(variable) == 1:
                if data[ord(variable) - 65][i]:
                    match_count += 1
            else:
                if data[ord(variable[1])-65][i] == False:
                    match_count += 1

        if match_count == len(condition):
            condition_count +=1
            for q_variable in query:
                if len(q_variable) == 1:
                    if data[ord(q_variable) - 65][i]:
                        q_match_count += 1
                else:
                    if data[ord(q_variable[1]) - 65][i] == False:
                        q_match_count += 1

            if q_match_count == len(query):
                query_count += 1

    print(query_count / condition_count)


def mainEquation(a, b, c, d, e, f, g):
    equation_dict = {
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
    result = equation_dict[a] * equation_dict[b] * equation_dict[c + a] * equation_dict[e + c] * equation_dict[g + d] * \
             equation_dict[c + a] * equation_dict[d + a + b] * equation_dict[f + c]

    return result


def sortVariableList(given_list, missing_list):
    for item in given_list:
        missing_list.append(item)

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(missing_list) - 1):
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
    print(missing_list)
    return missing_list


def findProbabilityWithBayesian(variables):
    variable_dict = {
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

    pay_list = []
    for item in variables:
        if len(item) == 1:
            del variable_dict[item]
            del variable_dict["n" + item]
        else:
            del variable_dict[item]
            del variable_dict[item[1]]

    for missing_variables in list(variable_dict.keys()):
        if len(missing_variables) == 1:
            small_list = [missing_variables, "n" + missing_variables]
            pay_list.append(small_list)

    result = 0

    for elements in list(product(*pay_list)):
        sortedVariableList = sortVariableList(list(elements), copy.deepcopy(variables))
        result += mainEquation(sortedVariableList[0], sortedVariableList[1], sortedVariableList[2],
                               sortedVariableList[3], sortedVariableList[4], sortedVariableList[5],
                               sortedVariableList[6])

    return result


if __name__ == '__main__':
    arr = np.load('data 1.npy')
    number_of_data = len(arr[0])

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
            if arr[1][i]:
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
            if arr[2][i]:
                e_and_c += 1
            else:
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

    g_d = g_and_d / p_d
    not_g_d = 1 - g_d
    g_not_d = g_and_not_d / (number_of_data - p_d)
    not_g_not_d = 1 - g_not_d

    f_c = f_and_c / p_c
    not_f_c = 1 - f_c
    f_not_c = f_and_not_c / (number_of_data - p_c)
    not_f_not_c = 1 - f_not_c

    e_c = e_and_c / p_c
    not_e_c = 1 - e_c
    e_not_c = e_and_not_c / (number_of_data - p_c)
    not_e_not_c = 1 - e_not_c

    c_a = c_and_a / p_a
    not_c_a = 1 - c_a
    c_not_a = c_and_not_a / (number_of_data - p_a)
    not_c_not_a = 1 - c_not_a

    d_a_b = d_and_a_b / p_a_b
    not_d_a_b = 1 - d_a_b
    d_not_a_b = d_and_not_a_b / p_not_a_b
    not_d_not_a_b = 1 - d_not_a_b
    d_a_not_b = d_and_a_not_b / p_a_not_b
    not_d_a_not_b = 1 - d_a_not_b
    d_not_a_not_b = d_and_not_a_not_b / p_not_a_not_b
    not_d_not_a_not_b = 1 - d_not_a_not_b

    p_a /= number_of_data
    p_b /= number_of_data
    p_c /= number_of_data
    p_d /= number_of_data
    p_e /= number_of_data
    p_f /= number_of_data
    p_g /= number_of_data


    pay = ["D", "nG", "A", "C"]
    payda = ["A", "C"]

    a = findProbabilityWithBayesian(pay)
    b = findProbabilityWithBayesian(payda)
    print(a / b)

find_solution(["D","nG"],payda,arr)