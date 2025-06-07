v1 = 20     # velocità iniziale primo viaggiatore
v2 = 1      # velocità iniziale secondo viaggiatore

acc1 = 0    # accelerazione primo viaggiatore
acc2 = 1    # accelerazione secondo viaggiatore

dis1 = 0
dis2 = 0

for i in range(1000):
    dis1 += v1
    dis2 += v2

    v1 += acc1
    v2 += acc2

    if dis2 >= dis1:
        break

print(i)