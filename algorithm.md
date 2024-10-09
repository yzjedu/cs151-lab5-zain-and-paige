# Algorithm Document

1. set initial balance to 1000
2. ask user if they want to deposit withdraw, view balance, or exit
3. convert options to lowercase
3. while options does not equal to 'w', 'd', 'v', or 'e'
3. while options does not equal 'e':
   1. ask user if they want to deposit withdraw, or view balance
   2. covert options to lowercase
   3. if options is equal to 'w'
      1. ask user how much they want to withdraw 
      2. set new balance to the value of initial balance minus money withdraw
      3. if new balance is less than 0:
         4. output 'warning'
   4. if otherwise options is equal to 'd':
      1. ask user how much they want to deposit
      2. add deposit to initial balance
   5. otherwise options equal 'v':
      1. output initial balance 
      
