try:
    f = open("example_file.py")
    if f.name == "example_file.py":
        raise Exception
    # bad = bad_var
# except FileNotFoundError:
#     print("sorry! file not found")
# except Exception:
#     print("opps! something went wrong")
except FileNotFoundError as a:
    print("sorry! this file is not found")
    print(a)
except Exception as e:
    print("Error!!!!!")
else:
    print(f.read())
    f.close()
finally:
    print("thank you")

