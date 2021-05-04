class Human:
    name = 'Petr'
    job = 'Programmer'
    born = 'Kyrgyzstan'
    merried = True

    def start(self):
        print('Happy birhday')

    def finish(self):
        print('Good job bro')


human_a = Human()

human_b = Human()

print(human_a.start())
print(human_b.finish())