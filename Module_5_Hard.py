import time

class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return


    def register(self, nickname, password, age):
        for names in self.users:
            if nickname ==  names.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self,*args):
        for i in args:
            if not i.title in self.videos:
                self.videos.append(i)

    def get_videos(self, word):
        videolist = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                 videolist.append(i.title)
        return videolist

    def watch_video(self, name):
        if not self.current_user is None:
            for titles in self.videos:
                if name == titles.title:
                    if titles.adult_mode and self.current_user.age >= 18:
                        i = 1
                        while i <= titles.duration:
                            print(i, end=' ')
                            time.sleep(1)
                            i += 1
                        print('Конец фильма')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
