from dataclasses import dataclass

@dataclass(frozen=True)
class Strategy:
    fast_ema: int
    slow_ema: int
    losing_streak: int
    drawdown: float
    pnl: float
    total_commission: float
    average_spread: float

# simulated data
# fast ema , slow ema , losing streak , drawdown , PnL , commission , avg spread
strategies = [
    Strategy(10,30 , 4 ,8 ,450 , 35,1.2),
    Strategy(11,30 , 3 ,6 ,520 , 40,1.1),
    Strategy(12,30 , 5 ,12 ,600 , 45,1.3),
    Strategy(11,31 , 2 ,4 ,490 , 32,0.9),
    Strategy(15,40 , 3 ,5 ,700 , 50,1.0),
    Strategy(16,40 , 2 ,4 ,680 , 48,0.8),
]

def calculate_score(strategy: Strategy):
    return strategy.pnl - strategy.drawdown * 5

def find_strategy(fast_ema : int , slow_ema : int ):
    for strategy in strategies:
        if(strategy.fast_ema == fast_ema and strategy.slow_ema == slow_ema):
            return strategy
        return None

def get_neighbors(strategy : Strategy):
    candidates = [
        (strategy.fast_ema - 1, strategy.slow_ema),
        (strategy.fast_ema + 1, strategy.slow_ema),
        (strategy.fast_ema, strategy.slow_ema - 1),
        (strategy.fast_ema, strategy.slow_ema + 1),
    ]

    neighbors = []

    for fast_ema , slow_ema in candidates:
        if (fast_ema >= slow_ema):
            continue

        neighbor = find_strategy(fast_ema , slow_ema)
        if(neighbor is not None): neighbors.append(neighbor)

    return neighbors

def local_search(start: Strategy):
    current = start
    while True:
        neighbors = get_neighbors(current)

        best_neighbor = current

        for neighbor in neighbors:
            if(calculate_score(neighbor) > calculate_score(best_neighbor)):
                best_neighbor = neighbor

        if(best_neighbor == current): return current
        current = best_neighbor

start = strategies[0]
best = local_search(start= start)
print("best strategy flound:")
print(best)
print("Score: ", calculate_score(best))