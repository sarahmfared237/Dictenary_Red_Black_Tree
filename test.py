from Dictionary import Dictionary

def main():
    dic = Dictionary()
    dic.load("words")
    size_validation(dic)


def size_validation(dic:Dictionary):
    print(f'Size:{dic.size()} | Height:{dic.rbTree_height()}')

if __name__ == "__main__":
    main()