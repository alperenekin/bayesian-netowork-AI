import numpy as np


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


if __name__ == '__main__':
    arr = np.load('data 1.npy')
    number_of_data = len(arr[0])
    # g_d = 0
    # not_g_d = 0
    # g_not_d = 0
    # not_g_not_d = 0
    # for i in range(len(arr[0])):
    #     if arr[3][i] == True and arr[6][i] == True:
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

    for i in range(len(arr[0])):
        if arr[0][i]:  # a
            p_a += 1
            if arr[1][i]:
                p_a_b += 1
            else:
                p_a_not_b += 1
        if arr[1][i]:  # b
            p_b += 1
        if arr[2][i]:  # c
            p_c += 1
            if arr[0][i]:  # both c and a true
                c_and_a += 1
            else:
                c_and_not_a = 1  # c true and a false
        if arr[3][i]:  # d
            p_d += 1
            if arr[1][i] and arr[2][i]:  # d true and a true and b true
                d_and_a_b += 1
            elif arr[1][i] and not arr[2][i]:
                d_and_a_not_b += 1
            elif not arr[1][i] and arr[2][i]:
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
    not_g_not_d = 1 - g_d
    g_not_d = g_and_not_d / (number_of_data - p_d)
    not_g_d = 1 - g_not_d

    f_c = f_and_c / p_c
    not_f_not_c = 1 - f_c
    f_not_c = f_and_not_c / (number_of_data - f_c)
    not_f_c = 1 - f_not_c

    e_c = e_and_c / p_c
    not_e_not_c = 1 - e_c
    e_not_c = e_and_not_c / (number_of_data - p_c)
    not_e_c = 1 - e_not_c

    c_a = c_and_a / p_a
    not_c_not_a = 1 - c_a
    c_not_a = c_and_not_a / (number_of_data - p_a)
    not_c_a = 1 - c_not_a

    d_a_b = d_and_a_b / p_a_b
    not_d_not_a_not_b = 1 - d_a_b
    d_not_a_b = d_and_not_a_b / (number_of_data - p_a_not_b)
    not_d_a_not_b = 1 - d_not_a_b
    d_a_not_b = d_and_a_not_b / p_a_not_b
    not_d_not_a_b = 1 - d_a_not_b
    d_not_a_not_b = d_and_not_a_not_b / (number_of_data - p_a_b)
    not_d_a_b = 1 - d_not_a_not_b

    p_a /= number_of_data
    p_b /= number_of_data
    p_c /= number_of_data
    p_d /= number_of_data
    p_e /= number_of_data
    p_f /= number_of_data
    p_g /= number_of_data
    print(p_g)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
