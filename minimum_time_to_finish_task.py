#minimum time to finish tasks if we cannot skip 2 consecutive tasks
a = [10, 5, 2, 4, 8, 6, 7, 10]
min_task = 0
def min_task_value(a,i):
    incl = a[0]
    excl = 0
    for i in xrange(1,len(a)):
        incl_new = a[i]+min(excl,incl)
        excl = incl
        incl = incl_new
    return min(incl,excl)
min_task = min_task_value(a,0)
print min_task

