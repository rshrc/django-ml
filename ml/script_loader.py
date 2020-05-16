import pickle


class Loader:

    def __init__(self, filename, X_test):
        self.filename = filename
        self.X_test = X_test

    def load(self):
        loaded_model = pickle.load(open(self.filename, 'rb'))
        result = loaded_model.predict(self.X_test)
        return result
