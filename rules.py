class Rules(object):
    def __init__(self):
        self.rule_weight = 1
        # self.rule_weight_list = [1, 0.7,1 ,0.7,0.7,1,1,1,1]
        # self.rule_weight_list = [1, 1, 1, 1, 0.4, 1, 0.2, 1, 1]
        # [00,01,02,10,11,12,20,21,22]->[HH,HM,HL,MH,MM,ML,LH,LM,LL]
        # self.rule_weight_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        # self.rule_weight_list = []
        # self.antecedent_ref_val = []
        # self.antecedent_ref_title = []
        # self.antecedent_2 = ""
        # self.antecedent_2_ref_title = ""
        self.parent = ""
        self.combinations = []
        self.consequence_val = []
        self.matching_degree = None
        self.activation_weight = None

    # def sum_of_activation_weight(self):
    #     return sum(self.rule_weight * self.matching_degree)
