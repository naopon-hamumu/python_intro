class StudentCard:
    def __init__(self, id, name):
        self.__id = id #外部からアクセスできないようにする
        self.__name = name

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

a = StudentCard(1234, '鈴木太郎')
# print(a.__id) アクセス不可
# print(b.__name)

print(a.get_id())
print(a.get_name())
