class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)<=0:
            return s
        items = s.split(" ")
        print(items)
        res_items = []
        for item in items:
            print(type(item))
            item = item[::-1]
            res_items.append(item)
        res = ""
        for i,each in enumerate(res_items):
            res +=each
            if i!=len(res_items)-1:
                res +=" "
        return res
