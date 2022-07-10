import argparse
from src.Error.InputError import TextIsTooLongError


class InputValidator:
    def validate(self):
        parser = argparse.ArgumentParser(description='Process emails')
        parser.add_argument('--incorrect-emails', '-ic', action='store_true',
                            dest='is_incorrect_emails_option_selected', default=False,
                            help='Print the number of invalid emails, then one invalid email per line.')
        parser.add_argument('--search', '-s', type=str, dest='text_to_search',
                            help='The Program should take a string argument and print the number of found emails, '
                                 'then one found email per line.')
        parser.add_argument('--group-by-domain', '-gbd', action='store_true',
                            dest='is_group_by_domain_option_selected', default=False,
                            help='Group emails by one domain and order domains and emails alphabetically')
        parser.add_argument('--find-emails-not-in-logs', '-feil', type=str, dest='path_to_log_file',
                            help='Find emails that are not in the provided logs file. Print the numbers of found '
                                 'emails, then one found email per line sorted alphabetically.')

        args = parser.parse_args()

        if args.text_to_search is not None and len(args.text_to_search) > 320:
            raise TextIsTooLongError("Given text to search is too long, max length is 320")

        args.is_search_by_text_option_selected = args.text_to_search is not None
        args.is_find_email_not_in_logs_option_selected = args.path_to_log_file is not None

        return args
