email = input("Aapka Email daliye: ").strip()

username = email[:email.index("@")]
doamin = email[email.index("@") + 1:]

print("Aappak Username hai ", username, " aur domain hai ", doamin)
