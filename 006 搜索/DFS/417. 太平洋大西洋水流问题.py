import heapq


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade > other.grade if self.grade != other.grade else self.name < other.name

    def __str__(self):
        return f"name is {self.name}, grade is {self.grade}"


if __name__ == '__main__':
    q = []
    heapq.heappush(q, Student('tony', 89))
    heapq.heappush(q, Student('tom', 89))
    heapq.heappush(q, Student('rainbow', 99))
    heapq.heappush(q, Student('terry', 65))
    heapq.heappush(q, Student('Newton', 100))
    heapq.heappush(q, Student('trump', 69))

    for i in range(1, len(q) + 1):
        student = heapq.heappop(q)
        print(f"rank: {i},", student)
