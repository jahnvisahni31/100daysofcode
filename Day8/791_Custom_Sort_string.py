class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the count of each character in string s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # create the result string with the characters in the custom order
        result = ''
        for char in order:
            if char in char_count:
                result += char * char_count[char]
                char_count.pop(char)

        # Append any remaining characters from s that were not in the order string
        for char in char_count:
            result += char * char_count[char]

        return result
