def arithmetic_arranger(operations: list[str], show_results: bool = False) -> str:
    if len(operations) > 5:
        return 'Error: Too many problems.'
    separated = [operation.split() for operation in operations]
    if any([op[1] not in ('+', '-') for op in separated]):
        return "Error: Operator must be '+' or '-'."
    try:
        results = [eval(op) for op in operations]
    except SyntaxError:
        return "Error: Numbers must only contain digits."
    widths: list[int] = [max(map(len, operation)) for operation in separated]
    if any([width > 4 for width in widths]):
        return "Error: Numbers cannot be more than four digits."
    final_width = [[operation[0], f"{operation[1]} {operation[2]:>{widths[i]}}"] for i, operation in enumerate(separated)]
    widths = [max(map(len, operation)) for operation in final_width]
    formated = [[f"{x:>{widths[i]}}" for i, x in enumerate(part)] for part in zip(*final_width)]
    formated.append(["-"*i for i in widths])
    if show_results:
        formated.append([f"{result:>{widths[i]}}" for i, result in enumerate(results)])
    return "\n".join(["    ".join(part) for part in formated])
    

if __name__ == "__main__":
    print(arithmetic_arranger(["1345 + 234", "56 + 8", "1200 + 5647"], True))
