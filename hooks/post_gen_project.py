import os

PUBLISH_WORKFLOW = {{cookiecutter.add_publish_workflow}}


def main():
    if not PUBLISH_WORKFLOW:
        path = ".github/workflows/python-publish.yml"
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)


if __name__ == "__main__":
    main()
