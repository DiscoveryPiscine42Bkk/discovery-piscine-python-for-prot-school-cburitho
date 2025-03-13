import sys
def doecase_it(text):
    return text.lwer()
def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for param in sys.argv[1:]:
            print(doecase_it(param))
if __name__ == " __main__":
    main()