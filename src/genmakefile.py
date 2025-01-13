class MakefileGenerator:
    @staticmethod
    def generate_makefile(
        permutations_DI, apps: dict[str, str], combination_length: int = None
    ) -> str:
        '''
        Generate a text for Makefile file
        from a dictionatry of shortcuts and applications.

        Function complexity is: n! / (n - r)!
        Where n: amount of apps
        Where r: combination length

        Returns a string.
        '''
        # guard blocks for invalid input
        if not apps:
            return None

        if not combination_length or combination_length < 1:
            combination_length: int = len(apps.keys())

        makefile: str = ''
    
        # result of this operation (per cycle):
        #   x:
        # 	    open -a 'Application Name'
        for key, value in zip(apps.keys(), apps.values()):
            makefile += f'{key}:\n\t@open -a "{value}"\n'

        # '- 1' is to exclude singular keys,
        # as they were already defined above
        for _ in range(combination_length - 1):

            # 'itertools.permutations' == 'all combinations, with no repeating keys'
            # result of this operation with 2 apps (per cycle):
            #   xy: x y
            # example with 2 apps after 2 cycles:
            #   xy: x y
            #   yx: y x
            for combination in permutations_DI(apps.keys(), combination_length):
                makefile += ''.join(combination) + ':' + ' '.join(combination) + '\n'

            combination_length -= 1

        return makefile


    @staticmethod
    def user_input(custom_text_responses: dict[str, str] = None) -> dict[str, str] | None:
        '''
        Asks user to enter shortcuts and applications.

        Custom text responses can be passed as a dictionatry.

        Returns a dictionatry of shortcuts and applications.
        '''
        apps: dict[str, str] = {}
        text_responses: dict[str, str] = {
            'enter_value': 'Enter your application name: ',
            'enter_key': 'Enter a shortcut for this application: ',
            'error_empty': 'Empty shortcut. Try again.',
            'error_duplicate': 'Duplicate shortcut. Try again.',
        }

        if custom_text_responses:
            text_responses = custom_text_responses

        while True:
            value = input(text_responses['enter_value'])

            if not value:
                break

            key = input(text_responses['enter_key'])

            if not key:
                print(text_responses['error_empty'])
                continue

            if key in apps:
                print(text_responses['error_duplicate'])
                continue

            apps[key] = value

        return None if not apps else apps
    

    @staticmethod
    def write_to_file(file_name: str, content: str, file_path: str = '') -> str:
        with open(file=file_path + file_name, mode='w') as makefile:
            makefile.write(content)

        return file_name


if __name__ == '__main__':
    from itertools import permutations
    apps = MakefileGenerator.user_input()
    makefile = MakefileGenerator.generate_makefile(permutations, apps)
    if makefile:
        file_name = MakefileGenerator.write_to_file('makefile', makefile)
        print(f'Makefile generated successfully. File name: {file_name}')
