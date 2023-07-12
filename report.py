import psutil


ram = psutil.virtual_memory()
print("used", ram.used)
print("free", ram.free)
print("available", ram.available)
print("total", ram.total)
