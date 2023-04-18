from Dictionary import Dictionary

def main():
    dic = Dictionary()
    dic.load("EN-US-Dictionary")
    # size_validation(dic)
    while(True):
        y=input("If you want to insert press 1\nIf you want to look up a word press 2\n")
        if y=="1":  
            word=input("Enter the word you want to insert\n")
            dic.insert_word(word)
            size_validation(dic)
        elif y=="2":   
            look=input("Enter the word you want to look for\n")   
            if(dic.look_up(look)):
                print("Yes")
            else:
                print("No")
        else:
            break 
    
        


def size_validation(dic:Dictionary):
    print(f'Size:{dic.size()} | Height:{dic.rbTree_height()}')

if __name__ == "__main__":
    main()