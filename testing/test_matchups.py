from modules.matchups import Matchups
import timeit

def test_completed_matchups():
    start = timeit.default_timer()
    matchup = Matchups()
    completed = matchup.get_completed_matchups()
    # assert(len(completed)==156089)
    print(len(completed))
    # print(completed[5])
    stop = timeit.default_timer()
    print('Time: ', stop - start)
