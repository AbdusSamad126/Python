cet_student = {"John", "Alice","Bob"}
jee_student = {"Alice", "Charlie","David"}
neet_student = {"Eve","Bob","Alice"}

all_student=cet_student.union(jee_student,neet_student)
print("All Student:",all_student)

intersection_student = cet_student.intersection(jee_student)
print("Students appearing for both CET and JEE:", intersection_student)

intersection_student = jee_student.intersection(neet_student)
print("Students appearing for both JEE and NEET:", intersection_student)

intersection_student = cet_student.intersection(neet_student)
print("Students appearing for both CET and NEET:", intersection_student)

cet_not_jee = cet_student.difference(jee_student)

cet_not_neet = cet_student.difference(neet_student)

union_cet=cet_not_jee.union(cet_not_neet)
print("Students appearing only for CET:",union_cet)

jee_not_cet = jee_student.difference(cet_student)

jee_not_neet = jee_student.difference(neet_student)

union_jee=jee_not_cet.union(jee_not_neet)
print("Students appearing only for JEE:",union_jee)

neet_not_cet = neet_student.difference(cet_student)

neet_not_jee = neet_student.difference(jee_student)

union_neet=neet_not_cet.union(neet_not_jee)
print("Students appearing only for NEET:",union_neet)