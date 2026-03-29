class BaseJob:
    def __init__(self, spark, config):
        self.spark = spark
        self.config = config

    def extract(self):
        raise NotImplementedError("Extract method not implemented")

    def transform(self, df):
        raise NotImplementedError("Transform method not implemented")

    def load(self, df):
        raise NotImplementedError("Load method not implemented")

    def run(self):
        print(f"Starting job: {self.__class__.__name__}")
        df = self.extract()
        df_transformed = self.transform(df)
        self.load(df_transformed)
        print(f"Completed job: {self.__class__.__name__}")