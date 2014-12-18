\* Host Instance Scheduler Problem *\
Minimize
Sum_of_Host_Instance_Scheduling_Costs: IA_Host1_Instance0 + IA_Host1_Instance1
 + IA_Host1_Instance2 + IA_Host1_Instance3
Subject To
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._0:
 1024 IA_Host0_Instance0 + 1024 IA_Host0_Instance1 + 1024 IA_Host0_Instance2
 + 1024 IA_Host0_Instance3 <= 10240
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._1:
 1024 IA_Host1_Instance0 + 1024 IA_Host1_Instance1 + 1024 IA_Host1_Instance2
 + 1024 IA_Host1_Instance3 <= 2048
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._2:
 1024 IA_Host2_Instance0 + 1024 IA_Host2_Instance1 + 1024 IA_Host2_Instance2
 + 1024 IA_Host2_Instance3 <= 5000
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._3:
 1024 IA_Host3_Instance0 + 1024 IA_Host3_Instance1 + 1024 IA_Host3_Instance2
 + 1024 IA_Host3_Instance3 <= 5000
Costraint_Name_MaxRamAllocationPerHostConstraint_No._0: IA_Host0_Instance0
 + IA_Host0_Instance1 + IA_Host0_Instance2 + IA_Host0_Instance3 <= 1
Costraint_Name_MaxRamAllocationPerHostConstraint_No._1: IA_Host1_Instance0
 + IA_Host1_Instance1 + IA_Host1_Instance2 + IA_Host1_Instance3 <= 2
Costraint_Name_MaxRamAllocationPerHostConstraint_No._2: IA_Host2_Instance0
 + IA_Host2_Instance1 + IA_Host2_Instance2 + IA_Host2_Instance3 <= 1
Costraint_Name_MaxRamAllocationPerHostConstraint_No._3: IA_Host3_Instance0
 + IA_Host3_Instance1 + IA_Host3_Instance2 + IA_Host3_Instance3 <= 1
Costraint_Name_NonTrivialSolutionConstraint_No._0: IA_Host0_Instance0
 + IA_Host1_Instance0 + IA_Host2_Instance0 + IA_Host3_Instance0 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._1: IA_Host0_Instance1
 + IA_Host1_Instance1 + IA_Host2_Instance1 + IA_Host3_Instance1 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._2: IA_Host0_Instance2
 + IA_Host1_Instance2 + IA_Host2_Instance2 + IA_Host3_Instance2 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._3: IA_Host0_Instance3
 + IA_Host1_Instance3 + IA_Host2_Instance3 + IA_Host3_Instance3 = 1
Binaries
IA_Host0_Instance0
IA_Host0_Instance1
IA_Host0_Instance2
IA_Host0_Instance3
IA_Host1_Instance0
IA_Host1_Instance1
IA_Host1_Instance2
IA_Host1_Instance3
IA_Host2_Instance0
IA_Host2_Instance1
IA_Host2_Instance2
IA_Host2_Instance3
IA_Host3_Instance0
IA_Host3_Instance1
IA_Host3_Instance2
IA_Host3_Instance3
End
