import types


class QueryOperator:
    def apply(self, args):
        return None

    def input_type(self):
        return types.StringType
            
    def return_type(self):
        return types.StringType