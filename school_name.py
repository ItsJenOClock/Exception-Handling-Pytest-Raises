def claim_unreserved_code_school_name(name):
    if name == "Ada Developers Academy":
        raise ValueError("There's already an awesome school with that name!")

    if name != "Ada Developers Academy":
        raise ValueError("You didn't enter the right name")
    
    return True

claim_unreserved_code_school_name("")
claim_unreserved_code_school_name("Ada Developers Academy")