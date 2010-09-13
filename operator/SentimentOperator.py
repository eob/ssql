import QueryOperator

class SentimentOperator(QueryOperator.QueryOperator):
    def apply(self, args):
        return "positive"

def main():
    op = SentimentOperator()
    print op.apply("This is a test")

if __name__ == "__main__":
    main()