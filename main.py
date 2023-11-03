# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def main():
    argument1 = sys.argv[1]
    argument2 = sys.argv[2]
    with open(argument1 + ".txt", "r") as reader:  # reading first sequence
        seq1 = "".join(reader.readlines())
        print(seq1)
        reader.close()
    with open(argument2 + ".txt", "r") as reader:  # reading second sequence
        seq2 = "".join(reader.readlines())
        print(seq2)
        reader.close()
    alignment, alignment_score = smith_waterman(seq1, seq2)
    print("Max score of alignment: ", alignment_score)
    print("alignment 1: ", alignment[0])
    print("alignment 2: ", alignment[1])
    with open("results.txt", "w") as writer:
        writer.write("Max score of alignment: " + str(alignment_score) + "\n")
        writer.write("alignment 1: " + alignment[0] + "\nalignment 2: " + alignment[1])
        writer.close()



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

            delete_score = score_matrix[i-1][j] + gap_penalty # according to seq1 -> rows vertical
            insert_score = score_matrix[i][j-1] + gap_penalty  # according to seq2 -> cols horizontal

            score_matrix[i][j] = max(0, match_score, delete_score, insert_score) # comparison and choosing the highest value
            # 0 as possibility is the difference between smith-waterman and wunsch-needleman algorithm
    # tracking back implementation
            # 1. update max_score
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_row, max_col = i, j

    # 2. tracebacking as in iterating through
    alignment1 = []
    alignment2 = []  # declaring arrays that holds alignments of respective sequences
    i,j = max_row, max_col  # setting up iterators to max_score

    while score_matrix[i][j] != 0:  # seeking whether score comes from diagonal match/mismatch or from indel gap
        if score_matrix[i][j] == score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):  # checking diagonally
            alignment1.insert(0, seq1[i-1])  # always adding at the beginning so chars added first will be pushed
            alignment2.insert(0, seq2[j-1])  # to the end
            i -= 1
            j -= 1  # updating iterators
        elif score_matrix[i][j] == score_matrix[i-1][j] + gap_penalty:  # going vertical so deletion for seq1 compared to seq2
            alignment1.insert(0, seq1[i-1])
            alignment2.insert(0, "-")  # "-" symbolizes deletion for particular alignment
            i -= 1
        # algorithm prioritizes deletions over insertion if the same score is present for both of these options
        else:  # going horizontal so insertion for seq1 compared to seq2
            alignment1.insert(0, "-")  #
            alignment2.insert(0, seq2[j-1])
            j -= 1

    # 3. returning the best alignment and its score
    best_alignment = ("".join(alignment1), "".join(alignment2))
    return best_alignment, max_score  # passing two arguments as results
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
