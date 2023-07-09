# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint


def queens_positions(positions=None) -> list:
    '''Генерация позиций ферзей'''
    if positions is None:
        positions = list((randint(0, 7), randint(0, 7)) for pos in range(8))
    print(positions)
    return positions


def fill_chessboard(gen_positions: list) -> list:
    '''заполнение доски ферзями'''
    chess_table = [[0 for _ in range(8)] for _ in range(8)]
    for queen_pos in range(len(gen_positions)):
        position = gen_positions[queen_pos]
        chess_table[position[0]][position[1]] = 1
    return chess_table


def find_beaten(queens_poses_list: list, chess_board_list: list) -> tuple[list[bool], list[tuple]]:
    ''' Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
    Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''

    unbeaten_queen_pos = []
    isnt_beaten = []
    for queen in queens_poses_list:
        row = queen[0]
        column = queen[1]
        diagonal_results = \
            [True if chess_board_list[i][j] == 1 else False for dr, dc in [(-1, -1), (1, -1), (-1, 1), (1, 1)]
             for i, j in zip(range(row + dr, len(chess_board_list), dr),
                             range(column + dc, len(chess_board_list[0]), dc))]

        horizontal_results = \
            [True if chess_board_list[row][j] == 1 else False for j in range(len(chess_board_list[0]))]

        vertical_results = \
            [True if chess_board_list[i][column] == 1 else False for i in range(len(chess_board_list))]

        results = diagonal_results + horizontal_results + vertical_results
        final_result = not any(results)
        if final_result:
            unbeaten_queen_pos.append(queen)
            isnt_beaten.append(final_result)
        return isnt_beaten, unbeaten_queen_pos


if __name__ == "__main__":
    queens_poses = queens_positions()
    chess_board = fill_chessboard(queens_poses)
    isnt_beaten_final, unbeaten_queen_pos = find_beaten(queens_poses, chess_board)
    if len(isnt_beaten_final) == 0:
        print("Нет исходов, при которых ферзи не бьют друг друга")
    elif len(isnt_beaten_final) > 0:
        for result in unbeaten_queen_pos:
            print(f"Исход при котором ферзь не побит имеется. Позиция ферзя - {result}")
