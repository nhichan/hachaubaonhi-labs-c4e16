def remove_dollar_sign(st):
    new_s = st.replace("$", "")
    return new_s

s = str(input('write down in US dollar: '))
sanitized_s = remove_dollar_sign(s)
print(sanitized_s)
