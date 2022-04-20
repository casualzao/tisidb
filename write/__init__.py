def read():
    db = open("/Users/p.c.m.d/develop/project-python/tisidb/write/tisdb.txt")
    line = db.readline()
    while line:
        if line.__contains__('parse') or line.__contains__("None"):
            continue
        data = line.strip().split(" ")
        x = data[0]
        y = data[1]
        rho = data[4]
        p = data[7]
        line = db.readline()
        print(x, y, rho, p)


if __name__ == '__main__':
    read()
