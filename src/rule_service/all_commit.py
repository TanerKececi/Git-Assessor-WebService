from github import Github
import time

def all_commit(contributors,commits):
    print("---all_commit started")
    start = time.time()
    

    dict = {}
    for contributor in contributors:
        dict[contributor.login] = False
    
    
    #for contributor in contributors:
    #    dict[contributor] = False
    #print(dict.)

    for commit in commits:
        try:
            if (commit.author.login is not None):
                dict[commit.author.login] = True
        except:
            print("No author name detected!")
    
    #contrbituro ve collaborator farklarına bak
    endTime = time.time()
    print("---all_commit ended at " + str(endTime - start))
    return dict

    