from burp import IBurpExtender
from burp import ITab
from burp import IMessageEditorController
from javax import swing
from java import awt
from java.awt import BorderLayout;
from java.awt import GridLayout;
from java.awt import FlowLayout;
from javax.swing import JSplitPane;
from javax.swing import JTabbedPane;
from javax.swing import JButton;
from javax.swing import JFrame;
from javax.swing import JTable;
from javax.swing import JScrollPane;
from javax.swing import JPanel;
from javax.swing import JLabel;
from javax.swing import JTextArea;
from javax.swing import JTextField;
import urllib2
import json




class BurpExtender(IBurpExtender, ITab, IMessageEditorController):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.callbacks.setExtensionName("Burp Payload, Username & Password Repository")
        self.callbacks.printOutput("Welcome to my first Burp Extension. Please enjoy!")
        x = urllib2.urlopen('https://raw.githubusercontent.com/beb-commits/Project-Files/main/18000-common-usernames.txt')
        y = urllib2.urlopen('https://raw.githubusercontent.com/beb-commits/Project-Files/main/top-1575-probable-passwords.txt')
        
        frame = JFrame("Burp Payload, Username & Password Repository")
        frame.setSize(400, 900)
        frame.setLayout(BorderLayout())
        
    #UNUSED FUNCTIONS AND BUTTONS RELATING TO FUNCTIONS:
        
        # def request_usernames(event):
         # userreqFrame = JFrame("How many usernames would you like to retrieve?")
         # userreqPanel = JPanel()
         # userreqPanel.setLayout(BorderLayout())
         # userreqFrame.setSize(400, 400)
         # userreqFrame.setLayout(BorderLayout())
         # userreqPanel.setLayout(BorderLayout())
         # self.userfield = JTextField('Type the number here',15)
         # userreqPanel.add(self.userfield, BorderLayout.NORTH)
         # retUsenames = JButton('Get Usernames', actionPerformed=display_usernames)
         # userreqPanel.add(retUsenames, BorderLayout.SOUTH)
         # userreqFrame.add(userreqPanel)
         # userreqFrame.setVisible(True)
         # return
        
        # def display_usernames(event):
         # userdisFrame = JFrame("Results")
         # userdisPanel = JPanel()
         # userdisPanel.setLayout(BorderLayout())
         # userdisFrame.add(userdisPanel)
         # userdisArea = JTextArea
         # u = int(self.userfield.getText())
         # self.callbacks.printOutput(self.userfield.getText())
         # userdisArea.append(x.read()[u])
         # userdisPanel.add(userfield)
         # userdisFrame.setVisible(True)
         # return
    
        # def request_passwords(event):
         # passreqFrame = JFrame('How many passwords would you like to retrieve?')
         # passreqPanel = JPanel()
         # passreqPanel.setLayout(BorderLayout())
         # passreqFrame.add(passreqPanel, BorderLayout.NORTH)
         # self.passfield = JTextField('Type the number here',15)
         # passreqPanel.add(passfield, BorderLayout.NORTH)
         # retPasswords = JButton('Get Passwords', actionPerformed=display_passwords)
         # passreqPanel.add(retPasswords, BorderLayout.SOUTH)
         # passreqFrame.setVisible(True)
         # return
   
        # def display_passwords(event):
         # passdisFrame = JFrame('Results')
         # passdisPanel = JPanel
         # passdisPanel.setLayout(BorderLayout())
         # passdisFrame.add(passdisPanel)
         # passdisArea = JTextArea
         # p = int(self.passfield.getText())
         # passdisArea.append(x.read()[p])
         # passdisPanel.add(passfield)
         # passdisFrame.setVisible(True)
         # return
        
     # bxss = JButton("Copy")
     # bxssreq = JButton("Request Payloads")
     # bxssPanel = JPanel()
     # bxssPanel.setLayout(FlowLayout(FlowLayout.CENTER))
     # bxssPanel.add(bxssreq)
     # bxssPanel.add(bxss)
     # bsql = JButton("Copy")
     # bsqlreq = JButton("Request Payloads")
     # bsqlPanel = JPanel()
     # bsqlPanel.setLayout(FlowLayout(FlowLayout.CENTER))
     # bsqlPanel.add(bsqlreq)
     # bsqlPanel.add(bsql)
     # b2 = JButton("Copy")
     # by = JButton('Request Usernames', actionPerformed=request_usernames)
     # bPanel2 = JPanel()
     # bPanel2.setLayout(FlowLayout(FlowLayout.CENTER))
     # bPanel2.add(by)
     # bPanel2.add(b2)
     # b3 = JButton("Copy")
     # bz = JButton('Request Passwords', actionPerformed=request_passwords)
     # bPanel3 = JPanel()
     # bPanel3.setLayout(FlowLayout(FlowLayout.CENTER))
     # bPanel3.add(bz)
     # bPanel3.add(b3)
   
       #TABBED PANES:
     
        tabPane = JTabbedPane(JTabbedPane.TOP)
        tabPane2 = JTabbedPane(JTabbedPane.TOP)
        
     # scrollPane.setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)
   
   #FIRST TAB

        textPanel = JPanel()
        textPanel.setLayout(BorderLayout())
        textPanel.add(tabPane2, BorderLayout.NORTH)
        tabPane.addTab("Payloads", textPanel)
        
    #SUBTABS FOR PAYLOADS
        
        xssPanel = JPanel()
        sqlPanel = JPanel()
        tabPane2.addTab("XSS", xssPanel)
        tabPane2.addTab("SQLI", sqlPanel)
        
        
    #SUBTAB XSS
        
        xssArea = JTextArea(60, 60)
        xssPayloads = urllib2.urlopen("https://raw.githubusercontent.com/beb-commits/Project-Files/main/xss-payloads.txt")
        xssArea.append(xssPayloads.read())
        xssPanel.setLayout(BorderLayout())
        xssscrollPane = JScrollPane(xssArea)
        xssPanel.add(xssscrollPane, BorderLayout.NORTH)
      # xssPanel.add(bxssPanel, BorderLayout.SOUTH)
        
        
    #SUBTAB SQLI
        
        sqlArea = JTextArea(60, 60)
        sqlPayloads = urllib2.urlopen("https://raw.githubusercontent.com/beb-commits/Project-Files/main/sqli-payloads.txt")
        sqlArea.append(sqlPayloads.read())
        sqlPanel.setLayout(BorderLayout())
        sqlscrollPane = JScrollPane(sqlArea)
        sqlPanel.add(sqlscrollPane, BorderLayout.NORTH)
      # sqlPanel.add(bsqlPanel, BorderLayout.SOUTH)
        
        
   #SECOND TAB
          
        textArea2 = JTextArea(60, 60)
        
        textArea2.append(x.read())
        textPanel2 = JPanel()
        textPanel2.setLayout(BorderLayout()) 
        scrollPane2 = JScrollPane(textArea2)
        textPanel2.add(scrollPane2, BorderLayout.NORTH)
      # textPanel2.add(bPanel2, BorderLayout.SOUTH)
        tabPane.addTab("Usernames", textPanel2)
        
    #THIRD TAB
        
        textArea3 = JTextArea(60, 60)
        textArea3.append(y.read())
        textPanel3 = JPanel()
        textPanel3.setLayout(BorderLayout()) 
        scrollPane3 = JScrollPane(textArea3)
        textPanel3.add(scrollPane3, BorderLayout.NORTH)
      # textPanel3.add(bPanel3, BorderLayout.SOUTH)
        tabPane.addTab("Passwords", textPanel3)
        
        

        #TEXT AREA SETTINGS
        textArea2.setLineWrap(True)
        textArea3.setLineWrap(True)
        textArea2.setEditable(False)
        textArea3.setEditable(False)

   

        frame.add(tabPane)
        #frame.add(scrollPane)
        #frame.add(textArea)
        #frame.add(textAreaTwo)
        frame.setVisible(True)
    
        
        return 
        