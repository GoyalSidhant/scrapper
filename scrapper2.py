import requests
from lxml import html  


print("--------------Start-----------------")

url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
response = requests.get(url) 

def get_captcha():
    text = 'dem0'

    return text 

""" name="form_rcdl:j_idt34:CaptchaID"
name="form_rcdl:tf_dlNO"
name="form_rcdl:tf_dob_input" """


text = get_captcha()
payload = {
    'form_rcdl:tf_dlNO':'DL-0420110149646',
    'form_rcdl:tf_dob_input':'09-02-1976',
    'form_rcdl:j_idt34:CaptchaID':text
}

response = requests.post(url , payload)
byte_data = response.content 
source_code = html.fromstring(byte_data) 


name = source_code.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[2]')
print(name)
doi = source_code.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[2]')
print(doi)
doe = source_code.xpath('//*[@id="form_rcdl:j_idt118"]/table[2]/tbody/tr[1]/td[3]')
print(doe)
classof  = source_code.xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[2]')
print(classof)

print("------------The End--------------")
