import DNS, smtplib, socket, time
from interruptingcow import timeout

def send_email(sender_email, password, recip_mail, subject, text):
    gmail_user = sender_email
    gmail_pwd = password
    FROM = sender_email
    TO = [recip_mail] #must be a list
    SUBJECT = subject
    TEXT = text
    
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


def email_generator(first, last, email_end):
    firsts = []
    lasts = []
    emails = []
    separators = ['','.','_']

    for i in range(1, len(first)+1):
        firsts.append(first[:i])
    for i in range(1, len(last)+1):
        lasts.append(last[:i+1])


    # generate emails
    for f in firsts:
        for sep in separators:
            emails.append(f + sep + last + email_end)
            emails.append(last + sep + f + email_end)

    for l in lasts:
        for sep in separators:
                emails.append(first + sep + l + email_end)
                emails.append(l + sep + first + email_end)

    emails.append(first + email_end)
    emails.append(last + email_end)

    return emails


def checkmail(mail, attempts=0):
        DNS.DiscoverNameServers()
        hostname = mail[mail.find('@')+1:]
        try:
            mx_hosts = DNS.mxlookup(hostname)
        except:
            print 'failed email', mail
            return False
        # except:
        #     if attempts > 5:
        #         print 'Timeout'
        #     else:
        #         print 'failed email', mail
        #         attempts += 1
        #         time.sleep(5)
        #         checkmail(mail, attempts)
        failed_mx = True
        for mx in mx_hosts:
                smtp = smtplib.SMTP()
                try:
                        smtp.connect(mx[1])
                        failed_mx = False
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((mx[1], 25))
                        s.recv(1024)
                        s.send("HELO %s\n"%(mx[1]))
                        s.recv(1024)
                        s.send("MAIL FROM:< test@test.com>\n")
                        s.recv(1024)
                        s.send("RCPT TO:<%s>\n"%(mail))
                        result = s.recv(1024)
                        if result.find('Recipient address rejected') > 0:
                                failed_mx = True
                        elif result.find('does not exist') > 0:
                                failed_mx = True
                        else:
                                failed_mx = False
                        s.send("QUIT\n")
                        break
                except smtplib.SMTPConnectError:
                        continue

        if not failed_mx:
                return True
        return False

def gen_correct_emails(first, last, email_end):
    correct_emails = []
    emails = email_generator(first, last, email_end)
    for em in emails:
        try:
            if checkmail(em):
                print em
                correct_emails.append(em)
        except:
            continue
    return correct_emails

if __name__ == '__main__':
    pass