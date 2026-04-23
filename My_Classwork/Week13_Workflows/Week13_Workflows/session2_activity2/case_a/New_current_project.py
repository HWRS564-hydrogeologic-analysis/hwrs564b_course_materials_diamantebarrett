import sys
sys.path.append('/workspaces/hwrs564b_course_materials_diamantebarrett/My_Classwork/Week13_Workflows/Week13_Workflows/session2_activity2/case_a')
import my_functions

R = 1
gradient = -0.1
K = 1

Q = my_functions.darcys_flow(K,R, gradient)

print(Q)
