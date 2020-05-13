import uuid

x=input('Enter Word\n')
p=str(uuid.uuid5(uuid.NAMESPACE_DNS, x))
print(p)