import sys
sys.path.insert(0, './helper_functions')

def q67():
    data_67 = open("triangle.txt", "r")
    
    def prepare_data_67(x):
        lines = x.split('\n')[::-1]
        rows_str = [line.split(' ') for line in lines]
        rows_int = [[int(i) for i in line] for line in rows_str]
        return rows_int

    def calculate_best_results(acc, row):
        return [row[i] + max(acc[i], acc[i + 1]) for i in xrange(len(row))]

    rows = prepare_data_67(data_67)
    return reduce(calculate_best_results, rows)[0]
