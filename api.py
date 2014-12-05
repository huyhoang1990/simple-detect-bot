

import mechanize


br = mechanize.Browser()
response = br.open('http://localhost:5000/signup')
print response.read()

br.select_form(nr=0)
br.form['user'] = "hoang"
br.form['pass'] = "asdf"

res = br.submit()

print res.read()
