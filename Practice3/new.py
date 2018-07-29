import re


class StatisticsCalculator:
    user = {}
    city = {}
    total_distance = 0

    def process(self, line: str) -> str:

        # You must enter code here
        input = re.split('[-:]', line)
        if len(input) == 4:
            cur_distance = int(input[3])

            if input[0] in self.user:
                self.user[input[0]] += cur_distance
            else:
                self.user[input[0]] = cur_distance

            self.total_distance += cur_distance

            if input[1] in self.city:
                self.city[input[1]] += 1
            else:
                self.city[input[1]] = 1

            if input[2] in self.city:
                self.city[input[2]] += 1
            else:
                self.city[input[2]] = 1
        if len(self.user) != 0 and len(self.city) != 0:

            max_num = max(self.city.values())
            max_city = sorted([k for k, v in self.city.items() if v == max_num])[0]

            return (str(self.total_distance) + ":" + str(max(self.user, key=self.user.get)) + ":" + str(max_city))
        else:
            return ""
