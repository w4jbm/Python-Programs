with open("infile.txt") as f1:
    with open("outfile.txt", "w") as f2:
        for line in f1:
            f2.write(line)
