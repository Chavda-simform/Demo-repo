# i = [0,1,2,3,4,5,6,7,8] ;

# it = iter(i)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
square_iter = SquareIterator(5)
for square in square_iter:
    print(square)