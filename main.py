
"""
This repo is just to fulfill the "dummy assignment" requirement per the spec in https://gallettilance.github.io/assignments/assignment0/
"""

if __name__ == "__main__":
    print("Enter two numbers:")
    
    nums = []
    
    while len(nums) < 2:
        try:
            raw_input = input("> ")
            nums.append(int(raw_input))
            
        except ValueError:
            # nums.append(float(raw_input)) # TODO add proper handling
            print('Please enter a number')
            pass

    print(f"{nums[0]} + {nums[1]} = {sum(nums)}")

