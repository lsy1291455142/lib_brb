# @Author: mdrhri-6
# @Date:   2016-12-22T03:30:09+01:00
# @Last modified by:   mdrhri-6
# @Last modified time: 2017-02-13T15:08:06+01:00
# -*- coding: UTF-8 -*-


import json

from manipulate_data_new import RuleBase
from data import Data

def convert(input):
    # convert unicode to str in json
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

# Read data from file
# with open('temp_data.json') as file_data:
with open('test.json') as file_data:
# with open('2nd_order_tree.json') as file_data:
#with open('api/single_tree.json') as file_data:
# with open('sunonda_tree.json') as file_data:
# with open('agriculture_tree.json') as file_data:
#     data = json.load(file_data)
    data = convert(json.load(file_data))

# output_x2 = [[1,0,0],[0,1,0],[0,0,1]]
# output_x4 = [[1,0,0],[0.3,0.7,0],[0,0,0],[0.3,0.7,0],[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# # output_x6 = [[1,0,0], [0.4,0.6,0], [0,1,0], [0.2,0.8,0], [0,1,0], [0,0.2,0.8], [0.1,0.3,0.6], [0,0.2,0.8], [0,0,1]]
# output_x6 = [[1,0,0], [0.2,0.8,0], [0.1,0.3,0.6], [0.4,0.6,0], [0,1,0], [0,0.2,0.8], [0,1,0], [0,0.2,0.8], [0,0,1]]
# output_x6_shunxu = [0,3,6,1,4,7,2,5,8]
# # output_x8 = [[1, 0, 0], [0.3, 0.7, 0], [0, 0.3, 0.7], [0.4, 0.6, 0], [0, 1, 0], [0, 0.1, 0.9],[0.1, 0.3, 0.6], [0, 0.3, 0.7], [0, 0, 1]]
# output_x8 = [[1, 0, 0], [0.4, 0.6, 0], [0.1, 0.3, 0.6], [0.3, 0.7, 0], [0, 1, 0], [0, 0.3, 0.7],[0, 0.3, 0.7], [0, 0.1, 0.9], [0, 0, 1]]
# output_x9 = [[1, 0, 0], [0.2, 0.8, 0], [0.1, 0.2, 0.7], [0.2, 0.8, 0], [0, 1, 0], [0, 0.1, 0.9],[0.1, 0.2, 0.7], [0, 0.1, 0.9], [0, 0, 1]]
# output_dict_by_parent = dict()
# output_dict_by_parent = {'x2':output_x2,'x4':output_x4,'x6':output_x6,'x8':output_x8,'x9':output_x9}
# # print 'x2: {}'.format(output_x2)
#
# input_rule_weight_list_by_parent = dict()
# input_rule_weight_list_by_parent = {'x2':[1,1,1],
#                                     'x4':[1,0.7,0.5,0.7,0.7,0.5,1/3,1/3,1/3],
#                                     # 'x6':[1,1,1,1,0.4,1,0.2,1,1],
#                                     'x6':[1,1,0.2,1,0.4,1,1,1,1],
#                                     # 'x8':[1,0.2,0.8,1,0.4,1,1,1,1],
#                                     'x8':[1,1,1,0.2,0.4,1,0.8,1,1],
#                                     'x9':[1,0.6,1,0.6,0.6,1,1,1,1]}


obj_list = list()

# Save each node data as an object in a list
for each in data:
    obj = Data(**data[each])
    obj.name = str(each)
    obj_list.append(obj)

# Sort the obj_list based on is_input is true
# obj_list.sort(key=lambda x: int(x.antecedent_id[1:]))
obj_list.sort(key=lambda x: x.is_input == "true", reverse=True)
# obj_num = []
# obj_list.split('x')
# for each.antecedent_id in obj_list:
#     obj_num.append(each.antecedent_id[1:])

print "Initial nodes: {}".format([str(each.antecedent_id) for each in obj_list])

visited = list()

i = 0

count = 1

subtree = 1


res = dict()
result = list()

