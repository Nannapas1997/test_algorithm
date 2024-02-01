def alien_to_integer(s):
    symbol_values = {'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000}
    total = 0
    prev_value = 0
    
    for symbol in s:
        value = symbol_values[symbol]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    
    return total
