class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len1, len2 = len(str1), len(str2)
        common_length = find_gcd(len1, len2)
        common_divisor = str1[:common_length]

        if str1[:common_length] == common_divisor and str2[:common_length] == common_divisor:
            return common_divisor
        else:
            return ""

# Example usage:
solution = Solution()

str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))  # Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))  # Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(solution.gcdOfStrings(str1, str2))  # Output: ""
