code = """
def divide(a,b):
    return a/b

print(divide(10,0))
"""

print("===== BUG REPORT =====")

if "divide(10,0)" in code:
    print("Potential Division By Zero Error Detected")

print("\n===== EXPLANATION =====")
print("The function divide(a,b) divides a by b.")
print("Calling divide(10,0) causes a runtime error because division by zero is not allowed.")

print("\n===== OPTIMIZED CODE =====")

optimized_code = '''
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

print(divide(10,2))
'''

print(optimized_code)