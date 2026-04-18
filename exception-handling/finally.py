try:
    print("Raising Exception...")
    raise ValueError
finally:
    print("Performing clean up in Finally...")