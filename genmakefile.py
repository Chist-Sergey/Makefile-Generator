# Scroll to the bottom to edit the shortcuts

from itertools import permutations


def generate_makefile(
    apps: dict[str, str],
    combination_length: int
) -> str:
    """
    Generate a text for Makefile file
    from a dictionatry of applications.

    Function complexity is: n! / (n - r)!
    Where n: amount of app shortcuts
    Where r: length of combination

    Creates a new Makefile if Makefile is not present,
    overwrites it otherwise.

    Raises no errors.
    Returns a string with makefile contents.
    """
    content: str = ''

    '''top part of the file is where all the defenitions are located'''
    # adding these spectial chars to alleviate
    # the burden of writing them from the user
    for key, value in apps.items():
        apps[key] = key + ':\n\t@' + value

    # example:
        # v:
        # 	open -a "Visual Studio Code"
    content += '\n'.join(apps.values()) + '\n'

    '''bottom part of the file is where all the shortcuts are stored'''
    # '- 1' is to exclude singular keys,
    # as they are already defined
    for _ in range(combination_length - 1):
        # 'permutations' == 'all combinations with no repeating keys'
        for combination in permutations(apps.keys(), combination_length):
            # example:
                # vc: v c
                # cv: c v
            content += (
                ''.join(combination)
                + ':'
                + ' '.join(combination)
                + '\n'
            )
        combination_length -= 1

    return content


if __name__ == '__main__':
    # edit here
    combination_length: int = 2
    apps: dict[str, str] = {
    # example:
        # 'shortcut': 'application',
        # 'c': 'open -a "Google Chrome"',
        # 'v': 'open -a "Visual Studio Code"',
    }

    result: str = generate_makefile(apps, combination_length)

    makefile = open(file='makefile', mode='w')  # w == 'overwrite'
    makefile.write(result)
    makefile.close()

    print('Makefile generated successfully. File name: makefile')
