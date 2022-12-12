def to_camel_case(n: str, capitalize_first: bool):
    if n.find("_") == -1:
        sp = " "
    else:
        sp = "_"
    elif not capitalize_first:
        new = new[0].lower() + new[1:]
        return new
    new = n.title().replace(sp, "")
    if capitalize_first:
        return new

if __name__ == "__main__":
    print(to_camel_case("to_camel_case", True))