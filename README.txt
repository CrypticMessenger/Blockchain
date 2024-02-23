- Initially transactions consists of :
transactions = [
    "0xA_0xB_100_BTC_1",
    "0xC_0xD_200_BTC_2",
    "0xE_0xF_300_BTC_3",
    "0xG_0xH_400_BTC_4",
    "0xI_0xJ_500_BTC_5",
    "0xK_0xL_600_BTC_6",
    "0xM_0xN_700_BTC_7",
    "0xO_0xP_800_BTC_8",
    "0xQ_0xR_900_BTC_9",
    "0xS_0xT_1000_BTC_10",
    "0xU_0xV_1100_BTC_11",
]
transactions here are in format of "senderAddr_receiverAddr_amount_currency_TxnId"

- Intitially array of transactions to verify consists of :
transactions_to_prove = ["0xA_0xB_100_BTC_1", "0xX_0xZ_600_BTC_99", "0xW_0xX_12_BTC_100"]

- To change the transactions & transactions_to_verify, you can change the values in the test.py file.
- it's expected to return True only for 0xA_0xB_100_BTC_1 and False for the rest of the transactions.

- to run the program:
```bash
python3 test.py
```
- You are expected to see level-wise transactions hash (last 10 characters), root hash, and the result of the verifications.
- Comments have been added to the code to explain the logic and the steps of the program.

- Printing proof for each verification makes the output unreadable and is thus omitted, you can choose to print it by uncommenting 
line 40 in the test.py file.