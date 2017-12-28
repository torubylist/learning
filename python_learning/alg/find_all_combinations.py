##给定一个数组,给定一个target值,输出所有该数组中的数的和等于目标值的组合.
例如数组,[2,3,6,7]
目标值,7
输出:[[2,2,3],
     [7]
     ]

#------------------------------------------------------------
def find_all_combinations(arr,target):
    tmp_arr    = []
    result = []
    dfs(arr, result, tmp_arr, 0,target)

def dfs(arr, result, tmp_arr, tmp_target, target):
    if tmp_target == target:
        result << tmp_arr
        return
    for i in range(len(arr)):
        if target > tmp_target + arr[i]
            new_arr  = tmp_arr[:]
            new_arr.append(arr[i])
            dfs(arr, result, new_arr, tmp_target + arr[i],target)
