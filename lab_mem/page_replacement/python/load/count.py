import sys

# USAGE: python count.py < trace.x.in > trace.x.counted

workload = []
for line in sys.stdin.readlines():
    page_id, mode = line.split()
    workload.append((int(page_id), mode == "w"))

counter = {}
counter_w = 0
counter_r = 0

for (k, j) in workload:
    if counter.has_key(k):
        counter[k] += 1
    else:
        counter[k] = 1
    if j:
        counter_w += 1
    else:
        counter_r += 1

print "Quantidade de frames diferentes usados:", len(counter)
print "Quantidade de leituras realizadas:", counter_r
print "Quantidade de escritas realizadas:", counter_w

for k,v in sorted(counter.items(), key=lambda p:p[1], reverse=True):
    print "%d -> %d (%.2f%%)" % (k, v, float(v)*100.0/float(len(workload)))