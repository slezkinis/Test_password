import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(
        not letter.isalpha() and not letter.isdigit() for letter in password)


def checked(password):
    score = 0
    functions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    for function_response in functions:
        if function_response(password):
            score += 2
    return score


def on_password_change(edit, new_edit_text):
    score.set_text('Рейтинг этого пароля: %s' % checked(new_edit_text))


if __name__ == '__main__':
    password = urwid.Edit('Введите пароль: ', mask='*')
    score = urwid.Text("")
    menu = urwid.Pile([password, score])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_password_change)
    urwid.MainLoop(menu).run()
