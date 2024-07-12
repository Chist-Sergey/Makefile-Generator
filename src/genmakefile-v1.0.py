# v1.0
# PROS:
    # simple code &
    # easy readable result
# CONS:
    # limited combinations
    # (ex: "v", "vi")

def generate_makefile(apps: dict[str, str]) -> None:
    """
    generate_makefile(apps: dict[str, str]) -> None

    Generate text for Makefile file from a dictionatry of applications.
    Creates a new Makefile if Makefile is not present in a current folder.
    """
    content: str = ''

    '''top part of the file is where all the defenitions are located'''
    # ex:
        # v:
        # 	open -a "Visual Studio Code"
    for key, value in zip(apps.keys(), apps.values()):
        content += f'{key}:\n\t{value}\n'

    '''bottom part of the file is where all the shortcuts are stored'''
    # 2 loops make 2 letter combinatios
    # ex:
        # vc: v c
    for shortcut in apps.keys():
        for different_shortcut in apps.keys():

            # guard: avoid duplicates, e.g. vv: v v
            if shortcut == different_shortcut:
                continue

            content += '{0}{1}: {0} {1}\n'.format(
                shortcut, different_shortcut,
            )

    makefile = open(file='makefile', mode='w')  # w == 'overwrite'
    makefile.write(content)
    makefile.close()


if __name__ == '__main__':
    apps: dict[str, str] = {
        'c': '@open -a "Google Chrome"',
        'v': '@open -a "Visual Studio Code"',
        'b': '@open -a SeaLion',
        'm': '@open -a Telegram',
        't': '@open -a Telegram',
        'g': '@open -a GitAhead',
        'i': '@open -a GitAhead',
    }
    generate_makefile(apps)
    print('Makefile generated successfully. File name: makefile')
