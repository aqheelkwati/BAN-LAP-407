# 17. Create a function that takes the number of wins, draws and losses and calculates
# the number of points obtained so far for 'n' number of football teams . Print the
# winner team in the end . wins get +3 points, draws get +1 point, losses get -1 points .
# I/p:
# Team1(3, 4, 2) ## calculation : 33 +41 + 2(-1) = 11

# Team2(5, 0, 2) ## calculation : 53 + 01 + 2(-1) = 13
# Team3(0, 0, 1) ## calculation : 03 + 01 + 1(-1) = -1
# O/p:
# Winner: Team2


def winnerteam(*teams):
    maxpoints=0
    winner=''
    for i,team in enumerate(teams):
        points=(team[0]*3+team[1]*1+team[2]*-1)
        if  points>maxpoints:
            maxpoints=points
            winner=f'team{i+1}'
    print(f'winner is {winner}, points={maxpoints}')

Team1=(3, 4, 2) 
Team2=(5, 0, 2) 
Team3=(0, 0, 1)
winnerteam(Team1,Team2,Team3)
        