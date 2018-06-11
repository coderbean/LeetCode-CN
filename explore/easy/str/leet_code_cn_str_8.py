class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        curr_list = [1]
        next_list = list()
        count = 1

        for i in range(n - 1):
            for j in range(len(curr_list)):
                if j + 1 == len(curr_list) or curr_list[j] != curr_list[j + 1]:
                    next_list.append(count)
                    next_list.append(curr_list[j])
                    count = 1  # 当一个数字被说完后，重新将计数器置为1
                else:
                    count = count + 1
            curr_list = next_list
            next_list = []
        return "".join(map(str, curr_list))


if __name__ == '__main__':
    solution = Solution()
    result = solution.countAndSay(5)
    print(result)
