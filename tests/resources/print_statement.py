class PrintExample:

    def do_smth(self):
        a = 1
        b = 2
        c = a + b
        print(c)
        self.do_nothing("a")
        return c

    def do_nothing(self, name:str):
        pass