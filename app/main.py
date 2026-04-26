import sentry_sdk

sentry_sdk.init(
    dsn="https://0e080af9745c9c275c6a1847007e4e5c@o4511287037657088.ingest.de.sentry.io/4511287053582416",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


def find_max(numbers):
    """
    Повертає максимальне число зі списку.

    >>> find_max([1, 2, 3])
    3
    >>> find_max([-5, -1, -10])
    -1
    >>> find_max([7])
    7
    """
    if not numbers:
        raise ValueError("Список порожній!")

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


def main():
    try:
        user_input = input("Введіть числа через пробіл: ")
        numbers = list(map(int, user_input.split()))

        result = find_max(numbers)
        print(f"Максимальне число: {result}")

    except ValueError as e:
        sentry_sdk.capture_exception(e)
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
