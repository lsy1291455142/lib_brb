# @Author: mdrhri-6
# @Date:   2016-12-22T03:30:09+01:00
# @Last modified by:   mdrhri-6
# @Last modified time: 2017-02-13T15:08:06+01:00



import json

from manipulate_data_new import RuleBase
from data import Data

# Read data from file
# with open('temp_data.json') as file_data:
with open('test.json') as file_data:
# with open('2nd_order_tree.json') as file_data:
#with open('api/single_tree.json') as file_data:
# with open('sunonda_tree.json') as file_data:
# with open('agriculture_tree.json') as file_data:
    data = json.load(file_data)

obj_list = list()

# Save each node data as an object in a list
for each in data:
    obj = Data(**data[each])
    obj.name = str(each)
    obj_list.append(obj)
obj_list.sort(key=lambda x: x.is_input == "true", reverse=True)
for each in obj_list:
    print each.name

list0 = list()
list0.append(obj_list[3]) #x5
list0.append(obj_list[2]) #x4
# list1 = list()
# list1.append(obj_list[8]) #x4
parent = obj_list[5] # obj_list[7] is x6
rule_base = RuleBase(list0, parent)
rule_base.rule_weight_list = [1, 0.2, 0.8, 1, 0.4, 1, 1, 1, 1]
row_list = rule_base.create_rule_base()
rule_base.input_transformation()
rule_base.activation_weight()
rule_base.output_val_list = [[1, 0, 0], [0.3, 0.7, 0], [0, 0.3, 0.7], [0.4, 0.6, 0], [0, 1, 0], [0, 0.1, 0.9],
                        [0.1, 0.3, 0.6], [0, 0.3, 0.7], [0, 0, 1]]
rule_base.belief_update()
consequence_val = rule_base.aggregate_rule()
print consequence_val
parent.consequent_values = consequence_val
crisp_val = 0.0
for i in range(len(parent.ref_val)):
    crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

parent.input_val = str(crisp_val)
print 'parent.input_val: {}'.format(parent.input_val)

print '------------------------------------------------------'
print '------------------------------------------------------'

list0 = list()
list0.append(obj_list[2]) #x1
# list0.append(obj_list[3]) #x4
# list1 = list()
# list1.append(obj_list[8]) #x4
parent = obj_list[7] # obj_list[7] is x6
rule_base = RuleBase(list0, parent)
rule_base.rule_weight_list = [1, 1, 1]
row_list = rule_base.create_rule_base()
rule_base.input_transformation()
rule_base.activation_weight()
# rule_base.output_val_list = [[1, 0, 0], [0.3, 0.7, 0], [0, 0.3, 0.7], [0.4, 0.6, 0], [0, 1, 0], [0, 0.1, 0.9],
#                         [0.1, 0.3, 0.6], [0, 0.3, 0.7], [0, 0, 1]]
rule_base.output_val_list = [[1,0,0],[0,1,0],[0,0,1]]
rule_base.belief_update()
consequence_val = rule_base.aggregate_rule()
print consequence_val
parent.consequent_values = consequence_val
crisp_val = 0.0
for i in range(len(parent.ref_val)):
    crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

parent.input_val = str(crisp_val)
print 'parent.input_val: {}'.format(parent.input_val)

print 'obj_list[5].input_val: {}'.format(obj_list[5].input_val)
print 'obj_list[7].input_val: {}'.format(obj_list[7].input_val)

print '------------------------------------------------------'

list0 = list()
list0.append(obj_list[4]) #x1
list0.append(obj_list[9]) #x4
# list1 = list()
# list1.append(obj_list[8]) #x4
parent = obj_list[8] # obj_list[7] is x6
rule_base = RuleBase(list0, parent)
rule_base.rule_weight_list = [1, 1, 1, 1, 0.4, 1, 0.2, 1, 1]
row_list = rule_base.create_rule_base()
rule_base.input_transformation()
rule_base.activation_weight()
rule_base.output_val_list = [[1,0,0], [0.4,0.6,0], [0,1,0], [0.2,0.8,0], [0,1,0], [0,0.2,0.8], [0.1,0.3,0.6], [0,0.2,0.8], [0,0,1]]
rule_base.belief_update()
consequence_val = rule_base.aggregate_rule()
print consequence_val
parent.consequent_values = consequence_val
crisp_val = 0.0
for i in range(len(parent.ref_val)):
    crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

parent.input_val = str(crisp_val)
print 'parent.input_val: {}'.format(parent.input_val)
print 'obj_list[8].input_val: {}'.format(obj_list[8].input_val)

print '------------------------------------------------------'

list0 = list()
list0.append(obj_list[7]) #x1
list0.append(obj_list[0]) #x4
print obj_list[0].consequent_values
# list1 = list()
# list1.append(obj_list[8]) #x4
parent = obj_list[9] # obj_list[7] is x6
rule_base = RuleBase(list0, parent)
rule_base.rule_weight_list = [1,0.7,0.5,0.7,0.7,0.5,1/3,1/3,1/3]
row_list = rule_base.create_rule_base()
rule_base.input_transformation()
rule_base.activation_weight()
rule_base.output_val_list = [[1,0,0],[0.3,0.7,0],[0,0,0],[0.3,0.7,0],[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
rule_base.belief_update()
consequence_val = rule_base.aggregate_rule()
print consequence_val
parent.consequent_values = consequence_val
crisp_val = 0.0
for i in range(len(parent.ref_val)):
    crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

parent.input_val = str(crisp_val)
print 'parent.input_val: {}'.format(parent.input_val)
print 'obj_list[9].input_val: {}'.format(obj_list[9].input_val)

print '------------------------------------------------------'

list0 = list()
list0.append(obj_list[8]) #x1
obj_list[8].consequent_values = [0.17069966556200136, 0.7472616689016993, 0.08203866553629904]
list0.append(obj_list[5]) #x4
# obj_list[5].consequent_values = [0.17069966556200136, 0.7472616689016993, 0.08203866553629904]
# list1 = list()
# list1.append(obj_list[8]) #x4
parent = obj_list[6] # obj_list[7] is x6
rule_base = RuleBase(list0, parent)
rule_base.rule_weight_list = [1,0.6,1,0.6,0.6,1,1,1,1]
row_list = rule_base.create_rule_base()
rule_base.input_transformation()
print 'obj_list[8].consequent_values: {}'.format(obj_list[8].consequent_values)


rule_base.activation_weight()
rule_base.output_val_list = [[1, 0, 0], [0.2, 0.8, 0], [0.1, 0.2, 0.7], [0.2, 0.8, 0], [0, 1, 0], [0, 0.1, 0.9],[0.1, 0.2, 0.7], [0, 0.1, 0.9], [0, 0, 1]]
rule_base.belief_update()
consequence_val = rule_base.aggregate_rule()
print consequence_val
parent.consequent_values = consequence_val
crisp_val = 0.0
for i in range(len(parent.ref_val)):
    crisp_val += float(parent.ref_val[i]) * float(consequence_val[i])

parent.input_val = str(crisp_val)
print 'parent.input_val: {}'.format(parent.input_val)
import unicodedata
from fractions import Fraction
print float((1./3))
s=u'1./3'
print float(Fraction('1/3'))

print s.encode('utf-8')

