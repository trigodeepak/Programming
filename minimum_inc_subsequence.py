#Program for maximum sum increasing subsequence directly give th array as input
a = raw_input().strip().split(' ')
a= map(int,a)
n= len(a)
#actual_sequence
a_c=[i for i in range(n)]
#max_value
m_v = [i for i in a]
for i in range(n):
  for j in range(0,i):
    if a[i] > a[j]:
      m_v[i]=max(m_v[j]+a[i],m_v[i])
      a_c[i]=j
print a_c
print m_v
#answer is
print max(m_v)
