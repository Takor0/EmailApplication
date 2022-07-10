
class ConsoleOutputPrinter:
    INDENTATION = '    '

    def print_result(self, result, args):
        if args.is_incorrect_emails_option_selected:
            self.__print_incorrect_emails(result)
        if args.is_search_by_text_option_selected:
            self.__print_searched_emails(result, args)
        if args.is_group_by_domain_option_selected:
            self.__print_grouped_by_domain_emails(result)
        if args.is_find_email_not_in_logs_option_selected:
            self.__print_emails_not_in_logs(result)

    def __print_incorrect_emails(self, result):
        quantity = len(result)
        print(f'Invalid emails ({quantity}):')
        for email in result:
            print(self.INDENTATION + email)

    def __print_searched_emails(self, result, args):
        text = args.text_to_search
        quantity = len(result)
        print(f"Found emails with '{text}' in email ({quantity}): ")
        for email in result:
            print(self.INDENTATION + email)

    def __print_grouped_by_domain_emails(self, result):
        for domain in result:
            quantity = len(result[domain])
            print(f"Domain {domain} ({quantity})")
            for email in result[domain]:
                print(self.INDENTATION + email)

    def __print_emails_not_in_logs(self, result):
        quantity = len(result)
        print(f'Emails not sent ({quantity}):')
        for email in result:
            print(self.INDENTATION + email)

    def print_error(self, error):
        print(f"Error: {error}")
