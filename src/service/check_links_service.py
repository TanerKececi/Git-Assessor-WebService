from doctest import run_docstring_examples
from src.model.git_link import Git_Links
from ..rule_service.readme_rule import *
from ..rule_service.all_commit import all_commit
from ..rule_service.commit_comments import commit_comments_service
from ..rule_service.feature_branch import feature_branch_service
from github import Github
from .check_repo_service import check_repo_service
from concurrent.futures import ThreadPoolExecutor
import time




def check_links_service(link : Git_Links):

    start = time.time()
    print("hello")


    result={}

    rules = link.rules
    rules = list(rules)

    strRules = ""

    for rule in rules:
        strRules += rule

    rules = strRules.replace(',','')
    
    
    
    access_token = "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"

    repoExecutor = ThreadPoolExecutor(max_workers=5)

    
    
    if link.link5 is not None:
        r1 = repoExecutor.submit(check_repo_service, link.link1, rules, access_token)
        r2 = repoExecutor.submit(check_repo_service, link.link2, rules, access_token)
        r3 = repoExecutor.submit(check_repo_service, link.link3, rules, access_token)
        r4 = repoExecutor.submit(check_repo_service, link.link4, rules, access_token)
        r5 = repoExecutor.submit(check_repo_service, link.link5, rules, access_token)
        result.update(r1.result())
        result.update(r2.result())
        result.update(r3.result())
        result.update(r4.result())
        result.update(r5.result())
        #result[list(r5.result().keys())[0]] = r5.result()
    
    elif link.link4 is not None:
        r1 = repoExecutor.submit(check_repo_service, link.link1, rules, access_token)
        r2 = repoExecutor.submit(check_repo_service, link.link2, rules, access_token)
        r3 = repoExecutor.submit(check_repo_service, link.link3, rules, access_token)
        r4 = repoExecutor.submit(check_repo_service, link.link4, rules, access_token)
        result.update(r1.result())
        result.update(r2.result())
        result.update(r3.result())
        result.update(r4.result())
        #result[list(r4.result().keys())[0]] = r4.result()
    
    elif link.link3 is not None:
        r1 = repoExecutor.submit(check_repo_service, link.link1, rules, access_token)
        r2 = repoExecutor.submit(check_repo_service, link.link2, rules, access_token)
        r3 = repoExecutor.submit(check_repo_service, link.link3, rules, access_token)
        result.update(r1.result())
        result.update(r2.result())
        result.update(r3.result())
        #result[list(r3.result().keys())[0]] = r3.result()
    
    elif link.link2 is not None:
        
        r1 = repoExecutor.submit(check_repo_service, link.link1, rules, access_token)
        r2 = repoExecutor.submit(check_repo_service, link.link2, rules, access_token)

        result.update(r1.result())
        result.update(r2.result())
        
        #result[list(r2.result().keys())[0]] = r2.result()
    
    elif link.link1 is not None:
        r1 = repoExecutor.submit(check_repo_service, link.link1, rules, access_token)
        result.update(r1.result())
        #result[list(r1.result().keys())[0]] = r1.result()
    else:
        return result
    
    end = time.time()
    print("Project execution time: " + str(end - start))
    return result