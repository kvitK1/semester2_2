from node import TwoWayNode
head = None
previous = None

a = 22
results = []
while a >= 1:
    b = a%2
    print(f"b:{b}")
    print(f"a:{a}")
    results.insert(0, b)
    a //= 2
print(results)

for i in results:
    head = TwoWayNode(i, previous, head)
    previous = head

nums = 0
for i, val in enumerate(results):
    k= len(results)-i-1
    new_val = val*(2**k)
    nums += new_val

# while head is not None:
#     print(head.data)
#     head = head.next