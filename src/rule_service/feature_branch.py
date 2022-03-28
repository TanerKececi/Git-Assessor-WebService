from github import Github
from github.Branch import Branch
import time

def feature_branch_service(contributors, branches):
    
    start = time.time()
    print("------feature_branch started")
    
    arr = []
    dict = {}

    for contributor in contributors:
        dict[contributor.login] = False   
    

    for branch in branches:
        if (dict[branch.commit.author.login] == False):
            dict[branch.commit.author.login] = True

    
    endTime = time.time()
    if len(arr) == contributors.totalCount:
        print("------feature_branch ended " + str(endTime-start))
        return dict
        
    else:
        print("------feature_branch ended " + str(endTime-start))
        return dict