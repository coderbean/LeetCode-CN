class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_list = list(str)
        ans = list()
        sign_accept = True  # 用来表示是否接受符号，和是否已经接受了字符
        begin = False
        for i in range(len(str)):
            if str_list[i].isspace():
                if not begin and sign_accept:
                    continue
                else:
                    break
            if str_list[i].isdigit() or (str_list[i] in ['-', '+'] and sign_accept):
                sign_accept = False
                ans.append(str_list[i])
            else:
                break

        if ans == ['-'] or ans == ['+']:
            return 0
        if ans:
            if int("".join(ans)) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif int("".join(ans)) < -2 ** 31:
                return -2 ** 31
            else:
                return int("".join(ans))
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.myAtoi("   +0 123")
    print(result)
