

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

    def fix_account(self, account):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        if (account in self.accounts or not isinstance(account.name, str)):
            return False
        print(type(list(account.__dict__.keys())))
        print(list(account.__dict__.keys()))
        attributes = list(account.__dict__.keys())
        Corrupted &= False if (len(attributes) % 2) else True
        for attr in attributes:
            Corrupted &= True if (attr[0] == 'b') else True
        started_with = False
        for attr in attributes:
            if (attr.startswith('zip')):
                started_with = True
                break
            if (attr.startswith('addr')):
                started_with = True
                break
        Corrupted &= started_with
        Corrupted &= 'name' in attributes
        Corrupted &= 'id' in attributes
        Corrupted &= 'value' in attributes
        Corrupted &= isinstance(account.name, str)
        Corrupted &= isinstance(account.id, int)
        Corrupted &= isinstance(account.value, int) \
            or isinstance(account.value, float)
        return Corrupted

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
                or origin_account.value < amount or origin_account.value < 0:
            return False
        if (self.isCorrupted(origin_account)
                or self.isCorrupted(dest_account)):
            return(False)
        origin_account.value -= amount
        dest_account.value += amount
        return True
