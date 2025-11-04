def withdraw():
    if amount > 5000:
        raise ValueError("Amount exceeds limit.")
        raise Exception("Withdrawal Limit Exceeded.")
        print("Amount exceeds limit.")
try:
    withdraw(6000)
except ValueError as e:
    print("Error:", e)  
    except Exception as e:
    print("Error:", e)