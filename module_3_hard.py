def calculate_structure_sum(args):
    calc_sum = 0
    if isinstance(args, int):
        calc_sum += args
    elif isinstance(args, str):
        calc_sum += len(args)
    elif isinstance(args, list):
        for i in args:
            calc_sum += calculate_structure_sum(i)
    elif isinstance(args, tuple):
        for i in args:
            calc_sum += calculate_structure_sum(i)
    elif isinstance(args, set):
        for i in args:
            calc_sum += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for i, j in args.items():
            calc_sum += calculate_structure_sum(i)
            calc_sum += calculate_structure_sum(j)
    return(calc_sum)

data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]




result = calculate_structure_sum(data_structure)
print(result)
