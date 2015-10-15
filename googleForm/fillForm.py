import mechanize

br = mechanize.Browser()
br.open("https://docs.google.com/forms/d/121wWtxzmOnyBH4jpPYZn4jFIbGpkx17skurEtQHbxpU/viewform?usp=send_form")
print br.read()
br.select_from(name="Armando Suarez Rivas")
br["Sign In Status:"] = ["In"]
br.submit()