# While you have an object in obj_list
while len(obj_list):
    print "\n\nIteration: {}\n".format(count)
    count += 1

    # Get parent of the current node.
    parent = None
    # parent_id =
    for each in obj_list:
        if each.name == obj_list[i].parent:
            parent = each
            break

    visiting = list()

    # Find if there is any other node which has the same parent
    for j in range(i + 1, len(obj_list)):
        if obj_list[i].parent == obj_list[j].parent:
            visiting.append(obj_list[j])
    visiting.append(obj_list[i]) # Add the current node in the list
    visiting.sort(key=lambda x: int(x.antecedent_id[1:]))
    for each in visiting:
        if each.parent == each.name:
            visiting.remove(each)

    # Check if all the siblings has is_input true or not.
    isAllInput = True
    for each in visiting:
        if each.is_input != 'true':
            isAllInput = False

    if obj_list[0].name == obj_list[0].parent:
        print "Root node: {}, crisp_value:{}".format(obj_list[0].name, obj_list[0].crisp_val)
        break
    # if len(visiting) == len(obj_list):
    #     # Compute the BRB sub-tree for the nodes in visiting.
    #     print "Computing value of {} for {}".format(parent.antecedent_id,
    #                                                 [str(each.antecedent_id) for each in visiting if each.antecedent_id != parent.antecedent_id])
    #     # import pdb; pdb.set_trace()
    #     # brb_calculation = RuleBase()
    #     rule_base = RuleBase(visiting, parent)
    #     rule_base.output_val_list = output_dict_by_parent[parent.antecedent_id]
    #     rule_base.rule_weight_list = input_rule_weight_list_by_parent[parent.antecedent_id]
    #     row_list = rule_base.create_rule_base()
    #     rule_base.input_transformation()
    #     rule_base.activation_weight()
    #     rule_base.belief_update()
    #     consequence_val = rule_base.aggregate_rule()
    #     parent.consequent_values = consequence_val
    #     result.insert(count, consequence_val)
    #     parent.consequence_val = consequence_val
    #
    #     crisp_val = 0.0
    #     for i in range(len(parent.ref_val)):
    #         crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])
    #
    #     parent.input_val = str(crisp_val)
    #
    #     # import pdb; pdb.set_trace()
    #
    #     print "Rule Row List: {}".format([each.__dict__ for each in row_list])
    #
    #
    #     print "\nAll the current nodes have same parent \"{}\" so the tree traversal is done and the ultimate output is: {}".format(parent.antecedent_id, parent.antecedent_id)
    #
    #     print "Calculated consequence values for {} are: {}".format(parent.antecedent_id, consequence_val)
    #
    #     print "Crisp Value: {}".format(str(crisp_val))
    #
    #     break

    print "For {}, parent is: {}".format(str(obj_list[i].antecedent_id), parent.antecedent_id)

    # if not all the siblings has same parent, continue to the next node of obj_list
    if not isAllInput:
        i += 1
        print "Current Nodes: {}".format([str(each.antecedent_id) for each in visiting])
        print "All the children for parent {} is not calculated yet".format(parent)
        obj_list.sort(key=lambda x: x.is_input == "true", reverse=True)
        # obj_list.sort(key=lambda x: int(x.antecedent_id[1:]))
        continue
    else:
        # Compute the BRB sub-tree for the nodes in visiting.
        print "Computing value of {} for {}".format(parent.antecedent_id, [str(each.antecedent_id) for each in visiting])
        # import pdb; pdb.set_trace()
        # brb_calculation = RuleBase()
        rule_base = RuleBase(visiting, parent)
        # rule_base.output_val_list = output_dict_by_parent[parent.antecedent_id]
        # print 'rule_base.output_val_list: {}'.format(rule_base.output_val_list)
        rule_base.output_val_list = parent.output_weight_values
        print 'rule_base.output_val_list: {}'.format(rule_base.output_val_list)
        # rule_base.rule_weight_list = input_rule_weight_list_by_parent[parent.antecedent_id]
        print 'rule_base.rule_weight_list: {}'.format(parent.input_rule_weight_list_by_parent)
        rule_base.rule_weight_list = parent.input_rule_weight_list_by_parent
        row_list_1 = rule_base.create_rule_base()
        rule_base.input_transformation()
        rule_base.activation_weight()
        rule_base.belief_update()
        consequence_val = rule_base.aggregate_rule()
        parent.consequence_val = consequence_val
        parent.consequent_values = consequence_val
        result.insert(count, consequence_val)
        res[parent] = consequence_val

        crisp_val = 0.0
        for i in range(len(parent.ref_val)):
            crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

        parent.input_val = str(crisp_val)

        parent.crisp_val = str(crisp_val)

        # import pdb; pdb.set_trace()

        print "Calculated consequence values for {} are: {}".format(parent.antecedent_id, consequence_val)
        print "Crisp Value: {}".format(str(crisp_val))

        print "Rule Row List: {}".format([each.__dict__ for each in row_list_1])


        # Remove the visited nodes from obj_list
        for each in visiting:
            visited.append(each)
        obj_list = [each for each in obj_list if each not in visited]

        # Make the current nodes is_input true
        current = list()
        for each in obj_list:
            if each == parent:
                current = each
                each.is_input = 'true'
                i = 0
        print "Remaining nodes for traversal: {}".format([str(each.antecedent_id) for each in obj_list])

        print "\nIn iteration {}, {} is calculated and now it's an input node. We've calculated {} subtrees so far.".format(count-1, str(current.antecedent_id), subtree)
        subtree += 1
        obj_list.sort(key=lambda x: x.is_input == "true", reverse=True)


# for each in result:
#     print each
for each in res:
    crisp_val = 0
    for i in range(len(each.ref_val)):
        crisp_val += float(each.ref_val[i]) * float(res[each][i])
        # print "res[each][i]: {}".format(res[each][i])
    print 'parent_node: {} , result: {} , crisp_val: {}'.format(each.antecedent_id, res[each],crisp_val)
