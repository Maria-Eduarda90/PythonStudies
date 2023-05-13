from threading import Thread
from multiprocessing import Process

def funca0_a(nome):
    print(nome)

def main():
    t = Thread(target=funca0_a, args=("Minha Thread",))
    t.start()

    p = Process(target=funca0_a, args=("Meu Processo",))
    p.start()

if __name__ == '__main__':
    main()