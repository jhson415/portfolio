def vector_size_check(*vector_variables):

    result = set([len(vector) for vector in vector_variables]) == {len(vector_variables[0])}
    return result


def vector_addition(*vector_variables):

    result = [sum(vector) for vector in zip(*vector_variables)]
    return result


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError

    result = [vector[0] - sum(vector[1:]) for vector in zip(*vector_variables)]

    return result


def scalar_vector_product(alpha, vector_variable):

    result = [alpha * vector for vector in vector_variable]

    return result


def matrix_size_check(*matrix_variables):
    same_column = [len(set(len(i) for i in j)) for j in zip(*matrix_variables)]
    same_row = [set(len(i) for i in zip(*j)) for j in matrix_variables]

    length = 0
    for j in matrix_variables:
        for i in zip(*j):
            if length == 0:
                length = len(i)
            else:
                if length != len(i):
                    return False
    length =0

    for j in zip(*matrix_variables):
        for i in j:
            if length == 0:
                length = len(i)
            else:
                if length != len(i):
                    return False

    return True


def is_matrix_equal(*matrix_variables):

    result = any([any([(i[0] - sum(i[1:])) for i in zip(*j)]) for j in zip(*matrix_variables)]) == False

    return result


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    result = [[sum(i) for i in zip(*j)] for j in zip(*matrix_variables)]
    return result


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    result = [[i[0] - sum(i[1:]) for i in zip(*j)] for j in zip(*matrix_variables)]
    return result


def matrix_transpose(matrix_variable):
    result = [[i for i in transpose] for transpose in zip(*matrix_variable)]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    result = [[alpha * i for i in j] for j in matrix_variable]

    return result


def is_product_availability_matrix(matrix_a, matrix_b):
    result = all([all([len(column_a) == len(row_b) for column_a in matrix_a]) for row_b in zip(*matrix_b)])
    return result

    for column in matrix_a:
        for row in zip(*matrix_b):
            print(len(column), len(row))


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError

    result = [[sum(a * b for a, b in zip(column_a, row_b)) for row_b in zip(*matrix_b) ] for column_a in matrix_a]
    return result
