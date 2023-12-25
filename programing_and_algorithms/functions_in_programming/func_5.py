# 5 зад. Организирана е среща на високо ниво. В една от залите има въртящ се бар, като всеки може да завърти плота и в двете посоки.
# Да се състави програма, която по въведени брой позиции в бара [5..20], текуща позиция на клиента и позиция на желана напитка се избира най-късия път в кръга.


def shortest_path(total_positions, current_position, desired_position):
    # Изчисляване на разстоянието в посока по часовниковата стрелка 
    clockwise_distance = (desired_position - current_position + total_positions) % total_positions

    # Изчисляване на разстоянието в посока обратна на часовниковата стрелка 
    counterclockwise_distance = (current_position - desired_position + total_positions) % total_positions

    # Определяне на посоката, в която е най-късият път
    if clockwise_distance <= counterclockwise_distance:
        return clockwise_distance
    else:
        return counterclockwise_distance

# Входни данни
total_positions, current_position, desired_position = map(int, input().split())

# Изчисляване и извеждане на резултата
result = shortest_path(total_positions, current_position, desired_position)
print(result)
