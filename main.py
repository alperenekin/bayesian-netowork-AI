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


def find_independent_prob(p_a,p_b,p_c,p_d,p_e,p_f,p_g,data):
    for i in range(len(data[0])):
        if data[0][i]:
            p_a += 1
        if data[1][i]:
            p_b +=1
        if data[2][i]:
            p_c +=1
        if data[3][i]:
            p_d +=1
        if data[4][i]:
            p_e +=1
        if data[5][i]:
            p_f +=1
        if data[6][i]:
            p_g +=1
    p_a /= len(data[0])
    p_b /= len(data[0])
    p_c /= len(data[0])
    p_d /= len(data[0])
    p_e /= len(data[0])
    p_f /= len(data[0])
    p_g /= len(data[0])


if __name__ == '__main__':
    arr = np.load('data 1.npy')
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

    for i in range(len(arr[0])):
        if arr[0][i]:
            p_a += 1
        if arr[1][i]:
            p_b += 1
        if arr[2][i]:
            p_c += 1
        if arr[3][i]:
            p_d += 1
        if arr[4][i]:
            p_e += 1
        if arr[5][i]:
            p_f += 1
        if arr[6][i]:
            p_g += 1
    p_a /= len(arr[0])
    p_b /= len(arr[0])
    p_c /= len(arr[0])
    p_d /= len(arr[0])
    p_e /= len(arr[0])
    p_f /= len(arr[0])
    p_g /= len(arr[0])
    print(p_g)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




