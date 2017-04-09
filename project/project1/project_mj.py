class Matrix():
    def __init__(self,string):
        self.all = []
        if "l" in string:
            n = int(string[2])
            for i in range(n):
                row = [0]*n
                row[i] = 1
                self.all.append(row)
        else:
            string_list = string.split(";")
            for row in string_list:
                string_row_list = row.strip().split(" ")
                float_row_list = []
                for string in string_row_list:
                    float_row_list.append(float(string))
            self.append(float_row_list)

    def mymatrix(self):
        input_list = []
        for i in range(len(self.all)):
            for j in range(len(self.all[0])):
                self.all[i][j] = str(self.all[i][j])
            for row in self.all:
                input_list.append(" ".join(row))
            the_input = ";".joing(input_list)
            return Matrix(the_input)

    def show(self):
        output_string = ""
        for row in self.all:
            output_string = output_string + " ".join(str(x) for x in row) +"\n"
        print(out_put_string)
        return

    def row_size(self):
        return len(self.all)

    def col_size(self):
        return len(self.all[0])

    def compare(self, other):
        if (self.row_size() == other.row_size()) and (self.col_size() == other.col_size()):
            while (True):
                for i in range(self.row_size()):
                    for j in range(self.col_size()):
                        if self.all[i][j] != other.all[i][j]:
                            return False
                return True
        else:
            return False

    def __add__(self, other):
        answer_matrix = []
        input_list = []
        for i in range(self.row_size()):
            answer_matrix.append([])
        if (self.row_size() == other.row_size()) and (self.col_size() == other.col_size()):
            for j in range(self.row_size()):
                for k in range(self.col_size()):
                    answer = self.all[j][k] + other.all[j][k]
                    answer_matrix[j].append(str(answer))

