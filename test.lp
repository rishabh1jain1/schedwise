\* Host Instance Scheduler Problem *\
Minimize
Sum_of_Host_Instance_Scheduling_Costs: 0.16972972973 IA_Host1_Instance0
 + 0.16972972973 IA_Host1_Instance1 + 0.16972972973 IA_Host1_Instance2
 + IA_Host2_Instance0 + IA_Host2_Instance1 + IA_Host2_Instance2
 + IA_Host3_Instance0 + IA_Host3_Instance1 + IA_Host3_Instance2
Subject To
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._0:
 1024 IA_Host0_Instance0 + 1024 IA_Host0_Instance1 + 1024 IA_Host0_Instance2
 <= 10240
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._1:
 1024 IA_Host1_Instance0 + 1024 IA_Host1_Instance1 + 1024 IA_Host1_Instance2
 <= 1280
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._2:
 1024 IA_Host2_Instance0 + 1024 IA_Host2_Instance1 + 1024 IA_Host2_Instance2
 <= 5000
Costraint_Name_MaxDiskAllocationPerHostConstraint_No._3:
 1024 IA_Host3_Instance0 + 1024 IA_Host3_Instance1 + 1024 IA_Host3_Instance2
 <= 5000
Costraint_Name_MaxRamAllocationPerHostConstraint_No._0: 100 IA_Host0_Instance0
 + 100 IA_Host0_Instance1 + 100 IA_Host0_Instance2 <= 99
Costraint_Name_MaxRamAllocationPerHostConstraint_No._1: 100 IA_Host1_Instance0
 + 100 IA_Host1_Instance1 + 100 IA_Host1_Instance2 <= 256
Costraint_Name_MaxRamAllocationPerHostConstraint_No._2: 100 IA_Host2_Instance0
 + 100 IA_Host2_Instance1 + 100 IA_Host2_Instance2 <= 1024
Costraint_Name_MaxRamAllocationPerHostConstraint_No._3: 100 IA_Host3_Instance0
 + 100 IA_Host3_Instance1 + 100 IA_Host3_Instance2 <= 1024
Costraint_Name_NonTrivialSolutionConstraint_No._0: IA_Host0_Instance0
 + IA_Host1_Instance0 + IA_Host2_Instance0 + IA_Host3_Instance0 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._1: IA_Host0_Instance1
 + IA_Host1_Instance1 + IA_Host2_Instance1 + IA_Host3_Instance1 = 1
Costraint_Name_NonTrivialSolutionConstraint_No._2: IA_Host0_Instance2
 + IA_Host1_Instance2 + IA_Host2_Instance2 + IA_Host3_Instance2 = 1
Binaries
IA_Host0_Instance0
IA_Host0_Instance1
IA_Host0_Instance2
IA_Host1_Instance0
IA_Host1_Instance1
IA_Host1_Instance2
IA_Host2_Instance0
IA_Host2_Instance1
IA_Host2_Instance2
IA_Host3_Instance0
IA_Host3_Instance1
IA_Host3_Instance2
End
