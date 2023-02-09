from the_bank import Account, Bank
bank = Bank()
john = Account(
    'William John',
    zip='100-064',
    brother="heyhey",
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    lol = "hihi"
)
# bank.fix_account(john)
bank.fix_account('William John')