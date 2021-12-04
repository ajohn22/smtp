from socket import *

def smtp_client(port = 1025, mailserver = '127.0.0.1'):
   msg = "\r\n Hello, How are you?"
   endmsg = "\r\n.\r\n"
 # Create socket called clientSocket and establish a TCP connection with mailserver
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver,port))
   recv = clientSocket.recv(1024).decode()
   if recv[:3] != '220':
     print('220 reply not received from server.')


 # Send HELLO command and print server response.
   helloCommand = 'HELLO Alice\r\n'
   clientSocket.send(helloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send MAIL FROM command and print server response.
   mailfrom = "MAIL FROM: <ja4414@nyu.edu> \r\n"
   clientSocket.send(mailfrom.encode())
   recv2 = clientSocket.recv(1024).decode()
   if recv2[:3] != '250':
     print('250 reply not received from server.')

 # Send RCPT TO command and print server response.
   rcpto = "RCPT TO: <ajohn2m@gmail.com> \r\n"
   clientSocket.send(rcpto.encode())
   recv3 = clientSocket.recv(1024).decode()
   if recv3[:3] != '250':
     print('250 reply not received from server.')

 # Send DATA command and print server response.
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024).decode()
   if recv4[:3] != '354':
     print('354 reply not received from server.')

# Send message data.
   subject = "SUBJECT: SMTP mail client testing \r\n"
   clientSocket.send(subject.encode())
   clientSocket.send(msg.encode())
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024).decode()
   if recv5[:3] != '250':
     print('250 reply not received from server.')

   # Send QUIT command and get server response.
   quitcommand = "QUIT\r\n"
   clientSocket.send(quitcommand.encode())
   recv6 = clientSocket.recv(1024).decode()
   if recv6[:3] != '221':
     print('221 reply not received from server.')
   pass
   clientSocket.close()

if __name__ == '__main__':
  smtp_client(1025, '127.0.0.1')



