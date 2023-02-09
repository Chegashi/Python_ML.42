

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount
    def transferTo(self, amount):
        self.value -= amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        if (isinstance(new_account, Account)):
            for account in self.accounts:
                if account.name == new_account.name:
                    return False
            self.accounts.append(new_account)
            return True
        else:
            return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        origin_account = None
        dest_account = None
        for account in self.accounts:
            if account.name == origin:
                origin_account = account
            if account.name == dest:
                dest_account = account
        if origin_account is None or dest_account is None \
                or origin_account.value < amount or origin_account.value < 0 \
                or self.isCorrupted(origin_account.name) \
                or self.isCorrupted(dest_account.name):
            return(False)
        origin_account.transfer(amount)
        dest_account.transferTo(amount)
        return True

    def isCorrupted(self, account_name):
        account = None
        for iter in self.accounts:
            if iter.name == account_name:
                account = iter
                break
        if account is None:
            print("Accompte not found")
            return None
        if len(account.__dict__) % 2 == 0:
            return True
        chekedlist = 0
        for attr in list(account.__dict__.keys()):
            if attr.startswith('b'):
                return True
            if attr.startswith('zip'):
                chekedlist |= 1
            if attr.startswith('addr'):
                chekedlist |= 2
            if attr == 'name':
                chekedlist |= 4
            if attr == 'id':
                chekedlist |= 8
            if attr == 'value':
                chekedlist |= 16
        if chekedlist != (1 | 2 | 4 | 8 | 16) :
            return True
        if not isinstance(account.name, str) or not isinstance(account.id, int) or \
            (not isinstance(account.value, int) and not isinstance(account.value, float)):
                return True
        return False

    def fix_account(self, account_name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        account = None
        print('0', self.accounts)
        for iter in self.accounts:
            print("1", iter.name, account_name)
            if iter.name == account_name:
                account = iter
                break
        if account is None:
            print("Accompte not found")
            return None
        chekedlist = 0
        for attr in account.__dict__:
            if attr.startswith('b'):
                delattr(self.attr)
            if attr.startswith('zip'):
                chekedlist |= 1
            if attr.startswith('addr'):
                chekedlist |= 2
            if attr == 'name':
                chekedlist |= 4
            if attr == 'id':
                chekedlist |= 8
            if attr == 'value':
                chekedlist |= 16
        if chekedlist & 1 == 0:
            setattr(account, 'zip', "QCobalHhiX")
        if chekedlist & 2 == 0:
            setattr(account, 'addr', "hzT1G75GWU")
        if chekedlist & 4 == 0 or (chekedlist & 4 and \
                                    not isinstance(account.name, str)):
            setattr(account, 'name', "JdhuH970wv")
        if chekedlist & 8 == 0 or (chekedlist & 8 and \
                                   not isinstance(account.id, int)):
            setattr(account, 'id', "061915120123")
        if chekedlist & 16 == 0 or (chekedlist & 16 and \
                                    not isinstance(account.value, int) \
                or not isinstance(account.value, float)):
            setattr(account, 'value', 1337)
        if len(account.__dict__) % 2 == 0:
            setattr(account, 'vini', 1337)
        return account
