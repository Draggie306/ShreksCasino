# TO DO LIST:
- Fix the code
- Add more games
- Make Konami Easter egg once per account, but increase reward
- ur mom


# HOW TO USE MY SUBROUTINES
- To add a value to a card's balance, paste in this: `change_credit_card_balance(10)` (and obviously change `10` to any number to add by. Or `-10` for -10.)
  - `money = money + x` → `change_credit_card_balance(x)`
  - `money = money - x` → `change_credit_card_balance(-x)`

- To get a credit balance, paste in this: 
`call_credit_balance(credit_card)` (`credit_card` is already determined from a user's earlier input). This will change the variable `money` to the money from the file. It will also print `You now have {money}.`.
  - `print(f"You now have {money}."` → `call_credit_balance(credit_card)`

# OTHER STUFF
- Use the **Version Control** tab on the left when you want to save some code you've done. This is useful in case we need to roll back the code quickly and easily. An epic tutorial is here: https://replit.com/talk/learn/Replit-Git-Tutorial/23331

### Versions
- 0.11: removed the annnoying tab at the top taking up half the screen
- 0.14:
  - added Brawl Box Simulator - brawl_box()
  - improved divisions between subroutines and games to allow for easier management and player experience