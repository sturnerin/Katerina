# re.findall(r'\d', text)
# return ''.join(digits)
# =
# return re.sub(r'\D', '', text)

re.sub(r'\w+', 'whatever', s)
# если один или больше, заменяет

text = 'weird horror story'
short = re.sub(
    r'\s*(\w)\w+\s*',
    r'\1',
    text)
# 'w h s'

date = '03/4/2018'
new = re.sub(
    r'(\d\d)/(\d{1,2})/(\d{4})',
    r'\2.\1.\3',
    date)
# 4.03.2018

s = 'aaaaaaaamyyyybikeeeeeisssssssonnnnnnfireeeee'
print(re.sub(r'(\w)(\1+)(.*?)', r'\1+\3', s))
# or r'(\w)\1+', r'\1+'
# my+bike+is+on+fire
