import gc


print("GC ENABLE:", gc.isenabled())
print("GC collect():", gc.collect())
a = 123
print("GC collect():", gc.collect())

# print("GC get_objects():", gc.get_objects())
print("GC get_stats():", gc.get_stats())

print("gc.garbage", gc.garbage)
print("gc.callbacks:", gc.callbacks)
# gc.set_debug(gc.DEBUG_SAVEALL)
# gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_STATS)


class A:
	pass

while True:
	a += 1
	A = {
		'1': a
	}
	del A['1']
