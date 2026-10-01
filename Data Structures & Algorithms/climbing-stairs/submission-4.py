class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Question:
        How many distinct ways can we climb n stairs if each move
        can be either 1 step or 2 steps?

        Key idea:
        To reach step n, the last move must come from either:
        - step n - 1 using 1 step
        - step n - 2 using 2 steps

        Therefore:
        ways(n) = ways(n - 1) + ways(n - 2)

        This follows the Fibonacci pattern:
        ways(1) = 1
        ways(2) = 2

        We only store the previous two results, so:
        Time: O(n)
        Space: O(1)
        """

        # Base cases:
        # There is 1 way to reach step 1 and 2 ways to reach step 2.
        if n <= 2:
            return n

        # Number of ways to reach the previous two steps.
        one_step_before = 2  # ways(2)
        two_steps_before = 1  # ways(1)

        # Calculate the number of ways for each step from 3 to n.
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before

            # Shift the previous values forward.
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before