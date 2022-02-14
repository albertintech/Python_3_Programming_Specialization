"""List Comprehension Example 1"""
import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"}, {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {
    'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}


inner_list = tester['info']
print(json.dumps(inner_list, indent=2))
# compri = <some list of name>
# compri = [<tranformer_expr> for <varname> in <seq> if <filtration expression>]
compri = [d['name'] for d in inner_list]
print(compri)
