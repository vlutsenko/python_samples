from jnpr.junos import Device

dev = Device(host="10.101.164.44", user="root", password="root123")
dev.open()
print(dev.facts)
dev.close()
