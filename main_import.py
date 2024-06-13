from module.module_1 import xyz as swap


def test() -> None:
    return swap.engine_swap(2.6)

engineSize = 1.5
print("current engine: ", engineSize)

engineSize = test()

print("current engine: ", engineSize)
