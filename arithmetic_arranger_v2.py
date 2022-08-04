def arithmetic_arranger(operations: list[str], show_results: bool = False) -> str:
    if len(operations) > 5: return 'Error: Too many problems.'
    chunks = ([], [], [], [])
    for operation in operations:
        first, op, second = operation.split()
        if op not in ("+", "-"): return "Error: Operator must be '+' or '-'."
        if not (first.isnumeric() and second.isnumeric()): return "Error: Numbers must only contain digits."
        width = max(len(first), len(second))
        if width > 4: return "Error: Numbers cannot be more than four digits."
        chunks[0].append(f"{first:>{width + 2}}")
        chunks[1].append(f"{op} {second:>{width}}")
        chunks[2].append("-"*(width + 2))
        if show_results: chunks[3].append(f"{int(first) + int(op + second):>{width + 2}}")
    return "\n".join(["    ".join(chunk) for chunk in chunks if chunk])
print(arithmetic_arranger(["1345 + 234", "56 + 8", "1200 + 5647"], True))