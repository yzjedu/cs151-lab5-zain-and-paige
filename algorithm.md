# Algorithm Document

1. set initial balance to 1000
2. ask user if they want to deposit withdraw, view balance, or exit 
3. convert options to lowercase
4. SENTINEL = 'e'
5. while options does not equal SENTINEL:
   1. if options is equal to 'w':
      1. ask user how much they want to withdraw 
      2. if withdraw is less than 0:
         1. output 'Error, cant input negative numbers try again'
      3. otherwise
         1. set new balance to the value of initial balance minus money withdraw
         2. output new balance 
      4. if new balance is less than 0:
         1. output 'warning'
   2. if otherwise options is equal to 'd':
      1. ask user how much they want to deposit
      2. if deposit is less than 0:
         1. output 'Error, cant input negative numbers try again'
      3. otherwise
         1. add deposit to initial balance
         2. output new balance 
   3. otherwise options equal 'v':
      1. output initial balance 
   4. otherwise options does not equal 'w', 'd', 'v', or 'e':
      1. output'That is not a valid choice, enter 'w', 'd', 'v', or 'e''
6. output'Thank you for using the atm'
      
