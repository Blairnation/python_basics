
def main():
    final_list = []
    head = [1, 2, 3, 4, 5, 6]
    final = funct(head)
    for item in final:
        for i in item:
            final_list.append(i)
    print(final_list)


def funct(head):
    listed = []
  
    for index in range(0, len(head) - 1, 2):
        ans = (head[index + 1], head[index])
        listed.append(ans)
    return listed


main()
