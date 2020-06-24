import requests

class BankDetails:
    '''
        class to fetch the response of one Bank and 
        make it accessible through functions
    '''
    def __init__(self,IFSC_Code):
        URL = "https://ifsc.razorpay.com/"
        self.result = requests.get(URL+IFSC_Code).json()

    def getBankName(self):
        bankName = self.result['BANK']
        print('Bank Name : ',bankName)
        return bankName

    def getBankContact(self):
        bankContact = self.result['CONTACT']
        print('Bank Contact : ',bankContact)
        return bankContact

    def getBankAddress(self):
        bankAddr = self.result['ADDRESS']
        print('Bank Address : ',bankAddr)
        return bankAddr
    
    def getBankBranch(self):
        bankBranch = self.result['BRANCH']
        print('Bank Branch : ',bankBranch)
        return bankBranch

    def getBankState(self):
        bankState = self.result['STATE']
        print('Bank State : ',bankState)
        return bankState

    def getBankCity(self):
        bankCity = self.result['CITY']
        print('Bank City : ',bankCity)
        return bankCity

IFSC_Code = 'MAHB0001716'
bank = BankDetails(IFSC_Code)
bank.getBankName()
bank.getBankContact()
bank.getBankBranch()
bank.getBankAddress()
bank.getBankCity()
bank.getBankState()