# psudo recursion
import abc
from typing import Type, NoReturn


class email_sender():
    def __init__(self):
        pass

    def send_email(self, email_addr: str, content: str) -> NoReturn:
        print(f'email sent to {email_addr} : {content}')


class logger():
    def __init__(self):
        self.identity = 'logger'

    def log(self, logstr: str) -> str:
        print(logstr)


class abstract_notify(abc.ABC):

    def notify(self, notification: str) -> NoReturn:
        pass

    def notifier(self) -> str:
        pass


class minimal_notifier(abstract_notify):

    def __init__(self):
        self._logger = logger()

    def notify(self, notification: str) -> NoReturn:
        self._logger.log(notification)

    def notifier(self) -> str:
        return f'{self._logger.identity} notification'


class email_notifier(abstract_notify):
    def __init__(self, notifier: Type[minimal_notifier]):
        self._base_notifier = notifier
        self._emailer = email_sender()

    def notify(self, notification: str) -> NoReturn:
        self._emailer.send_email('me@me.me', notification)
        self._base_notifier.notify(notification)

    def notifier(self) -> str:
        return f'email notification , {self._base_notifier.notifier()}'


class sound_notifier(abstract_notify):
    def __init__(self, notifier: Type[minimal_notifier]):
        self._base_notifier = notifier

    def notify(self, notification: str) -> NoReturn:
        print('$$$ PLAY SOUND $$$')
        self._base_notifier.notify(notification)

    def notifier(self) -> str:
        return f'sound notification , {self._base_notifier.notifier()}'


class visual_notifier(abstract_notify):
    def __init__(self, notifier: Type[minimal_notifier]):
        self._base_notifier = notifier

    def notify(self, notification: str) -> NoReturn:
        print(f'********************DISPLAY NOTIFY : {notification}************************')
        self._base_notifier.notify(notification)

    def notifier(self) -> str:
        return f'display notification , {self._base_notifier.notifier()}'


if __name__ == "__main__":
    basic_notification = minimal_notifier()
    withsound = sound_notifier(basic_notification)
    withemail = email_notifier(withsound)

    withemail.notify('TEST')

    print(withemail.notifier())
    print('')
    print('******************* restart ***************')
    print('')
    min_notify = minimal_notifier()
    # play sound twice
    decorated_notify = sound_notifier(min_notify)
    decorated_notify = sound_notifier(decorated_notify)
    # display
    decorated_notify = visual_notifier(decorated_notify)
    #   email
    decorated_notify = email_notifier(decorated_notify)

    decorated_notify.notify('FOR REAL')

    print(decorated_notify.notifier())
