# 210421

import sys
from collections import Counter

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    shortcuts = Counter()
    formatted_list = list()

    for i in range(n):
        dat = str(sys.stdin.readline()).replace('\n', '')

        # head check flag.
        is_formatted = False

        # check head of word.
        for wdx, word in enumerate(dat.split(' ')):
            candidate = str.upper(word[0])

            if shortcuts[candidate]:
                continue
            else:
                # available.
                shortcuts[candidate] += 1
                formatted_list.append(' '.join(dat.split(' ')[:wdx] + ['[' + word[:1] + ']' + word[1:]] + dat.split(' ')[wdx + 1:]))
                is_formatted = True

                break

        # check head formatted.
        if is_formatted:
            continue
        else:
            # search from first letter.
            for ldx, l in enumerate(dat):
                if l != ' ':
                    if shortcuts[str.upper(l)]:
                        continue
                    else:
                        # selected.
                        shortcuts[str.upper(l)] += 1
                        formatted_list.append(dat[:ldx] + '[' + dat[ldx] + ']' + dat[ldx + 1:])
                        is_formatted = True
                        break

        if is_formatted:
            continue
        else:
            formatted_list.append(dat)

    for item in formatted_list:
        print(item)
