# @author: WillWang
# edit_distance : string, string  -> matrix , number
# to caculate edit distance between two strings and print distance_matrix
# algorithm
# example: edit_distance( 'cat','cool')
# to produce [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 1, 1, 2, 3], [0, 1, 2, 2, 3]]
#    the eidt distance is： 3

# def edit_distance(self,first,second):
# return edit distance between first and second & print distance_matrix
# tests: edit_distance( 'cat','cool'  )
# expected is: [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 1, 1, 2, 3], [0, 1, 2, 2, 3]]
#              The edit distance is:3

class algorithm():

    def __init__(self):
        pass
    def edit_distance(self,first,second):
        if len(first) > len(second):
            first,second = second,first
        if len(first) == 0:
            return len(second)
        if len(second) == 0:
            return len(first)
        first_length = len(first) + 1
        second_length = len(second) + 1
        distance_matrix = [range(second_length) for x in range(first_length)]

        for i in range(1,first_length):
            for j in range(1,second_length):
                deletion = distance_matrix[i-1][j] + 1
                insertion = distance_matrix[i][j-1] + 1
                substitution = distance_matrix[i-1][j-1]
                if first[i-1] != second[j-1]:
                    substitution += 1
                distance_matrix[i][j] = min(insertion,deletion,substitution)
        print distance_matrix
        print 'The edit distance is:'
        return distance_matrix[first_length-1][second_length-1]

if __name__ == "__main__":
    arith = algorithm()
    print arith.edit_distance( 'cat','cool'  )