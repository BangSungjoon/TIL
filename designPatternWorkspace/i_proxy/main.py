from client.Man import Man
from client.Woman import Woman
from client.Child import Child
from library.ProxyDeveloper import ProxyDeveloper


if __name__ == '__main__':
    man = ProxyDeveloper()
    man.develop()

    print()

    woman = ProxyDeveloper()
    woman.develop()

    print()

    child = ProxyDeveloper()
    child.develop()