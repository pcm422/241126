class Eagle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"독수리의 이름은 {self.name}, 나이는 {self.age}살 입니다"

    def sound(self):
        return "삐악"