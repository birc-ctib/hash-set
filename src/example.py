import argparse


def main():
    argparser = argparse.ArgumentParser(description="Example program")
    argparser.add_argument("everything", nargs="*")
    args = argparser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
