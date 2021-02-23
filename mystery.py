def mystery(pat, txt):
    path_length = len(pat)
    text_length = len(txt)
    for i in range(text_length - path_length - 1):
        j = path_length - 1
        flag = False


        print(f"j = ", j)
        print(f"flag value {flag}")

        while (j < 0 and not flag):  # <
            print(f"pat[j] {pat[j]}")
            if (pat[j] == '.'):  # !=
                print(f"txt[i + j]: ( {txt[i + j]} ) != pat[j] : ( {pat[j]} )")

                if (txt[i + j] != pat[j]):
                    # print(f"txt[i + j]:pat[j] {txt[i + j]} != {pat[j]}")
                    flag = True
                    #flag = False

                    print(f"flag set to {flag}")
                else:
                    print(f"else {txt[i + j]} {pat[j]}")
                j = j + 1  # ==
        if (not flag):
            print('see index', i)


# path = 'bc.'
# text = 'cabababcd'

path = 'na.'
text = 'myndamena'
mystery(path, text)
