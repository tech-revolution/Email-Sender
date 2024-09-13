import json
import os
import re
from threading import active_count
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session, url_for, flash
from werkzeug.utils import redirect, secure_filename
from flask_mail import Mail, Message
from datetime import date, timedelta
import csv


#to load json file
# with open('config.json', 'r') as var:
#     para = json.load(var) ["para"]


app = Flask(__name__)

# gmail_user = "odootest90@gmail.com"
# gmail_password = "Odoo12345678"
app.secret_key = "haideraamir"
app.config['MAIL_SERVER']='mail.privateemail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = "smmarketing@bitcointutorial.net"
# app.config['MAIL_PASSWORD'] = "Vision@2020"
app.config['MAIL_USERNAME'] = "nima-maximud@bitcointutorial.net"
app.config['MAIL_PASSWORD'] = "Nima@@@2022"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



#database connection with xampp
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/test_db"
# db = SQLAlchemy(app)


# class User(db.Model):
#     # Sno, Name, Age, Email, Address, Post, Phone, Photo
#     Sno = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String(100), unique=False, nullable=False)
#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.email}"

@app.route("/")
def sendendmail():
   
   
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        file_name = request.form['file_name']
        with open (f'{file_name}.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for i, line in enumerate(csv_reader, start=1):
                print(f"{i} = Message Sent Successfully to .....! {line[0]}" )
                msg = Message('Get 20% off to promote social Accounts!', sender = "nima-maximud@bitcointutorial.net" , recipients = [f"{line[0]}"])
                # msg.html = "<b> Hey "+ line[0] +" </b><br><p>Dear User!</p><br><p>Tesing Emails. Thanks for your subscription. </p>"     
                msg.html = "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'> <html xmlns='http://www.w3.org/1999/xhtml'><head> <meta content='text/html; charset=utf-8' http-equiv='Content-Type'/><meta content='width=device-width, initial-scale=1' name='viewport' /><title></title><style type='text/css'> @media only screen and (max-width:480px) { body, table, td, p, a, li, blockquote { -webkit-text-size-adjust: none !important} body { width: 100% !important;min-width: 100% !important}#bodyCell {padding: 10px !important}table.kmMobileHide {display: none !important}table.kmDesktopOnly, td.kmDesktopOnly, th.kmDesktopOnly,tr.kmDesktopOnly,td.kmDesktopWrapHeaderMobileNone {display: none !important} table.kmMobileOnly {display: table !important}tr.kmMobileOnly { display: table-row !important} td.kmMobileOnly,td.kmDesktopWrapHeader,th.kmMobileOnly { display: table-cell !important } tr.kmMobileNoAlign, table.kmMobileNoAlign { float: none !important; text-align: initial !important; vertical-align: middle !important;table-layout: fixed !important }tr.kmMobileCenterAlign {float: none !important; text-align: center !important; vertical-align: middle !important; table-layout: fixed !important} td.kmButtonCollection { padding-left: 9px !important; padding-right: 9px !important; padding-top: 9px !important; padding-bottom: 9px !important } td.kmMobileHeaderStackDesktopNone,img.kmMobileHeaderStackDesktopNone, td.kmMobileHeaderStack { display: block !important; margin-left: auto !important; margin-right: auto !important; padding-bottom: 9px !important; padding-right: 0 !important; padding-left: 0 !important } td.kmMobileWrapHeader, td.kmMobileWrapHeaderDesktopNone { display: inline-block !important }td.kmMobileHeaderSpacing { padding-right: 10px !important}td.kmMobileHeaderNoSpacing { padding-right: 0 !important }table.kmDesktopAutoWidth { width: inherit !important}table.kmMobileAutoWidth { width: 100% !important } table.kmTextContentContainer { width: 100% !important }table.kmBoxedTextContentContainer {  width: 100% !important} td.kmImageContent {  padding-left: 0 !important; padding-right: 0 !important } img.kmImage { width: 100% !important } td.kmMobileStretch { padding-left: 0 !important; padding-right: 0 !important } table.kmSplitContentLeftContentContainer, table.kmSplitContentRightContentContainer, table.kmColumnContainer,td.kmVerticalButtonBarContentOuter table.kmButtonBarContent, td.kmVerticalButtonCollectionContentOuter table.kmButtonCollectionContent, table.kmVerticalButton, table.kmVerticalButtonContent { width: 100% !important } td.kmButtonCollectionInner {padding-left: 9px !important; padding-right: 9px !important; padding-top: 9px !important; padding-bottom: 9px !important } td.kmVerticalButtonIconContent,td.kmVerticalButtonTextContent,td.kmVerticalButtonContentOuter {padding-left: 0 !important; padding-right: 0 !important; padding-bottom: 9px !important }table.kmSplitContentLeftContentContainer td.kmTextContent,table.kmSplitContentRightContentContainer td.kmTextContent,table.kmColumnContainer td.kmTextContent, table.kmSplitContentLeftContentContainer td.kmImageContent,table.kmSplitContentRightContentContainer td.kmImageContent { padding-top: 9px !important} td.rowContainer.kmFloatLeft, td.rowContainer.kmFloatLeft, td.rowContainer.kmFloatLeft.firstColumn, td.rowContainer.kmFloatLeft.firstColumn,  td.rowContainer.kmFloatLeft.lastColumn, td.rowContainer.kmFloatLeft.lastColumn { float: left; clear: both;width: 100% !important}table.templateContainer, table.templateContainer.brandingContainer, div.templateContainer, div.templateContainer.brandingContainer,table.templateRow { max-width: 600px !important;width: 100% !important} h1 { font-size: 40px !important;line-height: 1.1 !important} h2 {font-size: 32px !important;line-height: 1.1 !important} h3 {font-size: 24px !important;line-height: 1.1 !important } h4 { font-size: 18px !important; line-height: 1.1 !important } td.kmTextContent { font-size: 14px !important; line-height: 1.3 !important } td.kmTextBlockInner td.kmTextContent { padding-right: 18px !important; padding-left: 18px !important } table.kmTableBlock.kmTableMobile td.kmTableBlockInner {padding-left: 9px !important; padding-right: 9px !important}table.kmTableBlock.kmTableMobile td.kmTableBlockInner .kmTextContent { font-size: 14px !important; line-height: 1.3 !important; padding-left: 4px !important; padding-right: 4px !important }}</style> <style> span.yshortcuts:hover { background-color: none !important; border: none !important }span.yshortcuts:active { background-color: none !important; border: none !important } span.yshortcuts:focus {background-color: none !important; border: none !important }.rowContainer .kmTextContent a:link { color: #15C; font-weight: normal; text-decoration: underline }.rowContainer .kmTextContent a:visited { color: #15C; font-weight: normal; text-decoration: underline }.kmTable .kmTableRow:last-child>td { border-bottom: none !important }</style> <style>#outlook a {padding-left: 0;padding-right: 0; padding-top: 0; padding-bottom: 0;.ReadMsgBody { width: 100% }.ExternalClass { width: 100%} span.yshortcuts { background-color: none !important; border: none !important}body { margin: 0; padding: 0} a {word-wrap: break-word !important; max-width: 100% } img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; max-width: 100% } img[align='left'] { margin-right: 0;} img[align='right'] { margin-left: 0;} table, td {border-collapse: collapse; table-layout: fixed }p {margin-left: 0;margin-right: 0; margin-top: 0;margin-bottom: 0; padding-bottom: 1em} #bodyTable, #bodyCell {height: 100% !important; margin: 0;width: 100% !important;table-layout: auto } #bodyTable { padding: 0 } #bodyCell { padding-top: 50px; padding-left: 20px; padding-bottom: 20px; padding-right: 20px;border-top: 0}body, #bodyTable { background-color: #F7F7F7} .templateContainer { border: 0 none #aaa; background-color: #fff; border-radius: 0 }.brandingContainer { background-color: transparent; border: 0 } .templateContainerInner { padding: 0} h1 {color: #222 !important;display: block; font-family: 'Helvetica Neue', Arial;font-size: 40px; font-style: normal; font-weight: normal; line-height: 1.1;letter-spacing: 0; margin-left: 0; margin-right: 0; margin-top: 0; margin-bottom: 20px; text-align: left} h2 {color: #222 !important; display: block; font-family: 'Helvetica Neue', Arial;font-size: 32px;font-style: normal; font-weight: bold; line-height: 1.1; letter-spacing: 0; margin-left: 0;margin-right: 0; margin-top: 0; margin-bottom: 16px; text-align: left} h3 { color: #222 !important; display: block; font-family: 'Helvetica Neue', Arial; font-size: 24px; font-style: normal;font-weight: bold;line-height: 1.1;letter-spacing: 0; margin-left: 0;margin-right: 0; margin-top: 0; margin-bottom: 12px;text-align: left} h4 { color: #222 !important; display: block;font-family: 'Helvetica Neue', Arial; font-size: 18px; font-style: normal; font-weight: italic;line-height: 1.1; letter-spacing: 0;margin-left: 0; margin-right: 0; margin-top: 0; margin-bottom: 9px; text-align: left} .rowContainer .kmTextContent { color: #222; font-family: 'Helvetica Neue', Arial; font-size: 14px; line-height: 1.3; letter-spacing: 0;text-align: left; max-width: 100%; word-wrap: break-word}.rowContainer .kmTextContent .kmParagraph { padding-bottom: 9px;}.kmImageContent { padding: 0; font-size: 0 } .kmImage { padding-bottom: 0; display: inline !important; vertical-align: top; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none;font-size: 12px; width: 100%} .kmButtonBlockInner, .kmButtonCollectionInner { min-width: 60px; padding: 9px 18px } .kmButtonContentContainer { border-top-left-radius: 5px; border-top-right-radius: 5px; border-bottom-right-radius: 5px; border-bottom-left-radius: 5px; background-color: #999; border-collapse: separate} .kmButtonContent { color: white; font-family: 'Helvetica Neue', Arial;font-size: 16px} .kmButton {font-weight: bold; line-height: 100%; text-align: center;text-decoration: none; color: white; font-family: 'Helvetica Neue', Arial; font-size: 16px} .kmButtonBarContent,.kmButtonCollectionContent { font-family: 'Helvetica Neue', Arial}.kmVerticalButtonContent { border-collapse: separate } .kmMobileOnly { display: none}.kmDesktopWrapHeader, .kmDesktopWrapHeaderMobileNone { display: inline-block } .kmHide { display: none}.kmMobileHeaderStackDesktopNone, .kmMobileWrapHeaderDesktopNone { display: none}.kmDesktopAutoWidth { width: 100%} </style></head><body><center><table align='center' border='0' cellpadding='0' cellspacing='0' data-upload-file-url='/ajax/email-editor/file/upload' data-upload-files-url='/ajax/email-editor/files/upload' id='bodyTable' width='100%'><tbody><tr> <td align='center' id='bodyCell' valign='top'> <div class='templateContainer' style='display: table; width:600px'> <div class='templateContainerInner'>  <table border='0' cellpadding='0' cellspacing='0' width='100%'> <tr> <td align='center' valign='top'> <br> <br> <br> </td> </tr> <tr> <td align='center' valign='top'>  <table border='0' cellpadding='0' cellspacing='0' class='templateRow' width='100%'><tbody> <tr> <td class='rowContainer kmFloatLeft' valign='top'>  <table border='0' cellpadding='0' cellspacing='0' class='kmTextBlock' width='100%'> <tbody class='kmTextBlockOuter'> <tr> <td class='kmTextBlockInner' valign='top'> <table align='left' border='0' cellpadding='0' cellspacing='0' class='kmTextContentContainer' width='100%'>  <tbody> <tr> <td class='kmTextContent' style='padding-top:9px;padding-bottom:9px;padding-left:18px;padding-right:18px;' valign='top'> <h3><span style='font-size: 13px;'>Hello There,</span></h3><h3><span style='font-size: 13px;'>we have great news to share with you !!!</span></h3> <h3><span style='font-size: 13px;'>CARRAT just launched a safety bracelet that contacts your loved one in case of danger.</span> </h3> <p>Once you clicked on the bracelet an emergency call is made and your exact location is shared via text message to 5 of your contacts.</p> <p><strong>This allows you to always be safe.</strong></p> <p>Feel free to have a look at the bracelet <a href='https://carrat-smart-bracelet-gps.kckb.st/40c94abf'> Click here.</a></p> <img src='https://bitcointutorial.net/carrotone.jpg' width='500px' height='300px' alt='carrotone'> </td> </tr> </tbody> </table> </td> </tr> </tbody></table> </td></tr></tbody> </table></td></tr> </table> </div> </div> <div style='display:none !important;visibility:hidden;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;'></div></td></tr></tbody> </table></center></body></html>"
                mail.send(msg)
            return ("<div style='width:700px; margin:auto; margin-top:150px; border-radius:20px; background-image: radial-gradient(circle farthest-side, #fceabb, #f8b500);padding:50px; text-align center;'><h1>Thank You All E-mails are Sent Successfully .....! </h1></div>")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port='19000')
