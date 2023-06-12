import getpass

def get_login_id():
    try:
        return getpass.getuser()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to retrieve the login ID
login_id = get_login_id()

# Print the login ID
if login_id:
    print(f"Login ID: {login_id}")
else:
    print("Failed to retrieve the login ID.")