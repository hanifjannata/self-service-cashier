import self_service_cashier as ssc

user = ssc.Transaction()
# Test Case 1
#user.add_item("Ayam Goreng", 2, 20000)
#user.add_item("Pasta Gigi", 3, 15000)

# Test Case 2
#user.delete_item("Pasta Gigi")

# Test Case 3
#user.reset_transaction()

# Test Case 4
user.add_item("Ayam Goreng", 2, 20000)
user.add_item("Pasta Gigi", 3, 15000)
user.add_item("Mobil Mainan", 1, 200000)
user.add_item("Mie Instan", 5, 3000)
user.total_price()
