num=5
arr=[[1,2,3,4],[9,6,5,7,3]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==num:
            print(f"{i},{j}")
