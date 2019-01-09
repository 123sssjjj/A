def notification(self, html):
        """
        Send notification use by mail
        :param html:
        :return:
        """
        # 随机挑选一个邮箱来发送，避免由于发送量过大导致被封
        mails = get('mail', 'mails').split(',')
        mail = random.choice(mails)
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = '{0} <{1}>'.format(mail, get('mail', 'from'))
        # 支持多用户接收邮件
        msg['To'] = self.to
        msg['Cc'] = self.cc
       #"mogujie.org"
        text = MIMEText(html, 'html', 'utf-8')
        msg.attach(text)
        host = get('mail', 'host').strip()
        port = get('mail', 'port').strip()
