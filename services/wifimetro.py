from service import Service


class WifiMetro(Service):
    def send_sms(self):
        self.session.get('https://go.zazumedia.ru/auth/wait/sms/' + self.formatted_phone + '?from_reg=1')
