class Generator:
    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(10):
            yield i
gen_iter = Generator()

for i in gen_iter:
    print(i)
