class Solution:
    def canWin(self, s):
        if s is None or len(s) < 2:
            return False

        for i in range(len(s) - 1):
            if s[i] == "+" and s[i + 1] == "+":
                next_state = s[0 : i] + "--" + s[i + 2 :]
                if not self.canWin(next_state):
                    return True

        return False
