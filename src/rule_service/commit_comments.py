from github import Github
import time

def commit_comments_service(contributors,commits):
    
    start = time.time()

    print("-----commit_comments started")


    dict = {}
    for contributor in contributors:
        dict[contributor.login] = True    

    for commit in commits:
        try:
            if (commit.get_comments() == None and dict[commit.author.login] == True):
                dict[commit.author.login] = False
        except:
            print("Couldn't get commit author login or commit comment")
    

    # commit message uzunluğu 15 karakterin altındaysa sayma
    endTime = time.time()
    
    print("-----commit_comments ended at " + str(endTime - start))
    return dict
   