basicSalary = 20000

hra = 0.40 * basicSalary # 40%
da = 0.30 * basicSalary # 30%
pf = 0.20 * basicSalary # 20%
it = 0.10 * basicSalary # 10%

netSalary = basicSalary + hra + da - pf - it

print("Netsalary of {} is {}".format(basicSalary,netSalary))