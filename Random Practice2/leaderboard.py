
class LeaderBoard:
    def __init__(self):
        self.leaderboard = {}

    def add_score(self, player_id, score):

        # format of leaderboard :
        # {
        #   player_id1 : [avg1,[score1.1,score1.2,score1.3,...]]
        #   player_id2 : [avg2,[score2.1,score2.2,score2.3,...]]
        # }

        if player_id in self.leaderboard:
            self.leaderboard[player_id][1].append(score)
            avg = sum(self.leaderboard[player_id][1])/len(self.leaderboard[player_id][1])
            self.leaderboard[player_id][0] = avg
            return avg

        self.leaderboard[player_id] = [score,[score]]
        return score

    def top(self, no_of_top_players):
        top_list = []
        for key,value in sorted(self.leaderboard.items(),key=lambda e:e[1], reverse=True):
            top_list.append(key)
        return top_list[:no_of_top_players]

    def reset(self, player_id):
        if player_id in self.leaderboard:
            self.leaderboard[player_id][0] = 0
            self.leaderboard[player_id][1] = []

leader_board = LeaderBoard()

print(leader_board.add_score(1,50))
print(leader_board.add_score(2,80))
print(leader_board.add_score(2,70))
print(leader_board.add_score(2,60))
print(leader_board.add_score(3,90))
print(leader_board.add_score(3,85))


print("\n",leader_board.top(3))
# print(leader_board.top(2))
# print(leader_board.top(1))


# leader_board.reset(3)

# print(leader_board.top(3))

#
# def solution(A):
#     sumation = 0
#     for each_number in A:
#         if len(str(abs(each_number))) == 2:
#             sumation += each_number
#     return sumation