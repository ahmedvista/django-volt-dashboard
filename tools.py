def prompt_module():
    from tools.deploy import deploy
    from tools.generate_models import generate_moodels_png

    while True:
        user_input = input("deploy [1] generate_models [2]").strip().lower()
        if user_input == "1":
            deploy()
            break
        elif user_input == "2":
            generate_moodels_png()
            break
        # else:
        #     return True


if __name__ == "__main__":
    prompt_module()
