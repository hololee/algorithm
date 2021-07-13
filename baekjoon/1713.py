# 210428


import sys

if __name__ == '__main__':
    candidates_scores = list()
    candidates_names = list()  # left is older then right.

    n_frame = int(sys.stdin.readline())
    n_students = int(sys.stdin.readline())

    min_val = 0

    for recd_stu in sys.stdin.readline().split():
        if recd_stu in candidates_names:
            # add.
            candidates_scores[candidates_names.index(recd_stu)] += 1
        else:
            # check frame empty.
            if len(candidates_scores) < n_frame:
                candidates_scores.append(1)
                candidates_names.append(recd_stu)

            else:
                # remove old.
                removal_index = candidates_scores.index(min(candidates_scores))
                candidates_names.pop(removal_index)
                candidates_scores.pop(removal_index)

                # add new.
                candidates_scores.append(1)
                candidates_names.append(recd_stu)

    print(' '.join(list(map(str, sorted(list(map(int, candidates_names)))))))