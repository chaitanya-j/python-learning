class Rule:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.results = []


class Result:
    def __init__(self,row_no,res,value):
        self.row_no = row_no
        self.res = res
        self.value = value

    def __str__(self):
        return f'Result(row_no: {self.row_no}, result: {self.res}, value: {self.value})'

    def __repr__(self):
        return f'Result(row_no: {self.row_no}, result: {self.res}, value: {self.value})'
    