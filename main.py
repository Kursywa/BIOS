# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def main():
    argument1 = sys.argv[1]
    argument2 = sys.argv[2]
    with open(argument1 + ".txt", "r") as reader:  # reading first sequence
        seq1 = reader.readlines()
        print(seq1)
        reader.close()
    with open(argument2 + "txt", "r") as reader:  # reading second sequence
        seq2 = reader.readlines()
        print(seq2)
        reader.close()


def smith_waterman(seq1, seq2, match = 2, mismatch = -2, gap_penalty = -1):
    rows, cols = len(seq1) + 1, len(seq2) + 1
    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]  # initializing a matrix that holds both sequences plus
    # initial null column and row and fills them with zeros

    # initializing variables that hold information about maximum score
    max_score = 0
    max_row, max_col = 0, 0

    # iterating through the sequences and filling the scoring matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i - 1] == seq2[j - 1]:
                match_score = score_matrix[i-1][j-1] + match
            else:
                match_score = score_matrix[i-1][j-1] + mismatch

            delete_score = score_matrix[i-1][j] + gap_penalty # according to seq2
            insert_score = score_matrix[i][j-1] + gap_penalty

            score_matrix[i][j] = max(0, match_score, delete_score, insert_score) # comparison and choosing the highest value
            # 0 as possibility is the difference between smith-waterman and wunsch-needleman algorithm

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
