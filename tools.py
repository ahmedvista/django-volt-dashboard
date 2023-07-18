from tools.deploy import deploy


def prompt_module():
    while True:
        user_input = input("deploy [1]").strip().lower()
        if user_input == "1":
            deploy()
            break
        # elif user_input == "n":
        #     return False
        # else:
        #     return True


if __name__ == "__main__":
    prompt_module()
