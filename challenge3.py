# given a string removing vowels from the string breaks it up to different substrings
# the total value of each substring is calculated and compared with the other substrings and the one with the highest value is returned

def solve(s):
    def consonant_value(c):
        # Calculate the value of a consonant character
        return ord(c) - ord('a') + 1  
    
    # Initialize variables for maximum and current values
    max_value = current_value = 0  
    
     # Iterate through each character in the input string and remove the vowels
     # If the character is a consonant Add its value to current_value
    for char in s: 
        if char in 'aeiou':  
            max_value = max(max_value, current_value)  
            current_value = 0  
        else:  
            current_value += consonant_value(char)  
            
        # update and return highest value of the consonant substring
    max_value = max(max_value, current_value)  
    return max_value 



