import csv

FEATURE = 35

with open("ionosphere.txt", 'r') as f:
    with open ("sample_writer_row.csv", "w") as output:
        data = f.readlines()
        for i in range(len(data)):
            each_feature = data[i].split()
            s = [float(each_feature[0])]
            l = 1
            for j in range(1,FEATURE):
                x = each_feature[l].split(":")
                if j == float(x[0]):
                    s.append(float(x[1]))
                    if l < len(each_feature) - 1:
                        l = l + 1
                else:
                    s.append(0)
            writer = csv.writer(output)
            writer.writerow(s)