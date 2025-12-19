def manhattan(a, b):
    """
    İki vektör arasındaki Manhattan mesafesini hesaplar.

    Parametreler:
    - a: liste veya tuple (ör. [1, 2])
    - b: liste veya tuple (ör. [4, 6])

    Dönüş:
    - Manhattan mesafesi (int veya float)
    """

    distance = 0

    for ai, bi in zip(a, b):
        distance += abs(ai - bi)

    return distance


def euclidean(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return (dx**2 + dy**2) ** 0.5


