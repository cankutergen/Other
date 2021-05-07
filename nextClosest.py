class Solution:
    def nextClosest(self, time):
        minutes = int(time[0: 2]) * 60
        minutes += int(time[3:])

        digits = set()
        for char in time:
            if char != ":":
                digits.add(int(char))

        while True:
            minutes = (minutes + 1) % (24 * 60)
            next_time = [int(minutes / 60 / 10), int(minutes / 60 % 10), int(minutes % 60 / 10), int(minutes % 60 % 10)]

            is_valid = True
            for digit in next_time:
                if digit not in digits:
                    is_valid = False

            if is_valid:
                return str(next_time[0]) + str(next_time[1]) + ":" + str(next_time[2]) + str(next_time[3])
