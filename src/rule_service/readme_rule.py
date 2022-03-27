from github import Github
import time
def readme_rule_service(repo):
    start = time.time()
    print("----readme_rule started")

    try:
        contents = repo.get_contents("README.md").name
        endTime = time.time()
        print("----readme_rule ended " + str(endTime - start))
        return True
    except:
        contents = False

    try:
        contents = repo.get_contents("README.txt").name
        endTime = time.time()
        print("----readme_rule ended " + str(endTime - start))
        return True
    except:
        contents = False

    endTime = time.time()
    print("----readme_rule ended " + str(endTime - start))
    return contents