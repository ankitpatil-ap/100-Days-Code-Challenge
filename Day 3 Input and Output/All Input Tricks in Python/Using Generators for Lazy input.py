#Using Generators to lazily generate input values:

# Real-Life Problem: Lazy Data Loading for Financial Transaction Analysis

# Define a generator that lazily generates input values (financial transactions)
def input_generator():
    # Simulate a dataset of financial transactions
    financial_data = [
        {"amount": 100.00, "description": "Purchase", "category": "Shopping"},
        {"amount": 50.00, "description": "Dining", "category": "Food"},
        # ... more financial transactions
    ]

    # Yield each financial transaction lazily
    for transaction in financial_data:
        yield transaction

# Initialize the input generator
transaction_generator = input_generator()

# Process the financial transactions lazily
for transaction in transaction_generator:
    print("Processing transaction:", transaction)
    # Perform analysis or other processing on the transaction
