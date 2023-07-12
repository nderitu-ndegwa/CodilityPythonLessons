def binary_gap (n) :
    n = int(input())

    binary = ""
    max_count = 0
    count = 0
    prev_num = "0"

    while (n > 0) :
        binary += str(n % 2)
        n //= 2

        for n_bin in binary:
            if n_bin == "1":
                if count > max_count:
                    max_count = count
                count = 0
            elif n_bin == "0":
                count += 1
            else:
                raise ValueError("Error at: " + n_bin)
            prev_num = n_bin
        return max_count

    ##return binary[::-1]
 
    