\* Host Instance Scheduler Problem *\
Minimize
Sum_of_Host_Instance_Scheduling_Costs: IA_Host0_Instance0 + IA_Host0_Instance1
 + IA_Host0_Instance2 + IA_Host0_Instance3 + IA_Host0_Instance4
 + IA_Host0_Instance5 + IA_Host0_Instance6 + IA_Host0_Instance7
 + IA_Host0_Instance8 + IA_Host0_Instance9
Subject To
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._0:
 1024 IA_Host0_Instance0 + 1024 IA_Host0_Instance1 + 1024 IA_Host0_Instance2
 + 1024 IA_Host0_Instance3 + 1024 IA_Host0_Instance4 + 1024 IA_Host0_Instance5
 + 1024 IA_Host0_Instance6 + 1024 IA_Host0_Instance7 + 1024 IA_Host0_Instance8
 + 1024 IA_Host0_Instance9 <= 10240
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._1:
 1024 IA_Host1_Instance0 + 1024 IA_Host1_Instance1 + 1024 IA_Host1_Instance2
 + 1024 IA_Host1_Instance3 + 1024 IA_Host1_Instance4 + 1024 IA_Host1_Instance5
 + 1024 IA_Host1_Instance6 + 1024 IA_Host1_Instance7 + 1024 IA_Host1_Instance8
 + 1024 IA_Host1_Instance9 <= 1280
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._2:
 1024 IA_Host2_Instance0 + 1024 IA_Host2_Instance1 + 1024 IA_Host2_Instance2
 + 1024 IA_Host2_Instance3 + 1024 IA_Host2_Instance4 + 1024 IA_Host2_Instance5
 + 1024 IA_Host2_Instance6 + 1024 IA_Host2_Instance7 + 1024 IA_Host2_Instance8
 + 1024 IA_Host2_Instance9 <= 256
Costraint_Name_NonTrivialSolutionConstraint_No._0: IA_Host0_Instance0
 + IA_Host1_Instance0 + IA_Host2_Instance0 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._1: IA_Host0_Instance1
 + IA_Host1_Instance1 + IA_Host2_Instance1 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._2: IA_Host0_Instance2
 + IA_Host1_Instance2 + IA_Host2_Instance2 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._3: IA_Host0_Instance3
 + IA_Host1_Instance3 + IA_Host2_Instance3 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._4: IA_Host0_Instance4
 + IA_Host1_Instance4 + IA_Host2_Instance4 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._5: IA_Host0_Instance5
 + IA_Host1_Instance5 + IA_Host2_Instance5 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._6: IA_Host0_Instance6
 + IA_Host1_Instance6 + IA_Host2_Instance6 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._7: IA_Host0_Instance7
 + IA_Host1_Instance7 + IA_Host2_Instance7 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._8: IA_Host0_Instance8
 + IA_Host1_Instance8 + IA_Host2_Instance8 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._9: IA_Host0_Instance9
 + IA_Host1_Instance9 + IA_Host2_Instance9 = 1
Binaries
IA_Host0_Instance0
IA_Host0_Instance1
IA_Host0_Instance2
IA_Host0_Instance3
IA_Host0_Instance4
IA_Host0_Instance5
IA_Host0_Instance6
IA_Host0_Instance7
IA_Host0_Instance8
IA_Host0_Instance9
IA_Host1_Instance0
IA_Host1_Instance1
IA_Host1_Instance2
IA_Host1_Instance3
IA_Host1_Instance4
IA_Host1_Instance5
IA_Host1_Instance6
IA_Host1_Instance7
IA_Host1_Instance8
IA_Host1_Instance9
IA_Host2_Instance0
IA_Host2_Instance1
IA_Host2_Instance2
IA_Host2_Instance3
IA_Host2_Instance4
IA_Host2_Instance5
IA_Host2_Instance6
IA_Host2_Instance7
IA_Host2_Instance8
IA_Host2_Instance9
End
