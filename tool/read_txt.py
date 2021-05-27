def read_txt(filename):
    filepath = "./data/" + filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()

