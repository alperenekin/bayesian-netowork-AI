import numpy as np
from itertools import product
import copy



def find_solution(data):
    ac_count = 0
    dg_count = 0
    for i in range(len(data[0])):
        if data[0][i] == True and data[2][i] == True:
            ac_count += 1
            if data[3][i] == True and data[6][i] == False:
                dg_count += 1
    print(dg_count / ac_count)


def find_independent_prob(p_a, p_b, p_c, p_d, p_e, p_f, p_g, data):
    for i in range(len(data[0])):
        if data[0][i]:
            p_a += 1
        if data[1][i]:
            p_b += 1
        if data[2][i]:
            p_c += 1
        if data[3][i]:
            p_d += 1
        if data[4][i]:
            p_e += 1
        if data[5][i]:
            p_f += 1
        if data[6][i]:
            p_g += 1
    p_a /= len(data[0])
    p_b /= len(data[0])
    p_c /= len(data[0])
    p_d /= len(data[0])
    p_e /= len(data[0])
    p_f /= len(data[0])
    p_g /= len(data[0])
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
    print(b)
    result = equation_dict[a] * equation_dict[b] * equation_dict[c + a] * equation_dict[e + c] * equation_dict[g + d] * equation_dict[c + a] * equation_dict[d + a + b] * equation_dict[f + c]

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


if __name__ == '__main__':
    arr = np.load('data 1.npy')
    number_of_data = len(arr[0])

    p_a = 0  # TODO make them one line
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
    print(p_g)

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

    pay = ["A", "C"]
    payda = ["A", "C"]
    pay_list = []
    pay_dict = {}
    for item in pay:
        if len(item) == 1:
            pay_dict[item] = variable_dict[item]
            pay_dict["n" + item] = variable_dict["n" + item]
            del variable_dict[item]
            del variable_dict["n" + item]
        else:
            pay_dict[item] = variable_dict[item]
            pay_dict[item[1]] = variable_dict[item[1]]
            del variable_dict[item]
            del variable_dict[item[1]]

    for missing_variables in list(variable_dict.keys()):
        if len(missing_variables) == 1:
            small_list = [missing_variables, "n" + missing_variables]
            pay_list.append(small_list)

    print(pay_list)
    print(list(variable_dict.keys()))

    a = 0
    for elements in product(pay_list[0]):
        print(list(elements))
        mylist = sortVariableList(list(elements), copy.deepcopy(pay))
        a += mainEquation(mylist[0], mylist[1], mylist[2], mylist[3], mylist[4], mylist[5], mylist[6])

    print(a)