from doctest import run_docstring_examples
from src.model.git_link import Git_Links
from ..rule_service.readme_rule import *
from ..rule_service.all_commit import all_commit
from ..rule_service.commit_comments import commit_comments_service
from ..rule_service.feature_branch import feature_branch_service
from github import Github
from concurrent.futures import ThreadPoolExecutor
import time

def check_repo_service(indiv_link,rules, access_token):

    if(indiv_link != None):

            start = time.time()
            
            result = {}
            
            repo_result = {}

            txt = indiv_link.split("https://github.com/")

            g = Github(access_token)
            try:
                repo = g.get_repo(txt[1])
                result[repo.name] = {}
                repo_result['name'] = repo.name
                print("--REPO STARTED " + repo.name)
                
            except:
                return "Couldn't get repo from link {}".format(txt[1])
            
            contributors = repo.get_contributors()

            commits = repo.get_commits()
            
            branches = repo.get_branches()
            
            executor = ThreadPoolExecutor(max_workers=4)
            
            

            for rule in rules:

                if rule == "1":
                    t1 = executor.submit(all_commit, contributors,commits)
                    repo_result['commit'] = t1.result()

                elif rule == "2":

                    t2 = executor.submit(readme_rule_service, repo)
                    repo_result['readme'] = t2.result()

                elif rule == "3":

                    t3 = executor.submit(commit_comments_service, contributors, commits)
                    repo_result['commit_comments'] = t3.result()

                elif rule == "4":

                    t4 = executor.submit(feature_branch_service, contributors, branches)
                    repo_result['feature_branch'] = t4.result()

                else:
                    print("Unknown rule!!")
            

            
            
            
            result[repo.name].update(repo_result)
            
            endTime = time.time()
            print("--" + repo.name +  " finished working in " + str(endTime - start))
            return result

