
def analyze_password(
    password,
    min_length=8,
    require_digit=True,
    require_upper=True,
    require_symbol=False,
    banned_words=None
):

    if banned_words is None:
        banned_words =["abc","hovno","12345"]

    rules_total = 0
    rules_passed = 0
    missing_rules = []

    # 1. minimální délka
    rules_total += 1
    if len(password) >= min_length:
        rules_passed += 1
    else:
        missing_rules.append("krátký")

    # 2. číslice
    if require_digit:
        rules_total += 1
        if any(c.isdigit() for c in password):
            rules_passed += 1
        else:
            missing_rules.append("není číslo")

    # 3. velké písmeno
    if require_upper:
        rules_total += 1
        if any(c.isupper() for c in password):
            rules_passed += 1
        else:
            missing_rules.append("není velky pismeno")

    # 4. symbol
    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    if require_symbol:
        rules_total += 1
        if any(c in symbols for c in password):
            rules_passed += 1
        else:
            missing_rules.append("není specialní symbol")

    # 5. zakázaná slova
    rules_total += 1
    if any(word.lower() in password.lower() for word in banned_words):
        missing_rules.append("banned_word")
    else:
        rules_passed += 1

    # výpočet skóre
    score_percent = int((rules_passed / rules_total) * 100)

    is_strong = (rules_passed == rules_total)

    return (f"Je vše v pohodě? {is_strong}\nProcentuální podíl splněných pravidel vůči všem aktivním pravidlům {score_percent}% \nCo je blbě{missing_rules}")

print("=============================================================================================================================================================")
print(analyze_password("Test1234?", 8, True, True, False, None))
print("=============================================================================================================================================================")
print(analyze_password("Test1234", 8, require_symbol=True))
print("=============================================================================================================================================================")
print(analyze_password("hovno123", banned_words=["hovno", "kleslo"]))
print("=============================================================================================================================================================")