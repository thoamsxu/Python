#求表达式中正数的和
#Python中，for...[if]...语句一种简洁的构建List的方法，从for给定的List中选择出满足if条件的元素组成新的List，其中if是可以省略的。
def positive_sum(num_list):
    positive_list = [i for i in num_list if i > 0]
    return sum(positive_list)


#enumerate
#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
def accum(tempstr):
    str_list = enumerate(list(tempstr))
    #ch[0] 表示索引
    #ch[1] 表示值
    new_list = [ch[1].title() + ch[1] * ch[0] for ch in str_list]
    
    return "-".join(new_list)


num_list = [1, -4, 7, 12]
tempstr = "RqaEzty"

print(positive_sum(num_list))
print(accum(tempstr))
