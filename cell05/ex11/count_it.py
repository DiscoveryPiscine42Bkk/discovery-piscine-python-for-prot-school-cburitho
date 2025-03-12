import sys
if len(sys.argv) > 1:
    print(f"parameter: {len(sys.argv) - 1}")
    for param in sys.argv[1:]:
        print(f"{param} {len(param)}")
else:
    print("none")