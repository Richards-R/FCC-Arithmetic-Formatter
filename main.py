# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["912 - 68", "1 - 3801", "45 + 43", "123 + 49"],True))


# Run unit tests automatically
#main(['-vv'])
