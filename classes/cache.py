import pickle


class ContinueDate():
    def __init__(self, startPage, endPage):
        self.startPage = startPage
        self.endPage = endPage


def save_continue_date(obj):
    try:
        with open("pickles/continue-date.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_continue_date():
    try:
        with open("pickles/continue-date.pickle", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        return None


class PeakFlag():
    def __init__(self, param):
        self.unixTime = param


def save_peak_flag(obj):
    try:
        with open("pickles/peak-flag.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_peak_flag():
    try:
        with open("pickles/peak-flag.pickle", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        return None
