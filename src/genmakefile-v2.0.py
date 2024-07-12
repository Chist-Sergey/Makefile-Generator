# v2.0
# PROS:
    # all combinations are included
    # (ex: "v", "vi", "vig")
# CONS:
    # the result is hard to read

def generate_makefile(apps: dict[str, str]) -> None:
    """
    generate_makefile(apps: dict[str, str]) -> None

    Generate text for Makefile file from a dictionatry of applications.
    Creates a new Makefile if Makefile is not present in a current folder.
    """
    content: str = ''

    # 1st level
    # ex:
        # v:
        # 	open -a "Visual Studio Code"
    for shortcut in apps.keys():
        # 2nd level
        # ex:
            # vg: v g
        for different_shortcut in apps.keys():
            # 3rd level
            # ex:
                # vgb: v g b
            for yet_another_shortcut in apps.keys():
                # guard: repeated keys
                # ex:
                    # sigular:
                        # vvv: v v v
                        # ggg: g g g
                    # doubles:
                        # vvg: v v g
                        # ggv: g g v
                if (shortcut == different_shortcut
                    or shortcut == yet_another_shortcut
                        or different_shortcut == yet_another_shortcut):
                    continue

                content += '{0}{1}{2}: {0} {1} {2}\n'.format(
                    shortcut,
                    different_shortcut,
                    yet_another_shortcut,
                )

            # guard: repeated keys
            # ex:
                # vv: v v
                # gg: g g
            if shortcut == different_shortcut:
                continue

            content += '{0}{1}: {0} {1}\n'.format(
                shortcut, different_shortcut,
            )

        content += '{0}:\n\t{1}\n'.format(
            shortcut, apps[shortcut],
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
