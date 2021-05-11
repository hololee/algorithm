with open('/prev_training/bbb', 'w') as f:
    f.write("1500000\n")
    for i in range(1500000):
        f.write('1 {}\n'.format(i + 1))
