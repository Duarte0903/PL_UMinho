
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AT BEGIN COLON CONCAT DIVIDE DO DOT DROP DUP ELSE EXCLAMATION EXIT IF INF INFEQ LEFT_PAREN LOOP MINUS MOD NOT NUMBER OVER PLUS REPEAT RIGHT_PAREN ROT SEMICOLON STRING SUP SUPEQ SWAP THEN TIMES VARIABLE WHILE reserved_wordprogram : statementsstatements : statement\n                  | statements statementstatement : expression\n                 | flow_controlexpression : NUMBER\n                  | STRING\n                  | VARIABLE\n                  | special_expression\n                  | reserved_wordexpression : DOTexpression : expression expression arithmetic_oparithmetic_op : PLUS\n                     | MINUS\n                     | TIMES\n                     | DIVIDE\n                     | MODexpression : expression expression relational_oprelational_op : NOT\n                     | INF\n                     | SUP\n                     | INFEQ\n                     | SUPEQexpression : expression expression string_opstring_op : CONCATspecial_expression : EXCLAMATION\n                           | AT\n                           | COLON\n                           | SEMICOLON\n                           | LEFT_PAREN\n                           | RIGHT_PARENflow_control : if_statement\n                    | else_statement\n                    | while_loop\n                    | repeat_loop\n                    | exit_statement\n                    | drop_statement\n                    | dup_statement\n                    | swap_statement\n                    | rot_statement\n                    | over_statementif_statement : expression IF statements THENelse_statement : ELSEwhile_loop : WHILE expression DO statements LOOPrepeat_loop : BEGIN statements WHILE expression REPEATexit_statement : EXITdrop_statement : DROPdup_statement : DUPswap_statement : SWAProt_statement : ROTover_statement : OVER'
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[6,6,-2,6,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,6,6,-46,-47,-48,-49,-50,-51,-3,6,6,6,6,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,6,6,6,-42,6,6,-44,-45,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[7,7,-2,7,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,7,7,-46,-47,-48,-49,-50,-51,-3,7,7,7,7,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,7,7,7,-42,7,7,-44,-45,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[8,8,-2,8,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,8,8,-46,-47,-48,-49,-50,-51,-3,8,8,8,8,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,8,8,8,-42,8,8,-44,-45,]),'reserved_word':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[10,10,-2,10,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,10,10,-46,-47,-48,-49,-50,-51,-3,10,10,10,10,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,10,10,10,-42,10,10,-44,-45,]),'DOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[11,11,-2,11,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,11,11,-46,-47,-48,-49,-50,-51,-3,11,11,11,11,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,11,11,11,-42,11,11,-44,-45,]),'EXCLAMATION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[22,22,-2,22,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,22,22,-46,-47,-48,-49,-50,-51,-3,22,22,22,22,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,22,22,22,-42,22,22,-44,-45,]),'AT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[23,23,-2,23,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,23,23,-46,-47,-48,-49,-50,-51,-3,23,23,23,23,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,23,23,23,-42,23,23,-44,-45,]),'COLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[24,24,-2,24,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,24,24,-46,-47,-48,-49,-50,-51,-3,24,24,24,24,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,24,24,24,-42,24,24,-44,-45,]),'SEMICOLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[25,25,-2,25,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,25,25,-46,-47,-48,-49,-50,-51,-3,25,25,25,25,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,25,25,25,-42,25,25,-44,-45,]),'LEFT_PAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[26,26,-2,26,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,26,26,-46,-47,-48,-49,-50,-51,-3,26,26,26,26,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,26,26,26,-42,26,26,-44,-45,]),'RIGHT_PAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[27,27,-2,27,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,27,27,-46,-47,-48,-49,-50,-51,-3,27,27,27,27,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,27,27,27,-42,27,27,-44,-45,]),'ELSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[28,28,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,28,-46,-47,-48,-49,-50,-51,-3,28,28,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,28,28,-42,28,-44,-45,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[29,29,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,29,-46,-47,-48,-49,-50,-51,-3,29,58,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,29,29,-42,29,-44,-45,]),'BEGIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[30,30,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,30,-46,-47,-48,-49,-50,-51,-3,30,30,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,30,30,-42,30,-44,-45,]),'EXIT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[31,31,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,31,-46,-47,-48,-49,-50,-51,-3,31,31,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,31,31,-42,31,-44,-45,]),'DROP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[32,32,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,32,-46,-47,-48,-49,-50,-51,-3,32,32,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,32,32,-42,32,-44,-45,]),'DUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[33,33,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,33,-46,-47,-48,-49,-50,-51,-3,33,33,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,33,33,-42,33,-44,-45,]),'SWAP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[34,34,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,34,-46,-47,-48,-49,-50,-51,-3,34,34,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,34,34,-42,34,-44,-45,]),'ROT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[35,35,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,35,-46,-47,-48,-49,-50,-51,-3,35,35,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,35,35,-42,35,-44,-45,]),'OVER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,],[36,36,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,36,-46,-47,-48,-49,-50,-51,-3,36,36,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,36,36,-42,36,-44,-45,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,59,62,63,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,-46,-47,-48,-49,-50,-51,-3,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,-42,-44,-45,]),'THEN':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,62,63,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,-46,-47,-48,-49,-50,-51,-3,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,59,-42,-44,-45,]),'LOOP':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,59,60,62,63,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,-27,-28,-29,-30,-31,-43,-46,-47,-48,-49,-50,-51,-3,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,-42,62,-44,-45,]),'IF':([4,6,7,8,9,10,11,22,23,24,25,26,27,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[39,-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'PLUS':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,45,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'MINUS':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,46,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'TIMES':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,47,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'DIVIDE':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,48,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'MOD':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,49,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'NOT':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,50,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'INF':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,51,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'SUP':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,52,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'INFEQ':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,53,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'SUPEQ':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,54,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'CONCAT':([6,7,8,9,10,11,22,23,24,25,26,27,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,55,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,]),'DO':([6,7,8,9,10,11,22,23,24,25,26,27,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,61,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,57,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,57,]),'REPEAT':([6,7,8,9,10,11,22,23,24,25,26,27,42,43,44,45,46,47,48,49,50,51,52,53,54,55,61,],[-6,-7,-8,-9,-10,-11,-26,-27,-28,-29,-30,-31,-12,-18,-24,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-25,63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,30,39,57,],[2,41,56,60,]),'statement':([0,2,30,39,41,56,57,60,],[3,37,3,3,37,37,3,37,]),'expression':([0,2,4,29,30,38,39,40,41,56,57,58,60,61,],[4,4,38,40,4,38,4,38,4,4,4,61,4,38,]),'flow_control':([0,2,30,39,41,56,57,60,],[5,5,5,5,5,5,5,5,]),'special_expression':([0,2,4,29,30,38,39,40,41,56,57,58,60,61,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'if_statement':([0,2,30,39,41,56,57,60,],[12,12,12,12,12,12,12,12,]),'else_statement':([0,2,30,39,41,56,57,60,],[13,13,13,13,13,13,13,13,]),'while_loop':([0,2,30,39,41,56,57,60,],[14,14,14,14,14,14,14,14,]),'repeat_loop':([0,2,30,39,41,56,57,60,],[15,15,15,15,15,15,15,15,]),'exit_statement':([0,2,30,39,41,56,57,60,],[16,16,16,16,16,16,16,16,]),'drop_statement':([0,2,30,39,41,56,57,60,],[17,17,17,17,17,17,17,17,]),'dup_statement':([0,2,30,39,41,56,57,60,],[18,18,18,18,18,18,18,18,]),'swap_statement':([0,2,30,39,41,56,57,60,],[19,19,19,19,19,19,19,19,]),'rot_statement':([0,2,30,39,41,56,57,60,],[20,20,20,20,20,20,20,20,]),'over_statement':([0,2,30,39,41,56,57,60,],[21,21,21,21,21,21,21,21,]),'arithmetic_op':([38,],[42,]),'relational_op':([38,],[43,]),'string_op':([38,],[44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','forthYacc.py',11),
  ('statements -> statement','statements',1,'p_statements','forthYacc.py',16),
  ('statements -> statements statement','statements',2,'p_statements','forthYacc.py',17),
  ('statement -> expression','statement',1,'p_statement','forthYacc.py',27),
  ('statement -> flow_control','statement',1,'p_statement','forthYacc.py',28),
  ('expression -> NUMBER','expression',1,'p_expression','forthYacc.py',34),
  ('expression -> STRING','expression',1,'p_expression','forthYacc.py',35),
  ('expression -> VARIABLE','expression',1,'p_expression','forthYacc.py',36),
  ('expression -> special_expression','expression',1,'p_expression','forthYacc.py',37),
  ('expression -> reserved_word','expression',1,'p_expression','forthYacc.py',38),
  ('expression -> DOT','expression',1,'p_dot','forthYacc.py',57),
  ('expression -> expression expression arithmetic_op','expression',3,'p_expression_arithmetic','forthYacc.py',70),
  ('arithmetic_op -> PLUS','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',109),
  ('arithmetic_op -> MINUS','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',110),
  ('arithmetic_op -> TIMES','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',111),
  ('arithmetic_op -> DIVIDE','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',112),
  ('arithmetic_op -> MOD','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',113),
  ('expression -> expression expression relational_op','expression',3,'p_expression_relational','forthYacc.py',118),
  ('relational_op -> NOT','relational_op',1,'p_relational_op','forthYacc.py',150),
  ('relational_op -> INF','relational_op',1,'p_relational_op','forthYacc.py',151),
  ('relational_op -> SUP','relational_op',1,'p_relational_op','forthYacc.py',152),
  ('relational_op -> INFEQ','relational_op',1,'p_relational_op','forthYacc.py',153),
  ('relational_op -> SUPEQ','relational_op',1,'p_relational_op','forthYacc.py',154),
  ('expression -> expression expression string_op','expression',3,'p_string_operations','forthYacc.py',159),
  ('string_op -> CONCAT','string_op',1,'p_string_op','forthYacc.py',175),
  ('special_expression -> EXCLAMATION','special_expression',1,'p_special_expression','forthYacc.py',183),
  ('special_expression -> AT','special_expression',1,'p_special_expression','forthYacc.py',184),
  ('special_expression -> COLON','special_expression',1,'p_special_expression','forthYacc.py',185),
  ('special_expression -> SEMICOLON','special_expression',1,'p_special_expression','forthYacc.py',186),
  ('special_expression -> LEFT_PAREN','special_expression',1,'p_special_expression','forthYacc.py',187),
  ('special_expression -> RIGHT_PAREN','special_expression',1,'p_special_expression','forthYacc.py',188),
  ('flow_control -> if_statement','flow_control',1,'p_flow_control','forthYacc.py',193),
  ('flow_control -> else_statement','flow_control',1,'p_flow_control','forthYacc.py',194),
  ('flow_control -> while_loop','flow_control',1,'p_flow_control','forthYacc.py',195),
  ('flow_control -> repeat_loop','flow_control',1,'p_flow_control','forthYacc.py',196),
  ('flow_control -> exit_statement','flow_control',1,'p_flow_control','forthYacc.py',197),
  ('flow_control -> drop_statement','flow_control',1,'p_flow_control','forthYacc.py',198),
  ('flow_control -> dup_statement','flow_control',1,'p_flow_control','forthYacc.py',199),
  ('flow_control -> swap_statement','flow_control',1,'p_flow_control','forthYacc.py',200),
  ('flow_control -> rot_statement','flow_control',1,'p_flow_control','forthYacc.py',201),
  ('flow_control -> over_statement','flow_control',1,'p_flow_control','forthYacc.py',202),
  ('if_statement -> expression IF statements THEN','if_statement',4,'p_if_statement','forthYacc.py',208),
  ('else_statement -> ELSE','else_statement',1,'p_else_statement','forthYacc.py',212),
  ('while_loop -> WHILE expression DO statements LOOP','while_loop',5,'p_while_loop','forthYacc.py',216),
  ('repeat_loop -> BEGIN statements WHILE expression REPEAT','repeat_loop',5,'p_repeat_loop','forthYacc.py',220),
  ('exit_statement -> EXIT','exit_statement',1,'p_exit_statement','forthYacc.py',224),
  ('drop_statement -> DROP','drop_statement',1,'p_drop_statement','forthYacc.py',228),
  ('dup_statement -> DUP','dup_statement',1,'p_dup_statement','forthYacc.py',234),
  ('swap_statement -> SWAP','swap_statement',1,'p_swap_statement','forthYacc.py',252),
  ('rot_statement -> ROT','rot_statement',1,'p_rot_statement','forthYacc.py',265),
  ('over_statement -> OVER','over_statement',1,'p_over_statement','forthYacc.py',299),
]
