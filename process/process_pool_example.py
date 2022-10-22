from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"hi there, {name}"

if __name__ == '__main__':
    with Pool() as process_pool:
        # apply_async: async <-> apply: sync
        hi_park = process_pool.apply_async(say_hello, args=("park",))
        hi_bosung = process_pool.apply_async(say_hello, args=("bosung",))
        print(hi_park.get())
        print(hi_bosung.get())