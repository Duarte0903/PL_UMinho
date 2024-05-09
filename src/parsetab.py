
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '2DUP AT BEGIN CHAR COLON COMMENT_BLOCK COMMENT_LINE CONCAT CR DIVIDE DO DOT DROP DUP ELSE EMIT EXCLAMATION FUNCTION FUNCTION_CALL FUNC_BODY IF INF INFEQ KEY LEFT_PAREN LOOP MINUS MOD NEWLINE NOT NUMBER OVER PLUS REPEAT RIGHT_PAREN ROT SEMICOLON SPACE SPACES STDOUT STRING SUP SUPEQ SWAP THEN TIMES VARIABLE_ASSIGNMENT VARIABLE_DEFENITION VARIABLE_FETCH VARIABLE_PRINT WHILEprograma : comandoscomandos : comando\n                | comandos comandocomando : exp_aritmeticas\n               | exp_relacionais\n               | functions\n               | values\n               | creating_funcs\n               | variable\n               | flow_controlexp_aritmeticas : comando comando PLUS\n                       | comando comando MINUS\n                       | comando comando TIMES\n                       | comando comando DIVIDE\n                       | comando comando MODexp_relacionais : comando comando NOT\n                       | comando comando INF\n                       | comando comando SUP\n                       | comando comando INFEQ\n                       | comando comando SUPEQvalues : NUMBER\n              | STRINGflow_control : if\n                    | else\n                    | then\n                    | do\n                    | loopif : IFelse : ELSEthen : THENdo : DOloop : LOOPfunctions : stdout\n                 | dot\n                 | space\n                 | dup\n                 | comment\n                 | drop\n                 | swap\n                 | rot\n                 | over\n                 | concat\n                 | cr\n                 | emit\n                 | char\n                 | key\n                 | spaces\n                 | 2dupstdout : STDOUTdot : DOTspace : SPACEdup : comando DUPcomment : COMMENT_LINE\n               | COMMENT_BLOCKdrop : DROPswap : SWAProt : ROTover : OVERconcat : CONCATcr : CRemit : EMITchar : CHARkey : KEYspaces : SPACES2dup : 2DUPvariable : variable_definition\n                 | variable_assignment\n                 | variable_fetch\n                 | variable_printvariable_definition : VARIABLE_DEFENITIONvariable_assignment : VARIABLE_ASSIGNMENTvariable_fetch : VARIABLE_FETCHvariable_print : VARIABLE_PRINTcreating_funcs : func_criada\n                      | function\n                      | creating_funcs function\n                      | creating_funcs func_criadafunction : FUNCTION\n                | FUNCTION_CALLfunc_criada : FUNC_BODY'
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[27,27,27,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,27,27,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[28,28,28,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,28,28,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'STDOUT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[40,40,40,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,40,40,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'DOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[41,41,41,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,41,41,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'SPACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[42,42,42,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,42,42,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'COMMENT_LINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[43,43,43,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,43,43,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'COMMENT_BLOCK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[44,44,44,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,44,44,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'DROP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[45,45,45,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,45,45,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'SWAP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[46,46,46,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,46,46,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'ROT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[47,47,47,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,47,47,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'OVER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[48,48,48,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,48,48,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'CONCAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[49,49,49,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,49,49,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'CR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[50,50,50,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,50,50,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'EMIT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[51,51,51,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,51,51,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'CHAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[52,52,52,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,52,52,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'KEY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[53,53,53,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,53,53,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'SPACES':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[54,54,54,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,54,54,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'2DUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[55,55,55,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,55,55,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'FUNC_BODY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[56,56,56,-4,-5,-6,-7,56,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,56,56,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[57,57,57,-4,-5,-6,-7,57,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,57,57,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'FUNCTION_CALL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[58,58,58,-4,-5,-6,-7,58,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,58,58,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'VARIABLE_DEFENITION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[59,59,59,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,59,59,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'VARIABLE_ASSIGNMENT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[60,60,60,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,60,60,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'VARIABLE_FETCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[61,61,61,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,61,61,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'VARIABLE_PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[62,62,62,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,62,62,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[63,63,63,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,63,63,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'ELSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[64,64,64,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,64,64,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'THEN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[65,65,65,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,65,65,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'DO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[66,66,66,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,66,66,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'LOOP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[67,67,67,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,67,67,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,-3,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'DUP':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[70,-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,70,70,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'PLUS':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,73,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'MINUS':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,74,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'TIMES':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,75,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'DIVIDE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,76,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'MOD':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,77,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'NOT':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,78,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'INF':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,79,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'SUP':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,80,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'INFEQ':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,81,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'SUPEQ':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-4,-5,-6,-7,-8,-9,-10,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-21,-22,-74,-75,-66,-67,-68,-69,-23,-24,-25,-26,-27,-49,-50,-51,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-80,-78,-79,-70,-71,-72,-73,-28,-29,-30,-31,-32,82,-52,-76,-77,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'comandos':([0,],[2,]),'comando':([0,2,3,68,69,],[3,68,69,69,69,]),'exp_aritmeticas':([0,2,3,68,69,],[4,4,4,4,4,]),'exp_relacionais':([0,2,3,68,69,],[5,5,5,5,5,]),'functions':([0,2,3,68,69,],[6,6,6,6,6,]),'values':([0,2,3,68,69,],[7,7,7,7,7,]),'creating_funcs':([0,2,3,68,69,],[8,8,8,8,8,]),'variable':([0,2,3,68,69,],[9,9,9,9,9,]),'flow_control':([0,2,3,68,69,],[10,10,10,10,10,]),'stdout':([0,2,3,68,69,],[11,11,11,11,11,]),'dot':([0,2,3,68,69,],[12,12,12,12,12,]),'space':([0,2,3,68,69,],[13,13,13,13,13,]),'dup':([0,2,3,68,69,],[14,14,14,14,14,]),'comment':([0,2,3,68,69,],[15,15,15,15,15,]),'drop':([0,2,3,68,69,],[16,16,16,16,16,]),'swap':([0,2,3,68,69,],[17,17,17,17,17,]),'rot':([0,2,3,68,69,],[18,18,18,18,18,]),'over':([0,2,3,68,69,],[19,19,19,19,19,]),'concat':([0,2,3,68,69,],[20,20,20,20,20,]),'cr':([0,2,3,68,69,],[21,21,21,21,21,]),'emit':([0,2,3,68,69,],[22,22,22,22,22,]),'char':([0,2,3,68,69,],[23,23,23,23,23,]),'key':([0,2,3,68,69,],[24,24,24,24,24,]),'spaces':([0,2,3,68,69,],[25,25,25,25,25,]),'2dup':([0,2,3,68,69,],[26,26,26,26,26,]),'func_criada':([0,2,3,8,68,69,],[29,29,29,72,29,29,]),'function':([0,2,3,8,68,69,],[30,30,30,71,30,30,]),'variable_definition':([0,2,3,68,69,],[31,31,31,31,31,]),'variable_assignment':([0,2,3,68,69,],[32,32,32,32,32,]),'variable_fetch':([0,2,3,68,69,],[33,33,33,33,33,]),'variable_print':([0,2,3,68,69,],[34,34,34,34,34,]),'if':([0,2,3,68,69,],[35,35,35,35,35,]),'else':([0,2,3,68,69,],[36,36,36,36,36,]),'then':([0,2,3,68,69,],[37,37,37,37,37,]),'do':([0,2,3,68,69,],[38,38,38,38,38,]),'loop':([0,2,3,68,69,],[39,39,39,39,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> comandos','programa',1,'p_programa','forthYacc.py',14),
  ('comandos -> comando','comandos',1,'p_comandos','forthYacc.py',18),
  ('comandos -> comandos comando','comandos',2,'p_comandos','forthYacc.py',19),
  ('comando -> exp_aritmeticas','comando',1,'p_comando','forthYacc.py',28),
  ('comando -> exp_relacionais','comando',1,'p_comando','forthYacc.py',29),
  ('comando -> functions','comando',1,'p_comando','forthYacc.py',30),
  ('comando -> values','comando',1,'p_comando','forthYacc.py',31),
  ('comando -> creating_funcs','comando',1,'p_comando','forthYacc.py',32),
  ('comando -> variable','comando',1,'p_comando','forthYacc.py',33),
  ('comando -> flow_control','comando',1,'p_comando','forthYacc.py',34),
  ('exp_aritmeticas -> comando comando PLUS','exp_aritmeticas',3,'p_exp_aritmeticas','forthYacc.py',43),
  ('exp_aritmeticas -> comando comando MINUS','exp_aritmeticas',3,'p_exp_aritmeticas','forthYacc.py',44),
  ('exp_aritmeticas -> comando comando TIMES','exp_aritmeticas',3,'p_exp_aritmeticas','forthYacc.py',45),
  ('exp_aritmeticas -> comando comando DIVIDE','exp_aritmeticas',3,'p_exp_aritmeticas','forthYacc.py',46),
  ('exp_aritmeticas -> comando comando MOD','exp_aritmeticas',3,'p_exp_aritmeticas','forthYacc.py',47),
  ('exp_relacionais -> comando comando NOT','exp_relacionais',3,'p_exp_relacionais','forthYacc.py',86),
  ('exp_relacionais -> comando comando INF','exp_relacionais',3,'p_exp_relacionais','forthYacc.py',87),
  ('exp_relacionais -> comando comando SUP','exp_relacionais',3,'p_exp_relacionais','forthYacc.py',88),
  ('exp_relacionais -> comando comando INFEQ','exp_relacionais',3,'p_exp_relacionais','forthYacc.py',89),
  ('exp_relacionais -> comando comando SUPEQ','exp_relacionais',3,'p_exp_relacionais','forthYacc.py',90),
  ('values -> NUMBER','values',1,'p_values','forthYacc.py',121),
  ('values -> STRING','values',1,'p_values','forthYacc.py',122),
  ('flow_control -> if','flow_control',1,'p_flow_control','forthYacc.py',136),
  ('flow_control -> else','flow_control',1,'p_flow_control','forthYacc.py',137),
  ('flow_control -> then','flow_control',1,'p_flow_control','forthYacc.py',138),
  ('flow_control -> do','flow_control',1,'p_flow_control','forthYacc.py',139),
  ('flow_control -> loop','flow_control',1,'p_flow_control','forthYacc.py',140),
  ('if -> IF','if',1,'p_if','forthYacc.py',144),
  ('else -> ELSE','else',1,'p_else','forthYacc.py',152),
  ('then -> THEN','then',1,'p_then','forthYacc.py',161),
  ('do -> DO','do',1,'p_do','forthYacc.py',168),
  ('loop -> LOOP','loop',1,'p_loop','forthYacc.py',192),
  ('functions -> stdout','functions',1,'p_functions','forthYacc.py',203),
  ('functions -> dot','functions',1,'p_functions','forthYacc.py',204),
  ('functions -> space','functions',1,'p_functions','forthYacc.py',205),
  ('functions -> dup','functions',1,'p_functions','forthYacc.py',206),
  ('functions -> comment','functions',1,'p_functions','forthYacc.py',207),
  ('functions -> drop','functions',1,'p_functions','forthYacc.py',208),
  ('functions -> swap','functions',1,'p_functions','forthYacc.py',209),
  ('functions -> rot','functions',1,'p_functions','forthYacc.py',210),
  ('functions -> over','functions',1,'p_functions','forthYacc.py',211),
  ('functions -> concat','functions',1,'p_functions','forthYacc.py',212),
  ('functions -> cr','functions',1,'p_functions','forthYacc.py',213),
  ('functions -> emit','functions',1,'p_functions','forthYacc.py',214),
  ('functions -> char','functions',1,'p_functions','forthYacc.py',215),
  ('functions -> key','functions',1,'p_functions','forthYacc.py',216),
  ('functions -> spaces','functions',1,'p_functions','forthYacc.py',217),
  ('functions -> 2dup','functions',1,'p_functions','forthYacc.py',218),
  ('stdout -> STDOUT','stdout',1,'p_STDOUT','forthYacc.py',222),
  ('dot -> DOT','dot',1,'p_DOT','forthYacc.py',229),
  ('space -> SPACE','space',1,'p_SPACE','forthYacc.py',244),
  ('dup -> comando DUP','dup',2,'p_DUP','forthYacc.py',252),
  ('comment -> COMMENT_LINE','comment',1,'p_COMMENT','forthYacc.py',261),
  ('comment -> COMMENT_BLOCK','comment',1,'p_COMMENT','forthYacc.py',262),
  ('drop -> DROP','drop',1,'p_DROP','forthYacc.py',268),
  ('swap -> SWAP','swap',1,'p_SWAP','forthYacc.py',278),
  ('rot -> ROT','rot',1,'p_ROT','forthYacc.py',291),
  ('over -> OVER','over',1,'p_OVER','forthYacc.py',328),
  ('concat -> CONCAT','concat',1,'p_CONCAT','forthYacc.py',359),
  ('cr -> CR','cr',1,'p_CR','forthYacc.py',371),
  ('emit -> EMIT','emit',1,'p_EMIT','forthYacc.py',377),
  ('char -> CHAR','char',1,'p_CHAR','forthYacc.py',388),
  ('key -> KEY','key',1,'p_KEY','forthYacc.py',396),
  ('spaces -> SPACES','spaces',1,'p_SPACES','forthYacc.py',404),
  ('2dup -> 2DUP','2dup',1,'p_2DUP','forthYacc.py',414),
  ('variable -> variable_definition','variable',1,'p_variable','forthYacc.py',438),
  ('variable -> variable_assignment','variable',1,'p_variable','forthYacc.py',439),
  ('variable -> variable_fetch','variable',1,'p_variable','forthYacc.py',440),
  ('variable -> variable_print','variable',1,'p_variable','forthYacc.py',441),
  ('variable_definition -> VARIABLE_DEFENITION','variable_definition',1,'p_variable_definition','forthYacc.py',445),
  ('variable_assignment -> VARIABLE_ASSIGNMENT','variable_assignment',1,'p_variable_assignment','forthYacc.py',453),
  ('variable_fetch -> VARIABLE_FETCH','variable_fetch',1,'p_variable_fetch','forthYacc.py',467),
  ('variable_print -> VARIABLE_PRINT','variable_print',1,'p_variable_print','forthYacc.py',476),
  ('creating_funcs -> func_criada','creating_funcs',1,'p_creating_funcs','forthYacc.py',489),
  ('creating_funcs -> function','creating_funcs',1,'p_creating_funcs','forthYacc.py',490),
  ('creating_funcs -> creating_funcs function','creating_funcs',2,'p_creating_funcs','forthYacc.py',491),
  ('creating_funcs -> creating_funcs func_criada','creating_funcs',2,'p_creating_funcs','forthYacc.py',492),
  ('function -> FUNCTION','function',1,'p_function','forthYacc.py',496),
  ('function -> FUNCTION_CALL','function',1,'p_function','forthYacc.py',497),
  ('func_criada -> FUNC_BODY','func_criada',1,'p_func_criada','forthYacc.py',527),
]
