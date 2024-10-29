import time

def register():
    username = input("Enter username: ")
    with open("config.txt", "w") as f:
        f.write(f"{username}")
    print("Account created successfully.")
    time.sleep(1)
    exit()

if __name__ == "__main__":
    register()
