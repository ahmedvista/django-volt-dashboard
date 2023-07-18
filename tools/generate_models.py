import os


def generate_moodels_png():
    exclude_models = [
        "LogEntry",
        "Token",
        "TokenProxy",
        "AbstractBaseSession",
        "Session",
        "AbstractUser",
        "Group",
        "Permission",
        "AbstractBaseUser",
        "PermissionsMixin",
        "ContentType",
    ]
    exclude = ",".join(exclude_models)
    args = [
        "--pydot",
        "--all-applications",
        "--group-models",
        "--color-code-deletions",
        "--arrow-shape normal",
        "--rankdir LR",
        "--theme django2018",
        f"--exclude-models {exclude}",
        "--output erd.png",
    ]
    args = " ".join(args)
    cmd = rf"env\Scripts\python.exe app/manage.py graph_models {args}"
    os.system(cmd)
