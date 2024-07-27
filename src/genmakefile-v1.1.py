# v1.1
# PROS:
    # still simple &
    # readable result
# CONS:
    # no double combination
    # (ex: "v", "vig", but not "vi")

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
    # 3 loops make 3 letter combinatios
    # ex:
        # vcg: v c g
    for shortcut in apps.keys():
        for different_shortcut in apps.keys():
            for yet_another_shortcut in apps.keys():

                # guard: avoid duplicates, e.g. vv: v v
                if (shortcut == different_shortcut
                    or shortcut == yet_another_shortcut
                        or different_shortcut == yet_another_shortcut):
                    continue

                content += '{0}{1}{2}: {0} {1} {2}\n'.format(
                    shortcut,
                    different_shortcut,
                    yet_another_shortcut,
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
