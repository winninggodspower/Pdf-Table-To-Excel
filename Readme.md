# Pdf Table to excel

This is a project extracts tables from pdf file to excel file.

To run on your machine you need to have python installed. you can do that from [https://www.python.org/downloads/](https://www.python.org/downloads/)
Then follow the below step.

1. clone this repo using 
    ```console
        git clone https://github.com/winninggodspower/<repo-name>/
    ```

2. install the requirements using .
    cd into the folder install the project dependency with the following command.
    ```console
        cd <repo-name>
        pip install requirements.txt
    ```

    > note: you need to have ***python*** and ***pip*** installed for this to work.
    To install pip visit: [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)


3. Install ghostscript.
    To install ghostcripts visit [https://www.ghostscript.com](https://www.ghostscript.com/releases/gsdnld.html).
    The project needs this to work. 
    
    And it need to be added to **path**. don't worry the installation process does this for you.

4. Test the project with.
    ```console
    python main.py foo.pdf
    ```

    the last paremeter should be the file location + filename

    e.g: say i have a file in downloads, the command will be
    ````console
    python main.py C:\Users\<Username>\Downloads\filename.pdf
    ````

    > Hope this helps
