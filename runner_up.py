def my_funct():
  list_arr = list(arr)
  sorted_list = sorted(list_arr)
  sorted_list = list(dict.fromkeys(sorted_list))
  sorted_list.pop()
  max_val = max(sorted_list)
  print(max_val)



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_funct()
