def app(*args):
    print(args)
if __name__ == '__main__':
    if app():
        print("2")
    app(1)