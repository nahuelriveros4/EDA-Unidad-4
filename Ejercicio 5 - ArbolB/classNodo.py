class Item:
    def __init__(self, kyy=None, count=1, p=None):
        self.__kyy = kyy
        self.__count = count
        self.__p = p

    def get_key(self):
        return self.__kyy

    def set_key(self, kyy):
        self.__kyy = kyy

    def get_count(self):
        return self.__count

    def increment_count(self):
        self.__count += 1

    def get_p(self):
        return self.__p

    def set_p(self, p):
        self.__p = p
