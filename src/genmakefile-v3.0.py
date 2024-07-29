# v3.0
# PROS:
    # readable result &
    # combinations may be exteded
# CONS:
    # exponentially slow
    # by n! / (n - r)!

from itertools import permutations


def generate_makefile(
    apps: dict[str, str],
    combination_length: int
) -> None:
    """
    Generate a text for Makefile file
    from a dictionatry of applications.

    Function complexity is: n! / (n - r)!
    Where n: amount of app shortcuts
    Where r: length of combination

    Creates a new Makefile if Makefile is not present,
    overwrites it otherwise.

    Raises no errors.
    Returns nothing.
    """
    content: str = ''

    '''top part of the file is where all the defenitions are located'''
    # ex:
        # v:
        # 	open -a "Visual Studio Code"
    content += '\n'.join(apps.values()) + '\n'

    '''bottom part of the file is where all the shortcuts are stored'''
    # '- 1' is to exclude singular keys,
    # as they are already defined
    for _ in range(combination_length - 1):
        # 'permutations' == 'all combinations, with no repeating keys'
        for combination in permutations(apps.keys(), combination_length):
            # ex:
            #   vc: v c
            #   cv: c v
            content += (
                ''.join(combination)
                + ':'
                + ' '.join(combination)
                + '\n'
            )
        combination_length -= 1

    makefile = open(file='makefile', mode='w')  # w == 'overwrite'
    makefile.write(content)
    makefile.close()


if __name__ == '__main__':
    apps: dict[str, str] = {
        'c': 'c:\n\t@open -a "Google Chrome"',
        'v': 'v:\n\t@open -a "Visual Studio Code"',
        'b': 'b:\n\t@open -a SeaLion',
        'm': 'm:\n\t@open -a Telegram',
        't': 't:\n\t@open -a Telegram',
        'g': 'g:\n\t@open -a GitAhead',
        'i': 'i:\n\t@open -a GitAhead',
    }
    combination_length: int = 4
    generate_makefile(apps, combination_length)
    print('Makefile generated successfully. File name: makefile')
