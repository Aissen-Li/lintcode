class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A or len(A) == 1:
            return 0

        count = 0
        far = 0
        i = 0
        jump_point = 0

        while i < len(A):
            step = A[i]
            if i == len(A) - 1:
                break

            if i + step >= len(A) - 1:
                count += 1
                break
            jump_range = A[i+1:i+1+step]

            for j in range(len(jump_range)):
                if i + 1 + j + jump_range[j] >= len(A) - 1:
                    count += 2
                    return count

                if i + j + 1 + jump_range[j] > far:
                    far = i + j + 1 + jump_range[j]
                    jump_point = j

            i = i + jump_point + 1
            count += 1
        return count