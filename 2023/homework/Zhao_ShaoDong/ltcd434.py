class Solution:
    def countSegments(self, s: str) -> int:

        start_index = 0 #初始化寻找空格的开始位置
        index_all = np.array([]) #为变量占位
        while True: #循环寻找
            index = s.find(' ', start_index) #从开始位置寻找空格
            index_all = np.append(index_all,[int(index)]) #记录空格位置
            if index == -1: #如果没有找到空格
                break  #退出循环
            start_index = index + 1 #找到空格后从下一个位置开始找

        index_all=index_all[:-1] #舍弃最后一个元素，一定是-1

        index_shift=np.insert(index_all[:-1],0,index_all[0]-1)#移动并且插入默认1初值

        diff=(index_all-index_shift) #利用np对两个数列做差

        countSgmts=np.count_nonzero(diff!=1) #找到阶跃的数目

        if index_all[0]!=0: #确认第一个空格前有无内容
            countSgmts=countSgmts+1
        if index_all[-1]!=len(s)-1: #确保最后一个空格后有无内容
            countSgmts=countSgmts+1
        return countSgmts #返回值

import sys #导入sys模组
import numpy as np #导入numpy模组


user_input = input("Enter a string: ") #从输入读取字符串

if len(user_input)>300: #长度限制
    sys.exit("Length of string exceed 300.") #值错误报错

if len(user_input)==0: #空字符串
    sys.exit("You have entered an empty string.") #提示空字符串

print("You entered:", user_input) #输出确认方才输入

solution_instance = Solution() #为类创建实例

sgmts_count = solution_instance.countSegments(user_input) #将用户输入传递给类实例

print("Number of segments:", sgmts_count) #输出结果
        