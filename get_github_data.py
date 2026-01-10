"""
queries the github rest API to find all the users in a certain organization
(https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28)

takes that response and puts it in github_data/raw_all_users.json



queries github rest api to get all repositories in an organization
(https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28)

takes that response and puts it in github_data/raw_all_repos.json



queries each repo from raw_all_repos

"""