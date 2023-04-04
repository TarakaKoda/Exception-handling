try:
    f = open("example_file.py")
    # bad = bad_var
# except FileNotFoundError:
#     print("sorry! file not found")
# except Exception:
#     print("opps! something went wrong")
except FileNotFoundError as a:
    print("sorry! this file is not found")
    print(a)
except NameError as e:
    print(e)


