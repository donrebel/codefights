def groupingDishes(dishes):
    rd = {}
    for d in dishes:
        for i in range(1, len(d)):
            if d[i] in rd:
                rd[d[i]].append(d[0])
                rd[d[i]] = sorted(rd[d[i]])
            else:
                rd[d[i]] = [d[0]]
    ingredients = sorted(rd.keys())
    res = []
    for i in ingredients:
        if len(rd[i]) > 1:
            res_item = [i]
            res_item += rd[i]
            res.append(res_item)
    return res

# =========================================================
# Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there
# should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which
# strings[i] ≠ strings[j] and patterns[i] = patterns[j].

def areFollowingPatterns(strings, patterns):
    ls = len(strings)
    lp = len(patterns)
    if ls != lp:
        return False
    sd = {}
    pd = {}
    for i in range(ls):
        s_item = strings[i]
        p_item = patterns[i]
        if s_item in sd.keys():
            sd[s_item].append(i)
        else:
            sd[s_item] = [i]
        if p_item in pd.keys():
            pd[p_item].append(i)
        else:
            pd[p_item] = [i]
        if pd[p_item] != sd[s_item]:
            return False
    return True

# =========================================================
# Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in
# the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

def containsCloseNums(nums, k):
    d = {}
    res = False
    for i in range(len(nums)):
        n = nums[i]
        if n in d.keys():
            res = (k >= (i - d[n]))
            if res:
                return res
        d[n] = i
    return res

# =========================================================
dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]

assert groupingDishes(dishes) == [["Cheese", "Quesadilla", "Sandwich"],
                                  ["Chicken", "Chicken Curry", "Quesadilla"],
                                  ["Nuts", "Fried Rice", "Salad"],
                                  ["Onions", "Fried Rice", "Pasta"]]

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

res = groupingDishes(dishes)

assert groupingDishes(dishes) == [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]


strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]
assert areFollowingPatterns(strings, patterns) == True
strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]
assert areFollowingPatterns(strings, patterns) == False


nums = [1, 0, 1, 1]
k = 1
containsCloseNums(nums, k)

nums = [0, 1, 2, 3, 5, 2]
k = 3
assert containsCloseNums(nums, k) == True
nums = [0, 1, 2, 3, 5, 2]
k = 2
assert containsCloseNums(nums, k) == False