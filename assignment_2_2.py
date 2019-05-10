duration=[288.09999999999997, 288.1, 332.9, 358.5000000000001, 398.79999999999995, 417.60000000000014, 431.1999999999998,
 520.0999999999999, 541.0999999999999]

T_1 = 300
T_2 = 400

for i in duration:

    if duration[i] < T_1:
        append.my_str(S)

        if duration[i] > T_2:
            append.my_str(L)

            if T_1 < duration[i] < T_2:
                append.my_str(M)
