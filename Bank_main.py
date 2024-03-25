import bank as Bnk

a1 = Bnk.Account_holder("Skyler","123","93040","A")
a2 = Bnk.Account_holder("Marc","637","73821","C")
a3 = Bnk.Account_holder("Landon","982","54502","B")
a4 = Bnk.Account_holder("Opal","123","19240","A")
a5 = Bnk.Account_holder("Emily","923","20390","C")


a1.transfer(a2)
a2.withdrawl()
a2.withdrawl()
a3.deposit()
a4.display_Bal()