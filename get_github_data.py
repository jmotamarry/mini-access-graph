"""
queries the github rest API to find all the users in a certain organization
(https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28)

takes that response and puts it in raw_github_data/all_users.json



queries github rest api to get all repositories in an organization
(https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28)

takes that response and puts it in raw_github_data/all_repos.json



queries each repo from raw_all_repos to get collaborators
(https://docs.github.com/en/rest/collaborators/collaborators?apiVersion=2022-11-28)

takes those responses and creates a json for each repo in raw_github_data/repo_collaborators/{repo_name}.json
"""