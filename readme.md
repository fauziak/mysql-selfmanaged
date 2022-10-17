Step 1: Creating a VM on GCP. Click "Create a VM"

Step 2: Set up the following settings
    
    a. Change the name for the VM or you can leave it as is.
    
    b. Under the "Machine Configuration" heading sleect Series "E2" and "Machine Type" to "e2-small..".
    
    c. Scroll down to "Boot Disk" and select the change button. Under "Operating System" select "Ubuntu" & change "Version" to "Ubuntu 1.04 LTS x86/64". Hit the "Select" button.

    d. Scroll down to "Firewall" and allow "HTTP traffic" and allow "HTTPS traffic".

    e. Hit "Create".

Step 3: After creating the new VM uner the "Connect" colum select the SSH dropdown, select the option " Open in browser window", wait till a terminal opens up. 

Step 4: Run the following commands in the new terminal thats opened up

    a. sudo apt-get update 

    b. sudo apt install mysql-server mysql-client 

    c. sudo mysql (logging into MySQL)

    d. CREATE USER ‘USERNAME'@'%' IDENTIFIED BY ‘PASSWORD’;

    e. select user from mysql.user; (this confirms the username created)

    f. GRANT ALL PRIVILEGES ON *.* TO 'USESRNAME'@'%' WITH GRANT OPTION;

    g. CREATE database databasename

    h. sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf/etc/init.d/mysql restart
