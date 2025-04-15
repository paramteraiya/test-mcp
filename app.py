route("/exception-new")
def generate_exception():
    print("Exception generated ......")
    try:
        sample_function()
        return "This should not be reached"
    except ZeroDivisionError as e:
        # Catch the specific error we know is occurring
        return f"Caught division by zero error: {str(e)}", 400
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {str(e)}", 500