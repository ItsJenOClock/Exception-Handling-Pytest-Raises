from school_name import claim_unreserved_code_school_name

def test_invalid_name_no_pytest():
    # Implement the equivalent of this test logic but DO NOT import or otherwise access pytest:

    # with pytest.raises(ValueError):
    #     claim_unreserved_code_school_name("Ada Developers Academy")

    # Think about what the test actually does and think about how to write them ourselves.

    # Replace this with your own logic
    try:
        claim_unreserved_code_school_name("University of Washington")
        assert ValueError, "Expected 'Ada Developers Academy'"

    except ValueError as error:
        print(f"{error}")

# test_invalid_name_no_pytest()
    # raise Exception("test not implemented")

#     def test_divide():
#     try:
#         divide(10, 0)
#         # This should not happen, so we raise an AssertionError
#         assert False, "Expected ZeroDivisionError but no exception was raised"
#     except ZeroDivisionError:
#         # This is the expected behavior, so the test passes
#         pass 

# test_divide()