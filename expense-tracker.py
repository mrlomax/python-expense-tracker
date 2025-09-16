def main():
    my_list = [1, 2]
    my_list.append(3)
    my_list[0] = 0
    my_list.insert(1, 1)
    my_list.pop()
    print(my_list)

if __name__ == '__main__':
    main()